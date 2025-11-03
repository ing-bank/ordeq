from ordeq import IO
from ordeq._substitute import _build_substitution_map
from ordeq_common import BytesBuffer

buffer = BytesBuffer()

print(_build_substitution_map({buffer: IO()}))
