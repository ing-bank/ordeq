from function_reuse import catalog
from function_reuse.catalog import A, B
from function_reuse.func_defs import print_input
from ordeq import node

a = node(print_input, inputs=A)
b = node(print_input, inputs=B)
c = node(print_input, inputs=catalog.C)

d = node(print_input, inputs=catalog.D)

node(print_input, inputs=A)
another_name = a


@node(inputs=A)
def pi(i):
    return print_input(i)


pipeline = {
    a,
    b,
    node(print_input, inputs=A),
    node(print_input, inputs=A),
    node(print_input, inputs=A),
}
