## Resource

```python
from ordeq import Input, InputHook, Output, OutputHook, node, run
from ordeq_common import StringBuffer


class MyInputHook(InputHook[str]):
    def before_input_load(self, io: Input[str]) -> None:
        print("Before loading data from:", io)

    def after_input_load(self, io: Input[str], data: str) -> None:
        print("After loading data from:", io)


class MyOutputHook(OutputHook[str]):
    def before_output_save(self, io: Output[str], data: str) -> None:
        print("Before saving data to:", io)

    def after_output_save(self, io: Output[str], data: str) -> None:
        print("After saving data to:", io)


hooked_input = StringBuffer("hello world").with_input_hooks(MyInputHook())
hooked_output = StringBuffer().with_output_hooks(MyOutputHook())


def hello_world(input_data: str) -> str:
    print(input_data.upper())
    return input_data[::-1]


run(node(hello_world, inputs=hooked_input, outputs=hooked_output))
print(hooked_output.load())

```

## Exception

```text
AttributeError: 'NoneType' object has no attribute 'items'
  File "/packages/ordeq/src/ordeq/_resolve.py", line LINO, in _resolve_strings_to_subs
    for old, new in subs.items():
                    ^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in run
    _resolve_strings_to_subs(io)
    ~~~~~~~~~~~~~~~~~~~~~~~~^^^^

  File "/packages/ordeq/tests/resources/hooks/io_hooks.py", line LINO, in <module>
    run(node(hello_world, inputs=hooked_input, outputs=hooked_output))
    ~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "<frozen importlib._bootstrap>", line LINO, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line LINO, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```