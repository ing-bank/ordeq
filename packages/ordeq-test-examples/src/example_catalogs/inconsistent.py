# This catalog is inconsistent with local because it doesn't define
# the 'result' IO
from ordeq_common import StringBuffer

hello = StringBuffer("Hello from remote")
# Uncommenting this line would make the catalog consistent with local:
# 'result' = StringBuffer()
