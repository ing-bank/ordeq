## Resource

```python
from dataclasses import dataclass

from ordeq import IO, Input, node, run
from ordeq_common import Print


@dataclass(frozen=True)
class Request(IO[str]):
    """Dummy IO class representing an API request."""

    url: str

    def load(self) -> None:
        pass

    def save(self, _) -> None:
        print("{'weather': 'sunny'}")


country = Input[str]("NL")
request = Request(url="whatstheweather.com")


@node(inputs=country, outputs=request)
def get_weather_for_country(cntry: str) -> str:
    match cntry:
        case "The Netherlands":
            return "NL"
        case "Germany":
            return "DE"
        case _:
            return "USA"


@node(inputs=request, outputs=Print())
def print_answer(answer: str) -> str:
    return f"The API responded: '{answer}'"


run(get_weather_for_country, print_answer)

```

## Output

```text
{'weather': 'sunny'}
The API responded: 'USA'

```

## Logging

```text
DEBUG	ordeq.io	Persisting data for Input(id=ID1)
DEBUG	ordeq.io	Loading cached data for Input 'get_weather_for_country:cntry' in module '__main__'
INFO	ordeq.runner	Running node 'get_weather_for_country' in module '__main__'
INFO	ordeq.io	Saving Request 'print_answer:answer' in module '__main__'
DEBUG	ordeq.io	Persisting data for Request 'print_answer:answer' in module '__main__'
DEBUG	ordeq.io	Loading cached data for Request 'print_answer:answer' in module '__main__'
INFO	ordeq.runner	Running node 'print_answer' in module '__main__'
INFO	ordeq.io	Saving Print()
DEBUG	ordeq.io	Unpersisting data for Request 'print_answer:answer' in module '__main__'

```