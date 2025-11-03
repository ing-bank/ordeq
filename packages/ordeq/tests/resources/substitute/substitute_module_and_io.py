from example_catalogs import local, remote
from example_catalogs.remote import hello
from ordeq._substitute import _build_substitution_map
from ordeq_common import Print

print(_build_substitution_map({local: remote, hello: Print()}))
