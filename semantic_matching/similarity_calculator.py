from sklearn.feature_extraction.text import TfidfVectorizer
from keybert import KeyBERT

class SemanticMatcher:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.kw_model = KeyBERT()

    def extract_keywords_tfidf(self, documents, top_n=10):
        tfidf_matrix = self.vectorizer.fit_transform(documents)
        feature_names = self.vectorizer.get_feature_names_out()
        keywords = []
        for doc_idx in range(tfidf_matrix.shape[0]):
            row = tfidf_matrix[doc_idx].toarray()[0]
            top_indices = row.argsort()[-top_n:][::-1]
            keywords.append([feature_names[i] for i in top_indices])
        return keywords

    def extract_keywords_keybert(self, document, top_n=10):
        return [kw[0] for kw in self.kw_model.extract_keywords(document, top_n=top_n)]

    def compute_overlap(self, terms_a, terms_b):
        set_a = set(terms_a)
        set_b = set(terms_b)
        if not set_a or not set_b:
            return 0.0
        return len(set_a & set_b) / len(set_a)

