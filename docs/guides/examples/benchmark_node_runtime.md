# Benchmarking node runtime

Node [hooks](../../getting-started/concepts/hooks.md) can be used to keep
track of node execution durations. Using hooks to achieve this has the
advantage that the timing does not add cognitive complexity to the dataset
transformations. It also avoids repetitive boilerplate code inside the nodes.

```pycon title="timer_hook.py"
>>> from time import perf_counter
>>>
>>> from ordeq import Node, NodeHook
>>>
>>> class TimerHook(NodeHook):
...     """Hook to time nodes."""
...
...     def __init__(self):
...         self.node_timing = {}
...
...     def before_node_run(self, node: Node) -> None:
...         self.node_timing[hash(node)] = perf_counter()
...
...     def after_node_run(self, node: Node) -> None:
...         start = self.node_timing[hash(node)]
...         end = perf_counter()
...         function_name = node.func.__name__
...         print(f"Executing `{function_name}` took {end - start:.2f}s")
>>>
>>> timer = TimerHook()

```

Usage:

```pycon
>>> from ordeq import node, run
>>>
>>> @node(inputs=[...], outputs=[...])
... def my_transformation_function(data):
...     ...
>>> run(my_transformation_function, hooks=[timer])  # doctest: +SKIP
```
