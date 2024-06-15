import spacy
import string
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
            cls._initialize(cls._instance)
        return cls._instance

    def _initialize(self):
        self.tokenizer = word_tokenize
        self.stopwords = set(stopwords.words("russian"))
        self.punctuation = set(string.punctuation)
        self.stemmer = SnowballStemmer("russian")
        self.nlp = spacy.load("ru_core_news_sm")

    def tokenize_text(self, text: str, language: str) -> list[str]:
        return self.tokenizer(text, language=language)

    def delete_stopwords_and_punctuation(self, words: list[str]) -> list[str]:
        return [
            word
            for word in words
            if word not in self.stopwords and word not in self.punctuation
        ]

    def stemming_words(self, words: list[str]) -> list[str]:
        return [self.stemmer.stem(word) for word in words]

    def lemmatize_words(self, words: list[str]) -> list[str]:
        return [self.nlp(token)[0].lemma_ for token in words]

    def process_text(self, text: str) -> list[str]:
        tokens = self.tokenize_text(text, "russian")
        tokens = self.delete_stopwords_and_punctuation(tokens)
        tokens = self.lemmatize_words(tokens)
        return tokens
