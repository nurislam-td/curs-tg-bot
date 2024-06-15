from abc import ABC, abstractmethod


class Tokenizer(ABC):
    @abstractmethod
    def process_text(self, text: str) -> list[str]: ...
