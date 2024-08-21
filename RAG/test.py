"""
Author: Carlos L. Gray
Date: August 2024

Description:
This Python script defines a custom Client class to interact with an API endpoint 
hosted locally at a configurable port, which is read from a `.env` file. The script 
is designed to send prompts to a specified model (e.g., "llama3.1:8b") and retrieve 
generated responses. It accomplishes the following tasks:

1. Loads environment variables from a `.env` file to configure the API's port.
2. Initializes an `httpx.Client` to manage HTTP requests to the API using the base URL
   that includes the configured port.
3. Implements a `generate` method within the Client class to send POST requests 
   to the `/api/generate` endpoint. This method:
   - Sends the model and prompt as JSON payloads.
   - Handles potential streaming responses by accumulating the response content 
     into a single string.
   - Includes error handling to manage JSON decoding issues and other exceptions 
     that may arise during the request.

4. The script also accepts a query as a command-line parameter, allowing dynamic
   interaction with the model.

Usage:
- Ensure the `.env` file is present in the same directory as this script and contains 
  a line defining the `PORT` (e.g., `LLM_PORT=11434`).
- Pass a query as a command-line argument to dynamically test different prompts 
  with the model.
- The script is designed for flexibility, allowing easy adjustments to the model 
  name and prompt structure as needed.
"""

import os
import sys
import httpx
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
port = os.getenv("LLM_PORT", "11434")  # Default to 11434 if PORT is not set

# Define the custom Client class to handle the base URL properly
class Client:
    def __init__(self, base_url=f"http://localhost:{port}"):
        self._client = httpx.Client(base_url=base_url)

    def generate(self, model, prompt):
        response = self._client.post(
            "/api/generate",
            json={"model": model, "prompt": prompt},
            timeout=None
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

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a query as a command-line argument.")
        sys.exit(1)
    
    query = sys.argv[1]
    
    # Instantiate the Client object with the correct base URL
    client = Client()

    # Generate the response using the provided query
    response = client.generate(model="llama3.1:8b", prompt=query)
    print(response)
