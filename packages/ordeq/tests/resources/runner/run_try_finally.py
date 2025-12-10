from ordeq import Input, node, run


class Connection(Input[str]):
    @staticmethod
    def load() -> str:
        try:
            print("Connection opened")
            return "connection"
        finally:
            print("Connection closed")


conn = Connection()


@node(inputs=conn)
def process_first(connection: str) -> None:
    print(f"Processing first with {connection}")


@node(inputs=conn)
def process_second(connection: str) -> None:
    print(f"Processing second with {connection}")


run(process_first, process_second)

conn.load()
