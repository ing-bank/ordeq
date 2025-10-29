from ordeq import node, run


@node
def print_message():
    print("Hello from printer")


run(print_message, verbose=True)

show_message = print_message

run(show_message, verbose=True)
