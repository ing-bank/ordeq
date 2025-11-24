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
		L0@{shape: rounded, label: "Node"}
		L00@{shape: rect, label: "AsyncStaticString"}
		L01@{shape: rect, label: "AsyncStringBuffer"}
		L02@{shape: rect, label: "StringBuffer"}
	end

	IO0 --> example_async.async_ios:process_slow_string
	example_async.async_ios:process_slow_string --> IO1
	IO2 --> example_async.async_ios:process_fast_string
	example_async.async_ios:process_fast_string --> IO3
	IO1 --> example_async.async_ios:combine_results
	IO3 --> example_async.async_ios:combine_results
	example_async.async_ios:combine_results --> IO4

	example_async.async_ios:process_slow_string@{shape: rounded, label: "process_slow_string"}
	example_async.async_ios:process_fast_string@{shape: rounded, label: "process_fast_string"}
	example_async.async_ios:combine_results@{shape: rounded, label: "combine_results"}
	IO1@{shape: rect, label: "slow_result"}
	IO3@{shape: rect, label: "fast_result"}
	IO0@{shape: rect, label: "slow_string_io"}
	IO2@{shape: rect, label: "fast_string_io"}
	IO4@{shape: rect, label: "combined_result"}

	class L0,example_async.async_ios:process_slow_string,example_async.async_ios:process_fast_string,example_async.async_ios:combine_results node
	class L00,IO0,IO2 io0
	class L01,IO3 io1
	class L02,IO1,IO4 io2
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
INFO	ordeq.io	Loading 'slow_string_io' in module 'example_async.async_ios'
DEBUG	ordeq.io	Persisting data for 'slow_string_io' in module 'example_async.async_ios'
INFO	ordeq.runner	Running node 'process_slow_string' in module 'example_async.async_ios'
INFO	ordeq.io	Saving 'slow_result' in module 'example_async.async_ios'
DEBUG	ordeq.io	Persisting data for 'slow_result' in module 'example_async.async_ios'
INFO	ordeq.io	Loading 'fast_string_io' in module 'example_async.async_ios'
DEBUG	ordeq.io	Persisting data for 'fast_string_io' in module 'example_async.async_ios'
INFO	ordeq.runner	Running node 'process_fast_string' in module 'example_async.async_ios'
INFO	ordeq.io	Saving 'fast_result' in module 'example_async.async_ios'
DEBUG	ordeq.io	Persisting data for 'fast_result' in module 'example_async.async_ios'
DEBUG	ordeq.io	Loading cached data for 'slow_result' in module 'example_async.async_ios'
DEBUG	ordeq.io	Loading cached data for 'fast_result' in module 'example_async.async_ios'
INFO	ordeq.runner	Running node 'combine_results' in module 'example_async.async_ios'
INFO	ordeq.io	Saving 'combined_result' in module 'example_async.async_ios'
DEBUG	ordeq.io	Persisting data for 'combined_result' in module 'example_async.async_ios'
DEBUG	ordeq.io	Unpersisting data for 'fast_string_io' in module 'example_async.async_ios'
DEBUG	ordeq.io	Unpersisting data for 'fast_result' in module 'example_async.async_ios'
DEBUG	ordeq.io	Unpersisting data for 'slow_string_io' in module 'example_async.async_ios'
DEBUG	ordeq.io	Unpersisting data for 'slow_result' in module 'example_async.async_ios'
DEBUG	ordeq.io	Unpersisting data for 'combined_result' in module 'example_async.async_ios'
INFO	ordeq.io	Loading 'combined_result' in module 'example_async.async_ios'

```