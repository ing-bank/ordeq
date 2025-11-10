## Resource

```python
from ordeq import run

run("example_1", hooks=["example_1.hooks:MyHook"])

```

## Output

```text
Starting the run
Name: John
Name: John
Finished the run

```

## Logging

```text
INFO	ordeq.io	Loading NameGenerator(name='John')
INFO	ordeq.runner	Running node "hello" in module "example_1.wrapped_io"
INFO	ordeq.io	Saving SayHello(name=NameGenerator(name='John'), writer=(NamePrinter(),))
INFO	ordeq.io	Saving NamePrinter()
INFO	ordeq.runner	Running node "print_message" in module "example_1.wrapped_io"
INFO	ordeq.io	Saving NamePrinter()

```