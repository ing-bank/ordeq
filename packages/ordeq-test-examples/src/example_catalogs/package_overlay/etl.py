from typing import Any

from ordeq import IO
from ordeq_common import StringBuffer

clients = StringBuffer("clients")
txs = IO[Any]()
temp = 1234  # Not an IO
