from ordeq import IO
from ordeq._substitute import _substitutes_modules_to_ios
from ordeq_common import BytesBuffer

buffer = BytesBuffer()

print(_substitutes_modules_to_ios({buffer: IO()}))
