from ordeq import Input, node


@node(inputs=[Input[str]("a")])
def my_node(*, a):
    print(a)
