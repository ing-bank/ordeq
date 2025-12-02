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
  File "/packages/ordeq/src/ordeq/_pipeline.py", line LINO, in __call__
    raise ValueError(
        f"Expected {len(self.inputs)} inputs, but got {len(args)}."
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
DEBUG	ordeq.io	Persisting data for Input(id=ID1)
DEBUG	ordeq.io	Persisting data for Input(id=ID2)
DEBUG	ordeq.io	Persisting data for Input(id=ID3)
DEBUG	ordeq.io	Loading cached data for Input(id=ID1)
DEBUG	ordeq.io	Loading cached data for Input(id=ID2)
DEBUG	ordeq.io	Loading cached data for Input(id=ID3)
INFO	ordeq.runner	Running view 'n1' in module '__main__'
DEBUG	ordeq.io	Persisting data for IO 'n2:b' in module '__main__'
DEBUG	ordeq.io	Loading cached data for IO 'n2:b' in module '__main__'
INFO	ordeq.runner	Running view 'n2' in module '__main__'
DEBUG	ordeq.io	Persisting data for IO 'n3:c' in module '__main__'
DEBUG	ordeq.io	Loading cached data for IO 'n3:c' in module '__main__'
INFO	ordeq.runner	Running node 'n3' in module '__main__'
DEBUG	ordeq.io	Persisting data for IO(id=ID4)
DEBUG	ordeq.io	Unpersisting data for IO 'n2:b' in module '__main__'
DEBUG	ordeq.io	Unpersisting data for IO 'n3:c' in module '__main__'
DEBUG	ordeq.io	Loading cached data for IO(id=ID4)

```