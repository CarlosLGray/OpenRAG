"""
Author: Carlos L. Gray
Date: August 2024

Description:
This script is designed to query a Chroma database for relevant documents based on a provided search query. 
It utilizes the `HuggingFaceEmbeddings` model to convert the query into embeddings, which are then used 
to search for similar documents within the Chroma database. The results are displayed in the console, 
including the content and metadata of the matching documents.

Usage:
Run the script from the command line with a query as an argument. For example:
    python query.py "What was my sprint mobile phone bill for February 2018?"

The script will return and display up to 10 documents that match the query based on their similarity 
to the embedded query vector.

Dependencies:
- langchain_huggingface: Provides the HuggingFaceEmbeddings class for converting text into embeddings.
- langchain_chroma: Integrates the Chroma vector store for efficient document retrieval.
- Python 3.x
"""

import sys
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

# Initialize the embeddings and Chroma database
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
chroma_document_store = Chroma(
    embedding_function=embeddings,
    persist_directory="./chroma_db"  # Ensure this matches the directory used in indexing
)

def query_chroma_db(query, k=10):
    """Query the Chroma DB and print the results."""
    print(f"Querying Chroma DB with: {query}")
    
    # Embed the query
    query_embedding = embeddings.embed_query(query)
    
    # Perform the similarity search
    docs = chroma_document_store.similarity_search(query, k=k)
    
    if docs:
        print(f"Found {len(docs)} documents:")
        for i, doc in enumerate(docs, 1):
            print(f"\nDocument {i}:")
            print(f"Content: {doc.page_content[:500]}...")  # Display first 500 characters of content
            print(f"Metadata: {doc.metadata}")
    else:
        print("No documents found for the query.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a query as a command-line argument.")
        sys.exit(1)
    
    query = sys.argv[1]
    query_chroma_db(query, k=5)
