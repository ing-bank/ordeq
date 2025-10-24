## Resource

```python
from ordeq import Output, OutputHook


class MyInvalidTypedOutputHook(OutputHook[str]):
    def before_output_save(
        self, op: Output[bytes], data: bytes
    ) -> None:
        print(f"saving data `{data}` to output `{op}`")


_ = MyInvalidTypedOutputHook()

```

## Typing

```text
packages/ordeq/tests/resources/hooks/invalid_typed_output_hook.py:6: error: Argument 1 of "before_output_save" is incompatible with supertype "ordeq._hook.OutputHook"; supertype defines the argument type as "Output[str]"  [override]
packages/ordeq/tests/resources/hooks/invalid_typed_output_hook.py:6: note: This violates the Liskov substitution principle
packages/ordeq/tests/resources/hooks/invalid_typed_output_hook.py:6: note: See https://mypy.readthedocs.io/en/stable/common_issues.html#incompatible-overrides
packages/ordeq/tests/resources/hooks/invalid_typed_output_hook.py:6: error: Argument 2 of "before_output_save" is incompatible with supertype "ordeq._hook.OutputHook"; supertype defines the argument type as "str"  [override]
packages/ordeq/tests/resources/hooks/invalid_typed_output_hook.py:8: error: If x = b'abc' then f"{x}" or "{}".format(x) produces "b'abc'", not "abc". If this is desired behavior, use f"{x!r}" or "{!r}".format(x). Otherwise, decode the bytes  [str-bytes-safe]
Found 3 errors in 1 file (checked 1 source file)

```