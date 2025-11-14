from ordeq import Output


class Example(Output[str]):
    def save(self, df: str) -> None:
        print("saving!", df)


data = "..."

example = Example()
example.save(df=data)  # should give an error
