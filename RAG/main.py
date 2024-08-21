"""
Author: Carlos L. Gray
Date: August 2024

Description:
This Flask server application handles POST requests to generate AI-driven responses based on user queries using a retrieval-augmented generation (RAG) approach. The key functionalities of this script include:

1. **Embeddings and Vector Store Initialization**: Utilizes Hugging Face embeddings and the Chroma vector store to store and retrieve documents. The Chroma database is persisted to the specified directory for future use.

2. **Client Class**: Defines a `Client` class to communicate with an AI model server, with the server port specified in a `.env` file. This class sends requests to the AI model and processes the streaming responses.

3. **Endpoint `/generate`**: The server exposes an endpoint `/generate`, which accepts a JSON payload containing a query. It performs a similarity search in the Chroma vector store, retrieves relevant documents, and combines them with the query to generate a response from the AI model.

4. **Cross-Origin Resource Sharing (CORS)**: CORS is enabled using the `Flask-CORS` package to allow requests from different origins, such as a React frontend.

Usage:
- Start the Flask server to listen for POST requests on the `/generate` endpoint.
- Ensure that the `.env` file contains the necessary configuration for the AI model server.
- The server can be integrated with a frontend application (e.g., React) to provide AI-driven responses based on document retrieval.

Dependencies:
- Flask: A lightweight WSGI web application framework for handling HTTP requests.
- Flask-CORS: A Flask extension for handling Cross-Origin Resource Sharing (CORS).
- langchain_chroma: Integrates the Chroma vector store for efficient document retrieval.
- langchain_huggingface: Provides HuggingFaceEmbeddings for text-to-embedding conversion.
- httpx: Handles HTTP requests to the AI model server.
- python-dotenv: Loads environment variables from a `.env` file.
- Python 3.x

"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import httpx
import json
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

# Load environment variables from .env file
load_dotenv()

llm_port = os.getenv('LLM_PORT', 11434)
k = int(os.getenv('K', 3))  # Ensure 'k' is an integer
rest_port = int(os.getenv('REST_PORT', 5001))  # Ensure 'rest_port' is an integer
rest_dbg = os.getenv('REST_DEBUG', 'True').lower() == 'true'  # Convert debug to boolean

base_url = f"http://localhost:{llm_port}"  # Default to port 11434 if not specified

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Initialize the embeddings and Chroma vector store
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
chroma_document_store = Chroma(embedding_function=embeddings, persist_directory="./chroma_db")

# Define the custom Client class to handle the base URL properly
class Client:
    def __init__(self, base_url=base_url, timeout=600):
        self._client = httpx.Client(base_url=base_url, timeout=timeout)

    def generate(self, model, prompt):
        response = self._client.post(
            "/api/generate",
            json={"model": model, "prompt": prompt}
        )

        full_response = ""

        try:
            # Handle potential streaming responses
            for line in response.content.splitlines():
                if line.strip():
                    try:
                        parsed_line = json.loads(line)
                        full_response += parsed_line.get("response", "")
                    except json.JSONDecodeError as e:
                        print(f"Failed to parse line: {line} with error: {e}")

            return full_response
        except Exception as e:
            print(f"Failed to process response: {e}")
            return None

# Function to generate a response using RAG
def generate_response(query):
    # Perform a similarity search with the query string directly
    docs = chroma_document_store.similarity_search(query, k=k)

    # Extract the text content from the retrieved documents
    doc_texts = [doc.page_content for doc in docs]

    # Combine the query with the retrieved documents' content
    combined_input = query + " " + " ".join(doc_texts)
    
    # Uncomment below for debugging
    # with open("combined_input.txt", "w", encoding="utf-8") as f:
    #     f.write(combined_input)
    # print(f"Combined input written to combined_input.txt")
    
    # Instantiate the Client object with the correct base URL
    client = Client(base_url=base_url)

    # Pass combined input to the model
    response = client.generate(model="llama3.1:8b", prompt=combined_input)
    
    return response

# Define route for generating responses
@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    query = data.get('query', '')

    if not query:
        return jsonify({"error": "Query not provided"}), 400
    
    response = generate_response(query)
    
    return jsonify({"response": response})

# Run the Flask app
if __name__ == '__main__':
    app.run(port=rest_port, debug=rest_dbg)  # The Flask server will run on port 5001 by default
