# PDF Interaction Interface: Streamlit Application
## Introduction
"PDF Interaction Interface" is a Streamlit-based web application designed to facilitate interactive Q&A sessions using content extracted from PDF documents. Utilizing advanced natural language processing techniques and Google Generative AI, this application allows users to upload PDF documents, process them, and pose questions whose answers are derived directly from the uploaded material.

## Features

**PDF Upload:** Users can upload one or multiple PDF files.<br>
**Text Extraction:** Extracts text from the uploaded PDF documents.<br>
**Text Chunking:** Splits the extracted text into manageable chunks for processing.<br>
**Vector Store Creation:** Generates embeddings for text chunks and stores them in ChromaDB for efficient retrieval.<br>
**Interactive Q&A:** Users can ask questions and receive answers based on the content of the uploaded PDFs.<br>

## Installation and Setup
**Clone the Repository**<br>
`git clone https://github.com/DC1809/LLM_Projects_Gemini_Pro.git`

**Install Required Packages**<br>
- Ensure you have Python installed on your system.<br>
- Install necessary Python packages using:<br>
`pip install streamlit PyPDF2 langchain langchain_google_genai langchain_community`

**Configuration**
Replace the google_api_key in the script with your Google Generative AI API key.

**Running the Application**
Navigate to the directory containing the app.<br>
Run the application using Streamlit:<br>
`streamlit run app.py`

##  Usage
**Start the Application:** Run the Streamlit app and navigate to the provided local URL.<br>
**Upload PDFs:** Use the sidebar to upload PDF files. Multiple files can be selected.<br>
**Process PDFs:** Click on "Process PDF" after uploading the files.<br>
**Ask Questions:** Enter your question in the "Submit Your Query" text box.<br>
**Receive Answers:** The application will process your question and provide an answer based on the PDF content.<br>

## Technology Stack
**Streamlit:** For creating the web application interface.<br>
**PyPDF2:** To handle PDF file reading and text extraction.<br>
**LangChain:** For text splitting and handling conversational AI chains.<br>
**Google Generative AI:** Powers the conversational AI model for answering questions.<br>
**ChromaDB:** Used for storing and retrieving text embeddings.<br>

<img width="1323" alt="Screenshot 2024-01-12 at 5 02 00 PM" src="https://github.com/DC1809/Kaggle_Case_Studies/assets/153703928/e6173b86-6674-4a3e-bfeb-5c09086df6e6">


