from dataclasses import dataclass

import sentence_transformers as st
from ordeq import Input


@dataclass(frozen=True)
class SentenceTransformer(Input[st.SentenceTransformer]):
    """Input for a SentenceTransformer model from the `sentence-transformers`
    library.

    Example:

    ```pycon
    >>> from ordeq_sentence_transformers import SentenceTransformer
    >>> huggingface_token = "your_hf_token_here"
    >>> model = SentenceTransformer(
    ...     'all-mpnet-base-v2'
    ... ).with_load_options(
    ...     token=huggingface_token
    ... )
    >>> st_model = model.load()  # doctest: +SKIP

    ```

    For more details, see [the `sentence-transformers` documentation][st-docs].

    [st-docs]: https://www.sbert.net/docs/quickstart.html

    """

    model: str

    def load(self, **load_kwargs) -> st.SentenceTransformer:
        return st.SentenceTransformer(self.model, **load_kwargs)
