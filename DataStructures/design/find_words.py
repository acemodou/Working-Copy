"""
books -> {doc1, doc2, doc3}
many  -> {doc1, doc3}
return doc1, doc3
"""

documents = {
    "doc1":  "many books are interesting",
    "doc2":  "books are a source of knowledge", 
    "doc3":  "many people love books "
}

def search_words_in_docs(words):
    words_in_set = {}
    for word in words:
        docs = set()
        for doc_id, content in documents.items():
            if word in content:
                docs.add(doc_id)
        words_in_set[word] = docs 
        print(words_in_set)
    return words_in_set

def find_words_in_docs(words):
    words_in_docs = search_words_in_docs(words)
    common_words_in_all_docs = set.intersection(*words_in_docs.values())
    print(" and ".join(sorted(common_words_in_all_docs)))


search_words = ["books", "many"]
find_words_in_docs(search_words)