import math

def euclidian_distance(doc1, doc2):
    token1 = tokenize_docs(doc1)
    token2 = tokenize_docs(doc2)
    
    vocabulary = create_vocab(token1, token2)
    
    vec1 = create_vectors(token1, vocabulary)
    vec2 = create_vectors(token2, vocabulary)
    
    actual_distance = math.sqrt(sum((v1 - v2) ** 2 for v1, v2 in zip(vec1, vec2)))
    
    max_distance = math.sqrt(len(vocabulary))
    
    dissimilarity_percentage = (actual_distance / max_distance) * 100
    similarity = (100 - dissimilarity_percentage)
    return similarity, dissimilarity_percentage
    
def tokenize_docs(docs):
    return docs.lower().split() 

def create_vocab(doc1, doc2):
    return set(doc1).union(set(doc2))
    
def create_vectors(tokens, vocab):
    return [tokens.count(word) for word in vocab]


doc_u = "This is a catterpillar"
doc_v = "This is a cat"


similarity, dissimilarity = euclidian_distance(doc_u, doc_v)
print(similarity, dissimilarity)