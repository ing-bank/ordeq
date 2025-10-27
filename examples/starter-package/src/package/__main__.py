import logging

import pipeline
from ordeq import run

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    run(pipeline)
