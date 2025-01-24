import math
from collections import Counter

def tokenize(text):
    """Tokenizes text into words."""
    return text.lower().split()

def compute_tf(doc):
    """Computes term frequency for a document."""
    tf = Counter(doc)
    total_terms = len(doc)
    return {word: count / total_terms for word, count in tf.items()}

def compute_idf(documents):
    """Computes inverse document frequency."""
    import math
    num_docs = len(documents)
    idf = {}
    all_tokens = set(token for doc in documents for token in doc)
    print("What's all the tokens", all_tokens)
    for token in all_tokens:
        containing_docs = sum(1 for doc in documents if token in doc)
        idf[token] = math.log(num_docs / (1 + containing_docs))
    return idf

def compute_tfidf(doc, idf):
    """Computes TF-IDF for a single document."""
    tf = compute_tf(doc)
    return {word: tf[word] * idf.get(word, 0) for word in tf}

def dot_product(vec1, vec2):
    """Computes the dot product between two vectors."""
    return sum(vec1.get(key, 0) * vec2.get(key, 0) for key in set(vec1) | set(vec2))

def magnitude(vec):
    """Computes the magnitude of a vector."""
    return math.sqrt(sum(val ** 2 for val in vec.values()))

def cosine_similarity(vec1, vec2):
    """Computes cosine similarity between two vectors."""
    numerator = dot_product(vec1, vec2)
    denominator = magnitude(vec1) * magnitude(vec2)
    return numerator / denominator if denominator else 0.0

# Sample documents
documents = [
    "The cat sat on the mat.",
    "The dog barked at the mailman.",
    "The cat lay down on the mat."
]

# Tokenize documents
tokenized_docs = [tokenize(doc) for doc in documents]

# Compute IDF
idf = compute_idf(tokenized_docs)

# # Compute TF-IDF for each document
tfidf_docs = [compute_tfidf(doc, idf) for doc in tokenized_docs]

# # Compute cosine similarity matrix
# num_docs = len(tfidf_docs)
# cosine_sim_matrix = [[cosine_similarity(tfidf_docs[i], tfidf_docs[j]) for j in range(num_docs)] for i in range(num_docs)]

# # Display the results
# print("Cosine Similarity Matrix:")
# for row in cosine_sim_matrix:
#     print(row)
