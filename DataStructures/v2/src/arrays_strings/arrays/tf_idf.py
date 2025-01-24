
from collections import Counter
import math 
def tokenized(docs):
    return docs.lower().split()

def compute_tf(docs):
    """ 
    TF(t) = Number of times term t appears in d / total number of terms in d
    """
    tf = Counter(docs)
    total_terms = len(docs)
    return {word: count / total_terms for word, count in tf.items()}

def compute_idf(docs):
    """ 
     idf(t) = log((total number of documents) / (number of docs containing t))
    """
    num_docs = len(docs)
    idf = {} 
    vocab = set(token for doc in docs for token in doc)
    for word in vocab:
        containing_doc = sum(1 for doc in docs if word in doc)
        idf[word] = math.log(num_docs / (1 + containing_doc))
    return idf

def compute_tfidf(doc, idf):
    """Computes TF-IDF for a single document.
        tf_idf = tf(t, d) * idf(t)"""
    tf = compute_tf(doc)
    return {word: tf[word] * idf.get(word, 0) for word in tf}
    

def cosine_similarity(vec1, vec2):
    numerator = dot_product(vec1, vec2)
    denominator = magnitude(vec1) * magnitude(vec2)
    return numerator / denominator if denominator else 0.0

def dot_product(vec1, vec2):
    return sum(vec1.get(key, 0) * vec2.get(key, 0) for key in set(vec1) | set(vec2))

def magnitude(vec):
    return math.sqrt(sum(val ** 2 for val in vec.values()))

documents = [
    "The sky is blue",
    "The sun in the sky is bright",
    "The sun is blue"
    
]

# Tokenize the documents 
tokenized_docs = [tokenized(doc) for doc in documents]

# Compute idf 
idf = compute_idf(tokenized_docs)

# Compute tfidf 
tfidf = [compute_tfidf(doc, idf) for doc in tokenized_docs]

# compute cosine similarity 
num_docs = len(tfidf)
cosine_sim_matrix = [[cosine_similarity(tfidf[i], tfidf[j]) for j in range(num_docs)] for i in range(num_docs)]

# Display cosine_sim_matrix 
for row in cosine_sim_matrix:
    print(row)