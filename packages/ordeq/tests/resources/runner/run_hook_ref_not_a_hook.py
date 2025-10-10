from ordeq import run

run(
    "packages.example",
    hooks=["packages.example.hooks:other_obj"]
)
