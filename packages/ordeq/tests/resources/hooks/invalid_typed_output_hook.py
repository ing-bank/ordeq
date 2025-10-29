from ordeq import Output, OutputHook


class MyInvalidTypedOutputHook(OutputHook[str]):
    def before_output_save(self, op: Output[bytes], data: bytes) -> None:
        print(f"saving data `{data}` to output `{op}`")


_ = MyInvalidTypedOutputHook()
