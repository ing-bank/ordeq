packages/ordeq/tests/resources/views/node_outputs_view.py:9: error: No overload variant of "node" matches argument type "Callable[[], str]"  [call-overload]
packages/ordeq/tests/resources/views/node_outputs_view.py:9: note: Possible overload variants:
packages/ordeq/tests/resources/views/node_outputs_view.py:9: note:     def [FuncParams`-1, FuncReturns] node(func: Callable[FuncParams, FuncReturns], *, inputs: Sequence[Input[Any] | Callable[..., Any]] | Input[Any] | Callable[..., Any] | None = ..., outputs: Sequence[Output[Any]] | Output[Any] | None = ..., **attributes: Any) -> Callable[FuncParams, FuncReturns]
packages/ordeq/tests/resources/views/node_outputs_view.py:9: note:     def node(*, inputs: Sequence[Input[Any] | Callable[..., Any]] | Input[Any] | Callable[..., Any] = ..., outputs: Sequence[Output[Any]] | Output[Any] | None = ..., **attributes: Any) -> Callable[[Callable[FuncParams, FuncReturns]], Callable[FuncParams, FuncReturns]]
packages/ordeq/tests/resources/views/node_outputs_regular_func.py:8: error: No overload variant of "node" matches argument type "Callable[[], str]"  [call-overload]
packages/ordeq/tests/resources/views/node_outputs_regular_func.py:8: note: Possible overload variants:
packages/ordeq/tests/resources/views/node_outputs_regular_func.py:8: note:     def [FuncParams`-1, FuncReturns] node(func: Callable[FuncParams, FuncReturns], *, inputs: Sequence[Input[Any] | Callable[..., Any]] | Input[Any] | Callable[..., Any] | None = ..., outputs: Sequence[Output[Any]] | Output[Any] | None = ..., **attributes: Any) -> Callable[FuncParams, FuncReturns]
packages/ordeq/tests/resources/views/node_outputs_regular_func.py:8: note:     def node(*, inputs: Sequence[Input[Any] | Callable[..., Any]] | Input[Any] | Callable[..., Any] = ..., outputs: Sequence[Output[Any]] | Output[Any] | None = ..., **attributes: Any) -> Callable[[Callable[FuncParams, FuncReturns]], Callable[FuncParams, FuncReturns]]
packages/ordeq/tests/resources/runner/runner_load_output.py:17: error: List item 0 has incompatible type "Example"; expected "Input[Any] | Callable[..., Any]"  [list-item]
packages/ordeq/tests/resources/runner/run_non_runnable.py:3: error: Argument 1 to "run" has incompatible type "float"; expected Module | Callable[..., Any] | str  [arg-type]
packages/ordeq/tests/resources/runner/run_main.py:5: error: Need type annotation for "io1"  [var-annotated]
packages/ordeq/tests/resources/runner/run_main.py:6: error: Need type annotation for "io2"  [var-annotated]
packages/ordeq/tests/resources/nodes/node_none_standalone.py:4: error: No overload variant of "node" matches argument type "None"  [call-overload]
packages/ordeq/tests/resources/nodes/node_none_standalone.py:4: note: Possible overload variants:
packages/ordeq/tests/resources/nodes/node_none_standalone.py:4: note:     def [FuncParams`-1, FuncReturns] node(func: Callable[FuncParams, FuncReturns], *, inputs: Sequence[Input[Any] | Callable[..., Any]] | Input[Any] | Callable[..., Any] | None = ..., outputs: Sequence[Output[Any]] | Output[Any] | None = ..., **attributes: Any) -> Callable[FuncParams, FuncReturns]
packages/ordeq/tests/resources/nodes/node_none_standalone.py:4: note:     def node(*, inputs: Sequence[Input[Any] | Callable[..., Any]] | Input[Any] | Callable[..., Any] = ..., outputs: Sequence[Output[Any]] | Output[Any] | None = ..., **attributes: Any) -> Callable[[Callable[FuncParams, FuncReturns]], Callable[FuncParams, FuncReturns]]
packages/ordeq/tests/resources/nodes/node_none.py:5: error: No overload variant of "node" matches argument type "None"  [call-overload]
packages/ordeq/tests/resources/nodes/node_none.py:5: note: Possible overload variants:
packages/ordeq/tests/resources/nodes/node_none.py:5: note:     def [FuncParams`-1, FuncReturns] node(func: Callable[FuncParams, FuncReturns], *, inputs: Sequence[Input[Any] | Callable[..., Any]] | Input[Any] | Callable[..., Any] | None = ..., outputs: Sequence[Output[Any]] | Output[Any] | None = ..., **attributes: Any) -> Callable[FuncParams, FuncReturns]
packages/ordeq/tests/resources/nodes/node_none.py:5: note:     def node(*, inputs: Sequence[Input[Any] | Callable[..., Any]] | Input[Any] | Callable[..., Any] = ..., outputs: Sequence[Output[Any]] | Output[Any] | None = ..., **attributes: Any) -> Callable[[Callable[FuncParams, FuncReturns]], Callable[FuncParams, FuncReturns]]
packages/ordeq/tests/resources/nodes/node_float_standalone.py:4: error: No overload variant of "node" matches argument type "float"  [call-overload]
packages/ordeq/tests/resources/nodes/node_float_standalone.py:4: note: Possible overload variants:
packages/ordeq/tests/resources/nodes/node_float_standalone.py:4: note:     def [FuncParams`-1, FuncReturns] node(func: Callable[FuncParams, FuncReturns], *, inputs: Sequence[Input[Any] | Callable[..., Any]] | Input[Any] | Callable[..., Any] | None = ..., outputs: Sequence[Output[Any]] | Output[Any] | None = ..., **attributes: Any) -> Callable[FuncParams, FuncReturns]
packages/ordeq/tests/resources/nodes/node_float_standalone.py:4: note:     def node(*, inputs: Sequence[Input[Any] | Callable[..., Any]] | Input[Any] | Callable[..., Any] = ..., outputs: Sequence[Output[Any]] | Output[Any] | None = ..., **attributes: Any) -> Callable[[Callable[FuncParams, FuncReturns]], Callable[FuncParams, FuncReturns]]
packages/ordeq/tests/resources/nodes/node_float.py:5: error: No overload variant of "node" matches argument type "float"  [call-overload]
packages/ordeq/tests/resources/nodes/node_float.py:5: note: Possible overload variants:
packages/ordeq/tests/resources/nodes/node_float.py:5: note:     def [FuncParams`-1, FuncReturns] node(func: Callable[FuncParams, FuncReturns], *, inputs: Sequence[Input[Any] | Callable[..., Any]] | Input[Any] | Callable[..., Any] | None = ..., outputs: Sequence[Output[Any]] | Output[Any] | None = ..., **attributes: Any) -> Callable[FuncParams, FuncReturns]
packages/ordeq/tests/resources/nodes/node_float.py:5: note:     def node(*, inputs: Sequence[Input[Any] | Callable[..., Any]] | Input[Any] | Callable[..., Any] = ..., outputs: Sequence[Output[Any]] | Output[Any] | None = ..., **attributes: Any) -> Callable[[Callable[FuncParams, FuncReturns]], Callable[FuncParams, FuncReturns]]
packages/ordeq/tests/resources/io/save_with_kwarg_data.py:5: note: "save" of "Example" defined here
packages/ordeq/tests/resources/io/save_with_kwarg_data.py:13: error: Unexpected keyword argument "data" for "save" of "Example"  [call-arg]
packages/ordeq/tests/resources/io/io_mixed_types_overloaded_save_options.py:46: error: No overload variant of "save" of "Text" matches argument types "bytes", "str"  [call-overload]
packages/ordeq/tests/resources/io/io_mixed_types_overloaded_save_options.py:46: note: Possible overload variants:
packages/ordeq/tests/resources/io/io_mixed_types_overloaded_save_options.py:46: note:     def save(self, data: str, encoding: str | None = ...) -> None
packages/ordeq/tests/resources/io/io_mixed_types_overloaded_save_options.py:46: note:     def save(self, data: bytes, encoding: None = ...) -> None
packages/ordeq/tests/resources/io/io_mixed_types_overloaded_save.py:46: error: No overload variant of "save" of "Text" matches argument types "bytes", "str"  [call-overload]
packages/ordeq/tests/resources/io/io_mixed_types_overloaded_save.py:46: note: Possible overload variants:
packages/ordeq/tests/resources/io/io_mixed_types_overloaded_save.py:46: note:     def save(self, data: str) -> Any
packages/ordeq/tests/resources/io/io_mixed_types_overloaded_save.py:46: note:     def save(self, data: bytes) -> Any
packages/ordeq/tests/resources/hooks/invalid_typed_output_hook.py:5: error: Argument 1 of "before_output_save" is incompatible with supertype "ordeq._hook.OutputHook"; supertype defines the argument type as "Output[str]"  [override]
packages/ordeq/tests/resources/hooks/invalid_typed_output_hook.py:5: note: This violates the Liskov substitution principle
packages/ordeq/tests/resources/hooks/invalid_typed_output_hook.py:5: note: See https://mypy.readthedocs.io/en/stable/common_issues.html#incompatible-overrides
packages/ordeq/tests/resources/hooks/invalid_typed_output_hook.py:5: error: Argument 2 of "before_output_save" is incompatible with supertype "ordeq._hook.OutputHook"; supertype defines the argument type as "str"  [override]
packages/ordeq/tests/resources/hooks/invalid_typed_output_hook.py:6: error: If x = b'abc' then f"{x}" or "{}".format(x) produces "b'abc'", not "abc". If this is desired behavior, use f"{x!r}" or "{!r}".format(x). Otherwise, decode the bytes  [str-bytes-safe]
packages/ordeq/tests/resources/catalog/static.py:17: error: Name "catalog" already defined on line 6  [no-redef]
packages/ordeq/tests/resources/views/view_takes_node_output.py:4: error: Need type annotation for "placeholder"  [var-annotated]
packages/ordeq/tests/resources/substitute/substitute_ios_with_ios.py:6: error: Need type annotation for "b"  [var-annotated]
packages/ordeq/tests/resources/substitute/substitute_ios_with_ios.py:8: error: Need type annotation for "B"  [var-annotated]
packages/ordeq/tests/resources/runner/logging_verbosity.py:17: error: Argument 1 to "from_nodes" of "NodeGraph" has incompatible type "set[Node[Any, Any]]"; expected "Sequence[Node[Any, Any]]"  [arg-type]
packages/ordeq/tests/resources/runner/graph.py:35: error: Argument 1 to "run" has incompatible type "*list[function]"; expected Module | Callable[..., Any] | str  [arg-type]
packages/ordeq/tests/resources/runner/graph.py:38: error: Argument 1 to "run" has incompatible type "*list[function]"; expected Module | Callable[..., Any] | str  [arg-type]
packages/ordeq/tests/resources/runner/graph.py:41: error: Argument 1 to "run" has incompatible type "*list[function]"; expected Module | Callable[..., Any] | str  [arg-type]
packages/ordeq/tests/resources/nodes/node_unexpected_output_type.py:7: error: No overload variant of "node" matches argument types "Literal[str]", "Literal[str]"  [call-overload]
packages/ordeq/tests/resources/nodes/node_unexpected_output_type.py:7: note: Possible overload variants:
packages/ordeq/tests/resources/nodes/node_unexpected_output_type.py:7: note:     def [FuncParams`-1, FuncReturns] node(func: Callable[FuncParams, FuncReturns], *, inputs: Sequence[Input[Any] | Callable[..., Any]] | Input[Any] | Callable[..., Any] | None = ..., outputs: Sequence[Output[Any]] | Output[Any] | None = ..., **attributes: Any) -> Callable[FuncParams, FuncReturns]
packages/ordeq/tests/resources/nodes/node_unexpected_output_type.py:7: note:     def node(*, inputs: Sequence[Input[Any] | Callable[..., Any]] | Input[Any] | Callable[..., Any] = ..., outputs: Sequence[Output[Any]] | Output[Any] | None = ..., **attributes: Any) -> Callable[[Callable[FuncParams, FuncReturns]], Callable[FuncParams, FuncReturns]]
packages/ordeq/tests/resources/views/standalone_view_df_filter.py:18: error: No overload variant of "where" of "DataFrame" matches argument type "str"  [call-overload]
packages/ordeq/tests/resources/views/standalone_view_df_filter.py:18: note: Possible overload variants:
packages/ordeq/tests/resources/views/standalone_view_df_filter.py:18: note:     def where(self, cond: Series[Any] | DataFrame | ndarray[tuple[Any, ...], dtype[Any]] | Callable[[DataFrame], DataFrame] | Callable[[Any], bool], other: Any = ..., *, inplace: Literal[True], axis: Literal['index', 0] | Literal['columns', 1] | None = ..., level: Hashable | None = ...) -> None
packages/ordeq/tests/resources/views/standalone_view_df_filter.py:18: note:     def where(self, cond: Series[Any] | DataFrame | ndarray[tuple[Any, ...], dtype[Any]] | Callable[[DataFrame], DataFrame] | Callable[[Any], bool], other: Any = ..., *, inplace: Literal[False] = ..., axis: Literal['index', 0, 'columns', 1] | None = ..., level: Hashable | None = ...) -> DataFrame
Found 26 errors in 20 files (checked 262 source files)
