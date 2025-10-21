import os
from dataclasses import dataclass

from datasets import Dataset, DatasetDict, load_from_disk
from ordeq import IO


@dataclass
class HuggingfaceDiskDataset(IO[Dataset | DatasetDict]):
    """Load and save a dataset from/to disk using the Huggingface datasets
    library.

    Example usage:

    ```pycon
    >>> from ordeq_huggingface import HuggingfaceDiskDataset
    >>> ds = HuggingfaceDiskDataset(path="path/to/dataset")  # doctest: +SKIP
    >>> data = ds.load()  # doctest: +SKIP

    ```

    """

    path: str | bytes | os.PathLike

    def load(self, **load_options) -> Dataset | DatasetDict:
        return load_from_disk(self.path, **load_options)

    def save(self, data: Dataset | DatasetDict, **save_options) -> None:
        data.save_to_disk(self.path, **save_options)
