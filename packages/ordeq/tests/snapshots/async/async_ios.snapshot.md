## Resource

```python
from example_async import async_ios
from ordeq import run
from ordeq_viz import viz

print(viz(async_ios, fmt="mermaid"))
print(
    "Expect the 'process_fast_string' node to complete "
    "before 'process_slow_string'"
)
run(async_ios)
print(async_ios.combined_result.load())

```

## Output

```text
graph TB
	subgraph legend["Legend"]
		direction TB
		node_type@{shape: rounded, label: "Node"}
		io_type_0@{shape: rect, label: "AsyncStaticString"}
		io_type_1@{shape: rect, label: "AsyncStringBuffer"}
		io_type_2@{shape: rect, label: "StringBuffer"}
	end

	example_async.async_ios:slow_string_io --> example_async.async_ios:process_slow_string
	example_async.async_ios:process_slow_string --> example_async.async_ios:slow_result
	example_async.async_ios:fast_string_io --> example_async.async_ios:process_fast_string
	example_async.async_ios:process_fast_string --> example_async.async_ios:fast_result
	example_async.async_ios:slow_result --> example_async.async_ios:combine_results
	example_async.async_ios:fast_result --> example_async.async_ios:combine_results
	example_async.async_ios:combine_results --> example_async.async_ios:combined_result

	example_async.async_ios:process_slow_string@{shape: rounded, label: "process_slow_string"}
	example_async.async_ios:process_fast_string@{shape: rounded, label: "process_fast_string"}
	example_async.async_ios:combine_results@{shape: rounded, label: "combine_results"}
	example_async.async_ios:fast_result@{shape: rect, label: "fast_result"}
	example_async.async_ios:slow_result@{shape: rect, label: "slow_result"}
	example_async.async_ios:combined_result@{shape: rect, label: "combined_result"}
	example_async.async_ios:fast_string_io@{shape: rect, label: "fast_string_io"}
	example_async.async_ios:slow_string_io@{shape: rect, label: "slow_string_io"}

	class node_type,example_async.async_ios:process_slow_string,example_async.async_ios:process_fast_string,example_async.async_ios:combine_results node
	class io_type_0,example_async.async_ios:fast_string_io,example_async.async_ios:slow_string_io io0
	class io_type_1,example_async.async_ios:fast_result io1
	class io_type_2,example_async.async_ios:slow_result,example_async.async_ios:combined_result io2
	classDef node fill:#008AD7,color:#FFF
	classDef io fill:#FFD43B
	classDef io0 fill:#66c2a5
	classDef io1 fill:#fc8d62
	classDef io2 fill:#8da0cb

Expect the 'process_fast_string' node to complete before 'process_slow_string'
Combined Results:
Result of slow data: <coroutine object AsyncStaticString.load at HASH1>


```

## Warnings

```text
RuntimeWarning: coroutine 'AsyncStringBuffer.save' was never awaited
RuntimeWarning: coroutine 'AsyncStaticString.load' was never awaited
```

## Logging

```text
INFO	ordeq.io	Loading AsyncStaticString 'slow_string_io' in module 'example_async.async_ios'
DEBUG	ordeq.io	Persisting data for AsyncStaticString 'slow_string_io' in module 'example_async.async_ios'
INFO	ordeq.runner	Running node 'process_slow_string' in module 'example_async.async_ios'
INFO	ordeq.io	Saving StringBuffer 'slow_result' in module 'example_async.async_ios'
DEBUG	ordeq.io	Persisting data for StringBuffer 'slow_result' in module 'example_async.async_ios'
INFO	ordeq.io	Loading AsyncStaticString 'fast_string_io' in module 'example_async.async_ios'
DEBUG	ordeq.io	Persisting data for AsyncStaticString 'fast_string_io' in module 'example_async.async_ios'
INFO	ordeq.runner	Running node 'process_fast_string' in module 'example_async.async_ios'
INFO	ordeq.io	Saving AsyncStringBuffer 'fast_result' in module 'example_async.async_ios'
DEBUG	ordeq.io	Persisting data for AsyncStringBuffer 'fast_result' in module 'example_async.async_ios'
DEBUG	ordeq.io	Loading cached data for StringBuffer 'slow_result' in module 'example_async.async_ios'
DEBUG	ordeq.io	Loading cached data for AsyncStringBuffer 'fast_result' in module 'example_async.async_ios'
INFO	ordeq.runner	Running node 'combine_results' in module 'example_async.async_ios'
INFO	ordeq.io	Saving StringBuffer 'combined_result' in module 'example_async.async_ios'
DEBUG	ordeq.io	Persisting data for StringBuffer 'combined_result' in module 'example_async.async_ios'
DEBUG	ordeq.io	Unpersisting data for AsyncStaticString 'fast_string_io' in module 'example_async.async_ios'
DEBUG	ordeq.io	Unpersisting data for AsyncStringBuffer 'fast_result' in module 'example_async.async_ios'
DEBUG	ordeq.io	Unpersisting data for AsyncStaticString 'slow_string_io' in module 'example_async.async_ios'
DEBUG	ordeq.io	Unpersisting data for StringBuffer 'slow_result' in module 'example_async.async_ios'
DEBUG	ordeq.io	Unpersisting data for StringBuffer 'combined_result' in module 'example_async.async_ios'
INFO	ordeq.io	Loading StringBuffer 'combined_result' in module 'example_async.async_ios'

```