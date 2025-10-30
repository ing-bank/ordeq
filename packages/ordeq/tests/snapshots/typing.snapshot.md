packages/ordeq/tests/resources/resolve/resolve_module_example_catalog.py:1: error: Skipping analyzing "example_1": module is installed, but missing library stubs or py.typed marker  [import-untyped]
packages/ordeq/tests/resources/resolve/resolve_module_example_catalog.py:1: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
packages/ordeq/tests/resources/views/view_inputs_none.py:5: error: No overload variant of "node" matches argument type "None"  [call-overload]
packages/ordeq/tests/resources/views/view_inputs_none.py:5: note: Possible overload variants:
packages/ordeq/tests/resources/views/view_inputs_none.py:5: note:     def [FuncParams`-1, FuncReturns] node(func: Callable[FuncParams, FuncReturns], *, inputs: Sequence[Input[Any] | Callable[..., Any]] | Input[Any] | Callable[..., Any] | None = ..., outputs: Sequence[Output[Any]] | Output[Any] | None = ..., **attributes: Any) -> Callable[FuncParams, FuncReturns]
packages/ordeq/tests/resources/views/view_inputs_none.py:5: note:     def node(*, inputs: Sequence[Input[Any] | Callable[..., Any]] | Input[Any] | Callable[..., Any] | None = ..., outputs: Sequence[Output[Any]] | Output[Any] | None = ..., **attributes: Any) -> Callable[[Callable[FuncParams, FuncReturns]], Callable[FuncParams, FuncReturns]]
packages/ordeq/tests/resources/views/node_outputs_view.py:9: error: No overload variant of "node" matches argument type "Callable[[], str]"  [call-overload]
packages/ordeq/tests/resources/views/node_outputs_view.py:9: note: Possible overload variants:
packages/ordeq/tests/resources/views/node_outputs_view.py:9: note:     def [FuncParams`-1, FuncReturns] node(func: Callable[FuncParams, FuncReturns], *, inputs: Sequence[Input[Any] | Callable[..., Any]] | Input[Any] | Callable[..., Any] | None = ..., outputs: Sequence[Output[Any]] | Output[Any] | None = ..., **attributes: Any) -> Callable[FuncParams, FuncReturns]
packages/ordeq/tests/resources/views/node_outputs_view.py:9: note:     def node(*, inputs: Sequence[Input[Any] | Callable[..., Any]] | Input[Any] | Callable[..., Any] | None = ..., outputs: Sequence[Output[Any]] | Output[Any] | None = ..., **attributes: Any) -> Callable[[Callable[FuncParams, FuncReturns]], Callable[FuncParams, FuncReturns]]
packages/ordeq/tests/resources/views/node_outputs_regular_func.py:8: error: No overload variant of "node" matches argument type "Callable[[], str]"  [call-overload]
packages/ordeq/tests/resources/views/node_outputs_regular_func.py:8: note: Possible overload variants:
packages/ordeq/tests/resources/views/node_outputs_regular_func.py:8: note:     def [FuncParams`-1, FuncReturns] node(func: Callable[FuncParams, FuncReturns], *, inputs: Sequence[Input[Any] | Callable[..., Any]] | Input[Any] | Callable[..., Any] | None = ..., outputs: Sequence[Output[Any]] | Output[Any] | None = ..., **attributes: Any) -> Callable[FuncParams, FuncReturns]
packages/ordeq/tests/resources/views/node_outputs_regular_func.py:8: note:     def node(*, inputs: Sequence[Input[Any] | Callable[..., Any]] | Input[Any] | Callable[..., Any] | None = ..., outputs: Sequence[Output[Any]] | Output[Any] | None = ..., **attributes: Any) -> Callable[[Callable[FuncParams, FuncReturns]], Callable[FuncParams, FuncReturns]]
packages/ordeq/tests/resources/runner/runner_load_output.py:17: error: List item 0 has incompatible type "Example"; expected "Input[Any] | Callable[..., Any]"  [list-item]
packages/ordeq/tests/resources/runner/run_non_runnable.py:3: error: Argument 1 to "run" has incompatible type "float"; expected Module | Callable[..., Any] | str  [arg-type]
packages/ordeq/tests/resources/runner/deterministic_graph.py:5: error: Need type annotation for "o1"  [var-annotated]
packages/ordeq/tests/resources/runner/deterministic_graph.py:6: error: Need type annotation for "o2"  [var-annotated]
packages/ordeq/tests/resources/runner/deterministic_graph.py:7: error: Need type annotation for "o3"  [var-annotated]
packages/ordeq/tests/resources/runner/deterministic_graph.py:8: error: Need type annotation for "o4"  [var-annotated]
packages/ordeq/tests/resources/runner/deterministic_graph.py:41: error: Argument 1 to "run" has incompatible type "*set[function]"; expected Module | Callable[..., Any] | str  [arg-type]
packages/ordeq/tests/resources/io/save_with_kwarg_data.py:5: note: "save" of "Example" defined here
packages/ordeq/tests/resources/io/save_with_kwarg_data.py:13: error: Unexpected keyword argument "data" for "save" of "Example"  [call-arg]
packages/ordeq/tests/resources/hooks/invalid_typed_output_hook.py:5: error: Argument 1 of "before_output_save" is incompatible with supertype "ordeq._hook.OutputHook"; supertype defines the argument type as "Output[str]"  [override]
packages/ordeq/tests/resources/hooks/invalid_typed_output_hook.py:5: note: This violates the Liskov substitution principle
packages/ordeq/tests/resources/hooks/invalid_typed_output_hook.py:5: note: See https://mypy.readthedocs.io/en/stable/common_issues.html#incompatible-overrides
packages/ordeq/tests/resources/hooks/invalid_typed_output_hook.py:5: error: Argument 2 of "before_output_save" is incompatible with supertype "ordeq._hook.OutputHook"; supertype defines the argument type as "str"  [override]
packages/ordeq/tests/resources/hooks/invalid_typed_output_hook.py:6: error: If x = b'abc' then f"{x}" or "{}".format(x) produces "b'abc'", not "abc". If this is desired behavior, use f"{x!r}" or "{!r}".format(x). Otherwise, decode the bytes  [str-bytes-safe]
packages/ordeq/tests/resources/views/view_takes_node_output.py:4: error: Need type annotation for "placeholder"  [var-annotated]
packages/ordeq/tests/resources/views/view_patch_io.py:17: error: Argument "io" to "run" has incompatible type "dict[Literal[str], Literal[str]]"; expected "dict[Input[Never] | Output[Never], Input[Never] | Output[Never]] | None"  [arg-type]
packages/ordeq/tests/resources/views/view_index_run_result_by_node.py:16: error: "run" does not return a value (it only ever returns None)  [func-returns-value]
packages/ordeq/tests/resources/runner/runner_io_more_than_once.py:26: error: Argument "io" to "run" has incompatible type "dict[Literal[int], Literal[int]]"; expected "dict[Input[Never] | Output[Never], Input[Never] | Output[Never]] | None"  [arg-type]
packages/ordeq/tests/resources/runner/runner_io.py:29: error: Argument "io" to "run" has incompatible type "dict[object, object]"; expected "dict[Input[Never] | Output[Never], Input[Never] | Output[Never]] | None"  [arg-type]
packages/ordeq/tests/resources/runner/runner_exhausted_stream.py:19: error: Unsupported left operand type for + ("Iterable[str]")  [operator]
packages/ordeq/tests/resources/runner/graph.py:35: error: Argument 1 to "run" has incompatible type "*set[function]"; expected Module | Callable[..., Any] | str  [arg-type]
packages/ordeq/tests/resources/runner/graph.py:38: error: Argument 1 to "run" has incompatible type "*set[function]"; expected Module | Callable[..., Any] | str  [arg-type]
packages/ordeq/tests/resources/runner/graph.py:41: error: Argument 1 to "run" has incompatible type "*set[function]"; expected Module | Callable[..., Any] | str  [arg-type]
packages/ordeq/tests/resources/nodes/node_unexpected_output_type.py:7: error: No overload variant of "node" matches argument types "Literal[str]", "Literal[str]"  [call-overload]
packages/ordeq/tests/resources/nodes/node_unexpected_output_type.py:7: note: Possible overload variants:
packages/ordeq/tests/resources/nodes/node_unexpected_output_type.py:7: note:     def [FuncParams`-1, FuncReturns] node(func: Callable[FuncParams, FuncReturns], *, inputs: Sequence[Input[Any] | Callable[..., Any]] | Input[Any] | Callable[..., Any] | None = ..., outputs: Sequence[Output[Any]] | Output[Any] | None = ..., **attributes: Any) -> Callable[FuncParams, FuncReturns]
packages/ordeq/tests/resources/nodes/node_unexpected_output_type.py:7: note:     def node(*, inputs: Sequence[Input[Any] | Callable[..., Any]] | Input[Any] | Callable[..., Any] | None = ..., outputs: Sequence[Output[Any]] | Output[Any] | None = ..., **attributes: Any) -> Callable[[Callable[FuncParams, FuncReturns]], Callable[FuncParams, FuncReturns]]
packages/ordeq/tests/resources/catalog/static.py:18: error: Name "catalog" already defined on line 7  [no-redef]
packages/ordeq/tests/resources/catalog/run_with_module_catalog.py:22: error: Argument "io" to "run" has incompatible type Module; expected "dict[Input[Never] | Output[Never], Input[Never] | Output[Never]] | None"  [arg-type]
packages/ordeq/tests/resources/catalog/inconsistent_without_check.py:8: error: Module has no attribute "result"  [attr-defined]
packages/ordeq/tests/resources/catalog/inconsistent_with_check.py:10: error: Module has no attribute "result"  [attr-defined]
packages/ordeq/tests/resources/catalog/catalogs/remote_overridden.py:7: error: Name "hello" already defined (possibly by an import)  [no-redef]
packages/ordeq/tests/resources/views/standalone_view_df_filter.py:18: error: No overload variant of "where" of "DataFrame" matches argument type "str"  [call-overload]
packages/ordeq/tests/resources/views/standalone_view_df_filter.py:18: note: Possible overload variants:
packages/ordeq/tests/resources/views/standalone_view_df_filter.py:18: note:     def where(self, cond: Series[Any] | DataFrame | ndarray[tuple[Any, ...], dtype[Any]] | Callable[[DataFrame], DataFrame] | Callable[[Any], bool], other: Any = ..., *, inplace: Literal[True], axis: Literal['index', 0] | Literal['columns', 1] | None = ..., level: Hashable | None = ...) -> None
packages/ordeq/tests/resources/views/standalone_view_df_filter.py:18: note:     def where(self, cond: Series[Any] | DataFrame | ndarray[tuple[Any, ...], dtype[Any]] | Callable[[DataFrame], DataFrame] | Callable[[Any], bool], other: Any = ..., *, inplace: Literal[False] = ..., axis: Literal['index', 0, 'columns', 1] | None = ..., level: Hashable | None = ...) -> DataFrame
Found 31 errors in 23 files (checked 141 source files)
