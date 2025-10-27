import logging

from ordeq import run

from package import nl

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    run(nl)
