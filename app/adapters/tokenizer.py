from app.services.abstract.tokenizer import Tokenizer
from nltk import word_tokenize, SnowballStemmer
from nltk.corpus import stopwords

# nltk.download("punkt")
# nltk.download("stopwords")


class NLTKTokenizer(Tokenizer):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.tokenizer = word_tokenize
        self.stopwords = set(stopwords.words("russian"))
        self.stemmer = SnowballStemmer("russian")

    def tokenize_text(self, text: str) -> list[str]:
        return self.tokenizer(text)

    def delete_stopwords(self, words: list[str]) -> list[str]:
        return [word for word in words if word not in self.stopwords]

    def stemming_words(self, words: list[str]) -> list[str]:
        return [self.stemmer.stem(word) for word in words]

    def process_text(self, text: str) -> list[str]:
        tokens = self.tokenize_text(text)
        tokens = self.delete_stopwords(tokens)
        tokens = self.stemming_words(tokens)
        return tokens
