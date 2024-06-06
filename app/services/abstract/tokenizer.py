from abc import ABC, abstractmethod


class Tokenizer(ABC):
    @abstractmethod
    def tokenize_text(self, word) -> str: ...
