## Resource

```python
# Users should be able to run runnables in idiomatic Python:
# 1. running a pipeline should be as simple as calling a function
# 2. args should be passed in-memory, not through IOs
from typing import Any

from ordeq import IO, node, pipeline

x1 = IO[Any]()
x2 = IO[Any]()
x3 = IO[Any]()
y = IO[Any]()


@node(inputs=[x1, x2, x3])
def n1(a, b, c):
    return a + 1 + 2 * b + 3 * c


@node(inputs=n1)
def n2(b):
    return b * 2


@node(inputs=n2, outputs=y)
def n3(c):
    return c - 3


my_pipeline = pipeline(n1, n2, n3, inputs=[x1, x2, x3], outputs=[y])

output = my_pipeline(30, 1, 3)
assert output == 81

print("Should raise error for wrong number of args")
my_pipeline(30, 1)

```

## Output

```text
Should raise error for wrong number of args
ValueError: Expected 3 inputs, but got 2.
  File "/packages/ordeq/src/ordeq/_pipeline.py", line LINO, in runner
    raise ValueError(
        f"Expected {len(inputs)} inputs, but got {len(args)}."
    )

  File "/packages/ordeq/tests/resources/pipeline/modular_multiple_args.py", line LINO, in <module>
    my_pipeline(30, 1)
    ~~~~~~~~~~~^^^^^^^

  File "<frozen runpy>", line LINO, in _run_code

  File "<frozen runpy>", line LINO, in _run_module_code

  File "<frozen runpy>", line LINO, in run_path

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    run_path(str(file_path), run_name="__main__")
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```

## Logging

```text
WARNING	ordeq.preview	The pipeline function is experimental and may change in future releases.
INFO	ordeq.io	Loading Literal(30)
INFO	ordeq.io	Loading Literal(1)
INFO	ordeq.io	Loading Literal(3)
INFO	ordeq.runner	Running view '__main__:n1'
INFO	ordeq.runner	Running view '__main__:n2'
INFO	ordeq.runner	Running node '__main__:n3'
INFO	ordeq.io	Saving Buffer(value=None)
INFO	ordeq.io	Loading Buffer(value=81)

```