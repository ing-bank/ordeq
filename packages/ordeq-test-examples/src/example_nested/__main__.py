from ordeq import run

from example_nested.subpackage.subsubpackage.hello_relative import (
    world_relative,
)

run(world_relative)
