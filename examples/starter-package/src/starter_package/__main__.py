import logging

from ordeq import run

from starter_package import pipeline

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    run(pipeline)
