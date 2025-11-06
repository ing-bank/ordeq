# Captures the behaviour when resolving a package catalog to IO.
from pprint import pprint

import ordeq_dev_tools
from ordeq._resolve import _resolve_package_to_ios

ios = _resolve_package_to_ios(ordeq_dev_tools)
pprint(ios)
