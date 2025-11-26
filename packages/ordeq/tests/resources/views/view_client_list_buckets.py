from ordeq import Input, node, run


class Client:
    @staticmethod
    def list_buckets() -> list[str]:
        return ["bucket1", "bucket2", "bucket3"]


@node(inputs=Input(Client()))
def buckets(client: Client) -> list[str]:
    return client.list_buckets()


@node(inputs=buckets)
def print_buckets(buckets: list[str]) -> None:
    for bucket in buckets:
        print(bucket)


run(print_buckets, verbose=True)
