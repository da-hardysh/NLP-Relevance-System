## About the Project

This system automates the process of **evaluating the relevance of learning materials to test questions**. It's designed to solve the problem of misalignment between educational content and assessment items, providing an **objective and rapid verification** of their correspondence.

Built with an object-oriented approach, the system leverages **modern Natural Language Processing (NLP) and semantic matching techniques** for text data analysis. This ensures **modularity, flexibility, and scalability** for various educational platforms and subject areas.

---

## Functionality

The system sequentially performs several key stages of processing and analysis:

* **Text Preprocessing:** Cleans, tokenizes, and lemmatizes raw text, preparing it for deeper analysis.
* **Keyword Extraction:** Identifies the most important terms and phrases using algorithms like TF-IDF and KeyBERT.
* **Named Entity Recognition (NER):** Detects and classifies named entities within the text.
* **Semantic Similarity Computation:** Assesses the conceptual closeness between learning materials and test questions using methods such as cosine similarity and Jaccard similarity.
* **Data Management:** Handles database interactions to fetch and store learning materials, test questions, and evaluation results.
* **Report Generation:** Creates detailed reports on the relevance assessment outcomes.

---
