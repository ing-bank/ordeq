from ordeq import Output


class ExampleStaticIO(Output[str]):
    @staticmethod
    def save(hello: str, world: str) -> None:
        print(f"{hello}, {world}!")


print("Expect error")
_ = ExampleStaticIO()
