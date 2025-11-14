from pprint import pprint

import example_namespace.namespace
from ordeq._resolve import _resolve_module_globals

pprint(_resolve_module_globals(example_namespace.namespace))
