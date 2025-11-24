## Resource

```python
from ordeq._fqn import FQN

fqn = FQN("package.module", "MyClass")
print(format(fqn, "ref"))
print(format(fqn, "desc"))
print(format(fqn))

```

## Output

```text
package.module:MyClass
'MyClass' in module 'package.module'
'MyClass' in module 'package.module'

```