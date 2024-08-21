# OpenRAG Project

The **OpenRAG** project is dedicated to securing funding for ongoing development and new AI-driven projects. By creating and sharing innovative open-source tools like the Retrieval-Augmented Generation (RAG) framework, we aim to advance AI technology and support future initiatives in this space.

## Support the Project

If you find this project useful and would like to support its ongoing development, please consider making a donation:

[![Donate](https://img.shields.io/badge/Donate-PayPal-blue.svg)](https://www.paypal.com/donate/?business=FQDLJUCG8MQ3L&no_recurring=0&item_name=The+OpenRAG+project+is+dedicated+to+securing+funding+for+ongoing+development+and+new+AI-driven+projects.&currency_code=USD)

Bitcoin: bc1qea2qw3k65v3930l0tdxmt25tlztkhaulz3gp4d

Ethereum: 0xCc76D9D79636Da61F308ae2Ac040605Bca3316A0

Your contribution will help fund ongoing development and support new projects within the OpenRAG initiative.

# OpenRAG Setup Guide

This guide will walk you through the process of setting up and running the OpenRAG project on both Windows and Linux/Mac OS.

## Prerequisites

1. **Download and Install Ollama**
   - Visit the [Ollama website](https://ollama.com) to download and install Ollama on your machine.

2. **Pull the Required Model**
   - After installing Ollama, pull the required model by running the following command:
     ```bash
     ollama pull <model>
     ```
     Replace `<model>` with the name of the model you need to pull.

3. **Start the Ollama Server**
   - Start the Ollama server by running:
     ```bash
     ollama serve
     ```
   - To change the port that Ollama is listening on, set the `OLLAMA_HOST` environment variable:

     **Windows:**
     ```cmd
     set OLLAMA_HOST=127.0.0.1:5000
     ```

     **Linux/Mac OS:**
     ```bash
     export OLLAMA_HOST=127.0.0.1:5000
     ```

     This example sets the server to listen on `127.0.0.1` at port `5000`.

## Setting Up the OpenRAG Project

1. **Clone the Repository**
   - Clone the OpenRAG repository from GitHub:
     ```bash
     git clone https://github.com/CarlosLGray/OpenRAG.git
     ```

2. **Navigate to the OpenRAG Directory**
   - Change directory to the OpenRAG project:
     ```bash
     cd OpenRAG
     ```

3. **Navigate to the RAG Directory**
   - Inside the OpenRAG project, navigate to the `RAG` directory:
     ```bash
     cd RAG
     ```

4. **Run Setup Script**
   - On **Mac OS/Linux**:
     ```bash
     ./setup.sh
     ```
   - On **Windows**:
     ```cmd
     setup.bat
     ```

5. **Configure Environment Variables**
   - Create a `.env` file or rename the `.env.example` file to `.env`:
     
     **Windows:**
     ```cmd
     ren .env.example .env
     ```
     
     **Linux/Mac OS:**
     ```bash
     mv .env.example .env
     ```

6. **Create a Python Virtual Environment**
   - Run the following command to create a virtual environment:

     **Windows/Linux/Mac OS:**
     ```bash
     python -m venv venv
     ```

7. **Run the Index Script**
   - Activate your virtual environment if not already activated, then run the `index.py` script:

     **Windows:**
     ```cmd
     venv\Scripts\activate
     python index.py
     ```

     **Linux/Mac OS:**
     ```bash
     source venv/bin/activate
     python index.py
     ```

8. **Run the Main Script**
   - With the virtual environment still activated, run the `main.py` script:

     **Windows:**
     ```cmd
     python main.py
     ```

     **Linux/Mac OS:**
     ```bash
     python main.py
     ```

## Setting Up and Running the Chatbot

1. **Navigate to the Chatbot Directory**
   - Change directory to the `Chatbot` directory:
     ```bash
     cd ../Chatbot
     ```

2. **Configure Environment Variables for Chatbot**
   - Create a `.env` file or rename the `.env.example` file to `.env`:
     
     **Windows:**
     ```cmd
     ren .env.example .env
     ```
     
     **Linux/Mac OS:**
     ```bash
     mv .env.example .env
     ```

3. **Start the Chatbot**
   - Run the following command to start the Chatbot:

     **Windows:**
     ```cmd
     npm install
     ```

     **Linux/Mac OS:**
     ```bash
     npm install
     ```
4. **Start the Chatbot**
   - Run the following command to start the Chatbot:

     **Windows:**
     ```cmd
     npm run start
     ```

     **Linux/Mac OS:**
     ```bash
     npm run start
     ```

This should start the Chatbot server, and you can begin interacting with it through the UI.
