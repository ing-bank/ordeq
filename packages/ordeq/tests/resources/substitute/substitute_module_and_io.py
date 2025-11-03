from example_catalogs import local, remote
from example_catalogs.remote import hello
from ordeq._substitute import _substitutes_modules_to_ios
from ordeq_common import Print

print(_substitutes_modules_to_ios({local: remote, hello: Print()}))
