from ordeq import Input, node

A = Input[str]("A")
B = Input[str]("B")


@node(inputs=A)
def Ap(data: str) -> str:
    return data.lower()


@node(inputs=B)
def Bp(data: str) -> str:
    return data * 3


@node(inputs=[Ap, Bp])
def AB(a: str, b: str) -> str:
    return a + b


@node(inputs=AB)
def print_result(data: str) -> None:
    print(data)


# Additional checks
D = Input[str]("D")


@node(inputs=[A, D], checks=[A])
def check_a(a: str, d: str) -> None:
    assert a != d, "A and D should not be equal"


@node(inputs=[Ap], checks=[Ap])
def check_ap(ap: str) -> None:
    assert ap.islower(), "Ap should be lowercase"


@node(inputs=[Bp], checks=[Bp])
def check_bp(bp: str) -> None:
    assert len(bp) == 3 * len("B"), "Bp should be three times the length of B"


@node(inputs=[Ap, Bp], checks=[Ap, Bp])
def check_join(ap: str, bp: str) -> None:
    assert len(ap) + len(bp) == 4


@node(inputs=[AB], checks=[AB])
def check_ab(ab: str) -> None:
    assert "a" in ab, "AB should contain 'a'"
