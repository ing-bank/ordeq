from typing import Tuple, Optional
from transformers import AutoTokenizer, AutoModel
import torch
from .config import ModelConfig

class ModelLoader:
    """
    Handles lazy loading of the model and tokenizer.
    Not a strict singleton, but designed to be reused.
    """
    def __init__(self, config: ModelConfig):
        self.config = config
        self._tokenizer = None
        self._model = None

    def load(self) -> Tuple[AutoTokenizer, AutoModel]:
        """
        Loads the model and tokenizer if they are not already loaded.
        Returns:
            Tuple[AutoTokenizer, AutoModel]: The loaded tokenizer and model.
        """
        if self._model is None or self._tokenizer is None:
            self._load_resources()
        
        return self._tokenizer, self._model

    def _load_resources(self):
        """Internal method to load resources from Hugging Face."""
        print(f"Loading model: {self.config.model_name}...")
        self._tokenizer = AutoTokenizer.from_pretrained(self.config.model_name)
        self._model = AutoModel.from_pretrained(self.config.model_name)
        
        # Enforce CPU execution
        self._model.to(torch.device("cpu"))
        self._model.eval() # Set to inference mode
