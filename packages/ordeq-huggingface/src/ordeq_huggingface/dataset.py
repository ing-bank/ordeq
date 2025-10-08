from dataclasses import dataclass

from datasets import (
    Dataset,
    DatasetDict,
    IterableDataset,
    IterableDatasetDict,
    load_dataset,
)
from ordeq import Input


@dataclass(kw_only=True, frozen=True)
class HuggingfaceDataset(
    Input[Dataset | DatasetDict | IterableDatasetDict | IterableDataset]
):
    """Load a dataset from the Huggingface datasets library.

    Example usage:

    ```pycon
    >>> from ordeq_huggingface import HuggingfaceDataset
    >>> ds = HuggingfaceDataset(path="imdb")
    >>> data = ds.load(split="train[:10%]")  # doctest: +SKIP
    >>> len(data)  # doctest: +SKIP

    ```
    """

    path: str

    def load(
        self, **load_args
    ) -> Dataset | DatasetDict | IterableDatasetDict | IterableDataset:
        return load_dataset(self.path, **load_args)
