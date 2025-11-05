# Captures the behaviour of an IO that doesn't cache saved data.
# For some IOs, like streams and buffers, caching is counter-productive:
# repeated calls to `load()` should reload the data from scratch.
from dataclasses import dataclass

from ordeq import IO


@dataclass(kw_only=True)
class Counter(IO[int], cache=False):
    counter: int = 0

    def save(self, _: int) -> None:
        self.counter += 1
        print(self.counter)


counter = Counter()
counter.save(123)  # expect 1
counter.save(123)  # expect 2
