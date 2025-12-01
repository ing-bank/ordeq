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

## Output

```text
Before loading data from: StringBuffer 'hello_world:input_data' in module '__main__'
After loading data from: StringBuffer 'hello_world:input_data' in module '__main__'
HELLO WORLD
Before saving data to: StringBuffer(_buffer=<_io.StringIO object at HASH1>)
After saving data to: StringBuffer(_buffer=<_io.StringIO object at HASH1>)
dlrow olleh

```

## Logging

```text
INFO	ordeq.io	Loading StringBuffer 'hello_world:input_data' in module '__main__'
DEBUG	ordeq.io	Persisting data for StringBuffer 'hello_world:input_data' in module '__main__'
INFO	ordeq.runner	Running Node(func=__main__:hello_world, ...)
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH1>)
DEBUG	ordeq.io	Persisting data for StringBuffer(_buffer=<_io.StringIO object at HASH1>)
DEBUG	ordeq.io	Unpersisting data for StringBuffer 'hello_world:input_data' in module '__main__'
DEBUG	ordeq.io	Unpersisting data for StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH1>)

```