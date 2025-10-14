from ordeq import node
from ordeq._nodes import get_node
from ordeq_common import Literal


class D:
    @staticmethod
    def list_buckets() -> list[str]:
        return ["bucket1", "bucket2", "bucket3"]


@node(client=Literal(Client()))
def view(client: Client) -> list[str]:
    return client.list_buckets()


@node(inputs=view)
def n(v: str) -> None:
    print(f"Node received {v}")


print(repr(get_node(view)))
print(repr(get_node(n)))
