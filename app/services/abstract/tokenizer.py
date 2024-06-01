from abc import ABC, abstractmethod


class Tokenizer(ABC):
    @abstractmethod
    def tokenize_word(self, word) -> str: ...
