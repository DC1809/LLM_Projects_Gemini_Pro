from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai 

os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model= genai.GenerativeModel("gemini-pro")

def gem_response(question):
    response = model.generate_content(question)
    return response.text


st.set_page_config(page_title="Q&A Demo")
st.header("Gemini Responses")
input=st.text_input("Input: ",key="input")
submit=st.button("Ask the question")
if submit:
    
    response=gem_response(input)
    st.subheader("The Response is")
    st.write(response)