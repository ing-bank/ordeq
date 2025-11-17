## Resource

```python
from ordeq import Output

io_empty_attrs = Output[str]().with_attributes()
io_with_attrs = Output[str]().with_attributes(hello="world", foo="bar")
io_with_attrs_twice = io_with_attrs.with_attributes(new_attr=123)
print(io_empty_attrs._attributes)
print(io_with_attrs._attributes)
print(io_with_attrs_twice._attributes)

```

## Output

```text
{}
{'hello': 'world', 'foo': 'bar'}
{'new_attr': 123}

```