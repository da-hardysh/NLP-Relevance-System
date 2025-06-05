import re
import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('wordnet')

class TextPreprocessor:
    def __init__(self, text):
        self.text = text.lower()

    def clean_text(self):
        text = re.sub(r'\d+', '', self.text)
        text = text.translate(str.maketrans('', '', string.punctuation))
        return text

    def tokenize(self, text):
        return word_tokenize(text)

    def lemmatize(self, tokens):
        lemmatizer = WordNetLemmatizer()
        return [lemmatizer.lemmatize(token) for token in tokens]

    def process(self):
        cleaned = self.clean_text()
        tokens = self.tokenize(cleaned)
        return self.lemmatize(tokens)
