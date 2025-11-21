import inspect
from collections.abc import Callable


def is_async(obj: Callable) -> bool:
    return inspect.iscoroutinefunction(obj)
