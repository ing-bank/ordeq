# Nodes

Nodes are functions representing a piece of data pipeline logic.
Typically, a node takes some data as input, transforms it, and returns the transformed data as output.
Nodes can be created by decorating a function with the `@node` decorator:

=== "nodes.py"
    ```python
    from ordeq import node
    from typing import Iterable

    @node
    def greet(names: Iterable[str]) -> None:
        """Prints a greeting for each person."""
        for name in names:
            print(f"Hello, {name}!")
    ```

Like functions, each node can have no, one, or more than one input(s), and return no, one, or more than one output(s).
In data pipelines, the inputs and outputs usually represent data that is processed by the pipeline.

### Specifying inputs and outputs

Suppose we want to greet a list of people whose names are provided in a CSV.
Let's use the CSV IO discussed in the [IO](io.md) section.
First we define the CSV IO in `catalog.py`. Next, we modify the node in `nodes.py`:

=== "nodes.py"
    ```python
    from ordeq import node
    import catalog

    @node(inputs=catalog.names)
    def greet(names: tuple[str, ...]):
        """Prints a greeting for each person."""
        for name in names:
            print(f"Hello, {name}!")
    ```

=== "catalog.py"
    ```python
    from ordeq_files import CSV
    from pathlib import Path

    names = CSV(path=Path("names.csv"))
    ```

By specifying `names` as the input, we inform Ordeq that the `greet` node should use the data from `names.csv` when the node is run.

!!!note "Where to define IOs"
    Although you can define IOs anywhere in your project, it is best practice to define them in a separate module.
    Such a module is often referred to as a "catalog" and is discussed in more detail in the [catalogs][catalog] section.


Similarly, we can add a `greetings` IO and specify it as output to the `greet` node:

=== "nodes.py"
    ```python
    import catalog

    @node(inputs=catalog.names, outputs=catalog.greetings)
    def greet(names: tuple[str, ...]) -> list[str]:
        """Returns a greeting for each person."""
        greetings = []
        for name in names:
            greetings.append(f"Hello, {name}!")
        return greetings
    ```

=== "catalog.py"
    ```python
    from ordeq_files import CSV, Text
    from pathlib import Path

    names = CSV(path=Path("names.csv"))
    greetings = Text(path=Path("greetings.txt"))
    ```

!!!info "Nodes behave like plain functions"
    The `@node` decorator only registers the function as a node, it does not change the function's behavior:

    ```pycon
    >>> type(greet)
    function
    >>> greet(["Alice", "Bob"])
    ["Hello, Alice!", "Hello, Bob!"]
    >>> greet(greet(["Alice"]))
    "Hello, Hello, Alice!!"
    >>> greet.__doc__
    "Prints a greeting for each person."
    >>> greet.__annotations__
    {'names': typing.Iterable[str], 'return': list[str]}
    ```

    This also means the node can be unit tested like any other function.


### Running a node

Nodes can be run as follows:

```pycon
>>> from ordeq import run
>>> run(greet)
```

Let's break down what happens when a node is run:

- the node inputs (`names`) are loaded and passed to the function `greet`
- the function `greet` is executed
- the values returned by `greet` are saved to the node outputs (`greetings`).

Running `greet` is therefore roughly equivalent to:

```pycon
>>> names = catalog.names.load()
>>> greetings = greet(names)
>>> catalog.greetings.save(greetings)
```

Because Ordeq handles the loading and saving of the inputs and outputs, you can focus on the transformation in the node.

### Running multiple nodes

Even the simplest data pipelines consist of multiple steps.
Usually, one step depends on the output of another step.
Let's extend our example with another node that parses the name to greet from a YAML file:

=== "nodes.py"
    ```python hl_lines="3-9"
    import catalog

    @node(
        inputs=catalog.invitees,
        outputs=catalog.names,
    )
    def parse_names(invitees: dict) -> list[str]:
        """Parse the names from the invitees data."""
        return [invitee["name"] for invitee in invitees]

    @node(
        inputs=catalog.names,
        outputs=catalog.greetings
    )
    def greet(names: tuple[str, ...]) -> list[str]:
        """Returns a greeting for each person."""
        greetings = []
        for name in names:
            greetings.append(f"Hello, {name}!")
        return greetings
    ```

=== "catalog.py"
    ```python hl_lines="4"
    from ordeq_files import CSV, Text, YAML
    from pathlib import Path

    invitees = YAML(path=Path("invitees.yaml"))
    names = CSV(path=Path("names.csv"))
    greetings = Text(path=Path("greetings.txt"))
    ```

Note that `parse_names` outputs the `names` IO, which is input to the `greet` node.
When we run the two nodes together, Ordeq will automatically pass the output of `parse_names` to `greet`:

```pycon
>>> run(parse_names, greet)
```

This is roughly equivalent to:

```pycon
>>> invitees = catalog.invitees.load()
>>> names = parse_names(invitees)
>>> catalog.names.save(names)
>>> greetings = greet(parsed_names)
>>> catalog.greetings.save(greetings)
```

As before, Ordeq handles the loading and saving of inputs and outputs.
But now, it also takes care of passing the outputs of one node as inputs to another.

!!!note "Dependency resolution"
    Ordeq resolves the [DAG (Directed Acyclic Graph)][dag] of the nodes that are run, ensuring that each node is run in the correct order based on its dependencies.
    This also means an IO cannot be outputted by more than one node.

### Retrieving results

The result of `run` is a dictionary containing the data that was loaded or saved by each IO:

```pycon
>>> result = run(parse_names, greet)
>>> result[catalog.names]
["Abraham", "Adam", "Azul", ...]
>>> result[catalog.greetings]
["Hello, Abraham!", "Hello, Adam!", "Hello, Azul!", ...]
```

This works much like a cache of the processed data for the duration of the run.
Of course, you can also load the data directly from the IOs:

```
>>> greetings.load()
["Hello, Abraham!", "Hello, Adam!", "Hello, Azul!", ...]
```

This has the overhead of loading the data from storage, but it can be useful if you want to access the data after the run has completed.

### _Advanced_: node tags

Nodes can be tagged to help organize and filter them.
Tags can be set using the `tags` parameter in the `@node` decorator:


=== "nodes.py"
    ```python
    import catalog

    @node(
        inputs=catalog.names,
        outputs=catalog.greetings,
        tags=["size:large"]
    )
    def greet(names: Iterable[str]) -> None:
        """Returns a greeting for each person."""
        greetings = []
        for name in names:
            greetings.append(f"Hello, {name}!")
        return greetings


    ```

The tags can be retrieved as follows:

```pycon
>>> from ordeq.framework import get_node
>>> node = get_node(greet)
>>> node.tags
['size:large']
```

Tags are currently used by Ordeq extensions such as `ordeq-cli-runner`, or `ordeq-viz`.
Refer to the documentation of these extensions for more information.

!!!success "Where to go from here?"
    - Have a look at the [example project][example-project] to see how nodes are used in practice
    - See how to extend inject custom logic with [node hooks][hooks]
    - Check out the [guide on testing nodes][testing-guide]

[catalog]: ../concepts/catalogs.md
[hooks]: hooks.md
[testing-guide]: ../../guides/testing_nodes.md
[dag]: https://en.wikipedia.org/wiki/Directed_acyclic_graph
[example-project]: ../../guides/examples/example-project/README.md
