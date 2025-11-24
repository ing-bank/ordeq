
import json
from collections import defaultdict

from ordeq._resolve import _resolve_packages_to_modules
from ordeq._scan import scan
if __name__ == "__main__":
    import example_1

    def pprint(obj):
        print(json.dumps(obj, indent=4, default=str))

    submodules = list(_resolve_packages_to_modules(example_1))
    _, ios = scan(*submodules)
    print("discovered IOs")
    io_to_fqns = defaultdict(list)
    for io_fq, io_obj in ios:
        io_to_fqns[id(io_obj)].append(io_fq)
    multi_ios = {
        key: value for key, value in io_to_fqns.items() if len(value) > 1
    }
    pprint(multi_ios)
    multi_modules = {
        module_name for item in multi_ios.values() for module_name, _ in item
    }

    references = []
    for mod in submodules:
        if mod.__name__ not in multi_modules:
            continue

        symbol_to_module = _module_to_imports(mod, multi_modules)
        references.extend((mod.__name__, name) for name in symbol_to_module)

    # iterate over multi_ios and remove references
    for io_id, fqns in io_to_fqns.items():
        for fqn in fqns:
            if fqn in references:
                fqns.remove(fqn)
        if len(fqns) == 1:
            io_to_fqns[io_id] = io_to_fqns[io_id][0]

    print("Final IO to FQNs mapping:")
    pprint(io_to_fqns)
