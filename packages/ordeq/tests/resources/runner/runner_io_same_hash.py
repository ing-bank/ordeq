from example_duplicates import duplicate_io_same_hash
from example_duplicates.duplicate_io_same_hash import MyIO, hello, result
from ordeq import run

sub = MyIO(
    value="sub", attr=result.attr
)  # has the same hash as `result` and `hello`
assert hash(sub) == hash(result)
assert hash(sub) == hash(hello)

print("Should print 'Saying hello (attr = 0)'")
run(duplicate_io_same_hash, io={result: sub})

print("Should print 'Saying hello (attr = 0)'")
run(duplicate_io_same_hash, io={sub: hello})

print("Should print 'Saying sub (attr = 0)'")
run(duplicate_io_same_hash, io={hello: sub})
