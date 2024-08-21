#!/bin/bash
# ------------------------------------------------------------------------------
# Author: Carlos L. Gray
# Date: August 2024
#
# Description:
# This shell script automates the setup of a Python virtual environment for a
# project, ensuring that all necessary dependencies are installed. The script
# performs the following tasks:
#
# 1. Checks if Python3 is installed on the system. If not, it prompts the user
#    to install Python3 before proceeding.
# 2. Creates a Python virtual environment named 'venv' to isolate the project's
#    dependencies.
# 3. Activates the virtual environment to prepare it for package installation.
# 4. Upgrades pip to the latest version to ensure compatibility with all
#    required packages.
# 5. Installs the necessary Python packages, including:
#    - langchain, langchain-community, langchain-chroma, langchain-huggingface
#    - chromadb, httpx, sentence-transformers, pymupdf, python-docx, openpyxl, python-pptx
# 6. Deactivates the virtual environment after installation, leaving the user
#    ready to reactivate it when needed.
#
# Usage:
# Run this script in a terminal. Ensure that Python3 is installed on the system
# before running the script. To start using the environment after setup, use:
#    source venv/bin/activate
#
# ------------------------------------------------------------------------------

# Check if Python3 is installed
if ! command -v python3 &> /dev/null
then
    echo "Python3 could not be found. Please install Python3 and try again."
    exit
fi

# Set up a Python virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Upgrade pip
python3 -m pip install --upgrade pip

# Install the required Python packages
pip install langchain langchain-community langchain-chroma langchain-huggingface chromadb httpx sentence-transformers pymupdf python-docx openpyxl python-pptx flask flask-cors

# Deactivate the virtual environment
deactivate

echo "Setup complete. To activate the environment, run:"
echo "source venv/bin/activate"