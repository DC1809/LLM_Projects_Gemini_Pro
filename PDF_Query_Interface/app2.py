import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.chains.question_answering import load_qa_chain

# Configuration for Google Generative AI
google_api_key = 'AIzaSyAcXdWGzJwzXxhL4NhYkXLGuTOyLMtegYY'


def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text



def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=200)
    return text_splitter.split_text(text)


class SimpleDoc:
    def __init__(self, content, metadata=None):
        self.page_content = content
        self.metadata = metadata if metadata is not None else {}

def get_vector_store(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=google_api_key)

    # Convert each text chunk into a SimpleDoc object with default metadata
    document_objects = [SimpleDoc(chunk) for chunk in text_chunks]

    return Chroma.from_documents(document_objects, embedding=embeddings, persist_directory="./chroma_db")




def get_conversational_chain():
    prompt_template = """
    Answer the question as detailed as possible from the provided context, make sure to provide all the details, if the answer is not in
    provided context just say, 'answer is not available in the context', don't provide the wrong answer\n\n
    Context:\n {context}?\n
    Question: \n{question}\n

    Answer:
    """
    model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3, google_api_key=google_api_key)
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    return load_qa_chain(model, chain_type="stuff", prompt=prompt)


def user_input(question, vector_store):
    docs = vector_store.similarity_search(question)
    chain = get_conversational_chain()
    response = chain({"input_documents": docs, "question": question}, return_only_outputs=True)
    return response['output_text']


def main():
    st.set_page_config("Chat PDF")
    st.header("PDF Interaction Interface")

    with st.sidebar:
        st.title("Upload PDF")
        pdf_docs = st.file_uploader("Multiple PDF upload", accept_multiple_files=True)
        if st.button("Process PDF"):
            if pdf_docs:
                with st.spinner("Processing PDF..."):
                    text = get_pdf_text(pdf_docs)
                    text_chunks = get_text_chunks(text)
                    vector_store = get_vector_store(text_chunks)
                    st.success("PDF Processed")

    user_question = st.text_input("Submit Your Query")
    if user_question and 'vector_store' in locals():
        reply = user_input(user_question, vector_store)
        st.write("Reply: ", reply)
    else:
        st.write("Please upload and process a PDF first.")

if __name__ == "__main__":
    main()
