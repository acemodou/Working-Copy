# Import classes from Libraries
from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI

import os
os.environ["OPENAI_API_KEY"] = ""

def read_pdf(pdf_path):
    data = PdfReader(pdf_path)
    combined_text = ''
    for i, page in enumerate(data.pages):
        text = page.extract_text()
        if text:
            combined_text += text
    return combined_text

def split_text(combined_text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=200,
        chunk_overlap=20,
        length_function=len,
    )
    final_data = text_splitter.split_text(combined_text)
    return final_data

def create_document_search(final_data, embeddings):
    try:
        document_search = FAISS.from_texts(final_data, embeddings)
        return document_search
    except Exception as e:
        # Log the error for debugging
        print(f"Error creating document search: {e}")
        raise  # Re-raise the exception for higher-level handling

def main():
    pdf_path = '/home/mjaw/code/Jupyter/my_award.pdf'
    try:
        combined_text = read_pdf(pdf_path)
        print(combined_text)

        final_data = split_text(combined_text)
        print(len(final_data))

        embeddings = OpenAIEmbeddings()
        chain = load_qa_chain(OpenAI(), chain_type="stuff")

        document_search = create_document_search(final_data, embeddings)

        my_query = "How many awards did Modou won?"
        docs = document_search.similarity_search(my_query)
        chain.run(input_documents=docs, question=my_query)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
