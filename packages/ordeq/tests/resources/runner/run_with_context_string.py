from ordeq._runner import run

run("example_nested.subpackage.subsubpackage.hello:world", verbose=True)

print("Should assign FQNs from context:")
run(
    "example_nested.subpackage.subsubpackage.hello:world",
    verbose=True,
    context="example_nested",
)

print("Should assign FQNs from context:")
run(
    "example_nested.subpackage.subsubpackage.hello:world",
    verbose=True,
    context="example_nested.subpackage",
)

print("Should assign FQNs from context:")
run(
    "example_nested.subpackage.subsubpackage.hello:world",
    verbose=True,
    context="example_nested.subpackage.subsubpackage",
)

print("Should assign FQNs from context:")
run(
    "example_nested.subpackage.subsubpackage.hello:world",
    verbose=True,
    context="example_nested.subpackage.subsubpackage.hello",
)

print("FQNs not found in context:")
run(
    "example_nested.subpackage.subsubpackage.hello:world",
    verbose=True,
    context="example_nested.subpackage.subsubpackage.hello_relative",
)

print("FQNs not found in context:")
run(
    "example_nested.subpackage.subsubpackage.hello:world",
    verbose=True,
    context="example_nested.catalog",
)
