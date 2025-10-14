import multiprocessing
import time

import pytest
import requests
import requests.exceptions
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    id: int
    name: str


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/nok/", status_code=418)
def nok():
    # Endpoint that only responds with a non-OK HTTP status
    return


@pytest.fixture(scope="session")
def host():
    return "localhost"


@pytest.fixture(scope="session")
def port():
    return 8001


@pytest.fixture(scope="session")
def url(host, port):
    return f"http://{host}:{port}"


def serve():
    uvicorn.run(app, host="localhost", port=8001)


@pytest.fixture(scope="session", autouse=True)
def api(url):
    """
    Fixture that spins up the FastAPI server in a separate process. The
    fixture yields once the API root endpoint is reachable, or after a
    timeout.
    """

    process = multiprocessing.Process(target=serve, args=(), daemon=True)
    process.start()
    start = time.time()
    while (time.time() - start) < 10:
        try:
            requests.get(f"{url}/", timeout=10)
            break
        except requests.exceptions.ConnectionError:
            time.sleep(0.1)
    yield
    process.terminate()
