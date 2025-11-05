# Captures the behaviour of an IO that doesn't cache loaded data.
# For some IOs, like streams and buffers, caching is counter-productive:
# repeated calls to `load()` should reload the data from scratch.
from dataclasses import dataclass

from ordeq import IO


@dataclass(kw_only=True)
class Counter(IO[int], cache=False):
    counter: int = 0

    def load(self) -> int:
        self.counter += 1
        return self.counter

    def save(self, num: int) -> None:
        print(num)


counter = Counter()
print(counter.load())  # expect 1
print(counter.load())  # expect 2
