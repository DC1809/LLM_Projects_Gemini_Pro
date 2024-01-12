# PDF Interaction Interface: Streamlit Application
## Introduction
"PDF Interaction Interface" is a Streamlit-based web application designed to facilitate interactive Q&A sessions using content extracted from PDF documents. Utilizing advanced natural language processing techniques and Google Generative AI, this application allows users to upload PDF documents, process them, and pose questions whose answers are derived directly from the uploaded material.

## Features

**PDF Upload:** Users can upload one or multiple PDF files.
**Text Extraction: **Extracts text from the uploaded PDF documents.
**Text Chunking:** Splits the extracted text into manageable chunks for processing.
**Vector Store Creation: **Generates embeddings for text chunks and stores them in ChromaDB for efficient retrieval.
**Interactive Q&A:** Users can ask questions and receive answers based on the content of the uploaded PDFs.

## Installation and Setup
**Clone the Repository**

`git clone https://github.com/DC1809/LLM_Projects_Gemini_Pro.git`

**Install Required Packages**

- Ensure you have Python installed on your system.
- Install necessary Python packages using:

`pip install streamlit PyPDF2 langchain langchain_google_genai langchain_community`

**Configuration**
Replace the google_api_key in the script with your Google Generative AI API key.

**Running the Application**
Navigate to the directory containing the app.
Run the application using Streamlit:

`streamlit run app.py`

##  Usage
**Start the Application:** Run the Streamlit app and navigate to the provided local URL.
**Upload PDFs:** Use the sidebar to upload PDF files. Multiple files can be selected.
**Process PDFs:** Click on "Process PDF" after uploading the files.
**Ask Questions:** Enter your question in the "Submit Your Query" text box.
**Receive Answers:** The application will process your question and provide an answer based on the PDF content.

## Technology Stack

**Streamlit:** For creating the web application interface.
**PyPDF2:** To handle PDF file reading and text extraction.
**LangChain:** For text splitting and handling conversational AI chains.
**Google Generative AI:** Powers the conversational AI model for answering questions.
**ChromaDB:** Used for storing and retrieving text embeddings.

<img width="1323" alt="Screenshot 2024-01-12 at 5 02 00 PM" src="https://github.com/DC1809/Kaggle_Case_Studies/assets/153703928/e6173b86-6674-4a3e-bfeb-5c09086df6e6">


