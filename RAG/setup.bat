@echo off
REM ------------------------------------------------------------------------------
REM Author: Carlos L. Gray
REM Date: August 2024
REM 
REM Description:
REM This batch script automates the setup of a Python virtual environment for 
REM a project, including the installation of necessary dependencies. The script 
REM performs the following tasks:
REM 
REM 1. Creates a Python virtual environment named 'venv'.
REM 2. Activates the virtual environment to isolate the project's dependencies.
REM 3. Upgrades pip to ensure the latest package management features.
REM 4. Installs all required Python packages, including:
REM    - langchain, langchain-community, langchain-chroma, and langchain-huggingface
REM    - chromadb, httpx, sentence-transformers, pymupdf, python-docx, openpyxl, python-pptx
REM 5. Deactivates the virtual environment after installation.
REM 
REM After running this script, the environment will be fully prepared for use. 
REM The user can reactivate the environment with a simple command provided at 
REM the end of the script.
REM 
REM Usage:
REM Run this script in a command prompt. The script assumes Python is already 
REM installed on the system. To start using the environment after setup, use:
REM    call venv\Scripts\activate
REM 
REM ------------------------------------------------------------------------------


@echo off

REM Set up a Python virtual environment
python -m venv venv

REM Activate the virtual environment
call venv\Scripts\activate

REM Upgrade pip
python -m pip install --upgrade pip

REM Install the required Python packages
pip install langchain langchain-community langchain-chroma langchain-huggingface chromadb httpx sentence-transformers pymupdf python-docx openpyxl python-pptx flask flask-cors

REM Deactivate the virtual environment
deactivate

echo Setup complete. To activate the environment, run:
echo call venv\Scripts\activate

