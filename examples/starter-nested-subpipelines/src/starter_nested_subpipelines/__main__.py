import logging

from ordeq import run
from starter_nested_subpipelines import nl

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    run(nl)
