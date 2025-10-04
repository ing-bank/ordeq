from ordeq import Input, Output
from ordeq_common import StringBuffer


class MockInput(Input[str]):
    def load(self) -> str:
        return "hello"


class MockOutput(Output[str]):
    def save(self, data: str):
        print("data", data)


Hello = StringBuffer()
World = StringBuffer()
TestInput = MockInput()
TestOutput = MockOutput()
