"""
Author: Carlos L. Gray
Date: August 2024

Description:
This Python script is designed to interact with a Chroma vector database, utilizing the 
LangChain and HuggingFace libraries to handle embeddings and document retrieval. The script 
performs the following tasks:

1. Initializes the Chroma database with embeddings provided by the HuggingFace model 
   "sentence-transformers/all-MiniLM-L6-v2". The database is set to persist in the directory 
   specified by `persist_directory`.

2. Defines functions to:
   - List all collections in the Chroma database.
   - Retrieve and display documents from a specified collection, including metadata and the 
     first 200 characters of each document's content.

3. The `main` function orchestrates these tasks, first listing all available collections, and 
   then displaying the documents within a specific collection (defaulting to the "langchain" 
   collection).

Usage:
Run this script to explore the contents of a Chroma vector database. Modify the 
`collection_name` variable in the `main` function to target a different collection for 
document retrieval. Ensure that the Chroma database has been populated and that the 
`persist_directory` matches the directory used during indexing.
"""

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

persist_directory = "./chroma_db"  # Specify the directory to persist the Chroma database

# Initialize the embeddings and Chroma database
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
chroma_document_store = Chroma(embedding_function=embeddings, persist_directory=persist_directory)

def list_collections():
    """List all collections in Chroma."""
    collections = chroma_document_store._client.list_collections()
    print("Collections in Chroma:")
    for collection in collections:
        print(f" - {collection}")

def list_documents_in_collection(collection_name):
    """List all documents in a specific collection."""
    collection = chroma_document_store._client.get_or_create_collection(collection_name)
    documents = collection.get(include=["metadatas", "documents"])

    print(f"Total documents retrieved: {len(documents['documents'])}")

    if documents["documents"]:
        print(f"\nDocuments in collection '{collection_name}':")
        for i, (doc, meta) in enumerate(zip(documents["documents"], documents["metadatas"]), 1):
            print(f"Document {i}:")
            print(f"Metadata: {meta}")
            print(f"Content: {doc[:200]}...")  # Display first 200 characters
    else:
        print(f"No documents found in collection '{collection_name}'.")

def main():
    # List all collections
    list_collections()

    # Example: list documents in a specific collection
    collection_name = "langchain"  # Ensure this matches the actual collection name
    list_documents_in_collection(collection_name)

if __name__ == "__main__":
    main()
