# Q&A Chatbot
#from langchain.llms import OpenAI

from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter

load_dotenv()  # take environment variables from .env.

import streamlit as st
import os
import pathlib
import textwrap
from PIL import Image

import google.generativeai as genai

text_col, button_col = st.columns([4, 1])


style = """
   <style>
    .css-ocqkz7 {
        position: fixed;
        bottom: 0;
        width: 58%;
        justify-content: center;
        align-items: end;
        padding:0.5rem;
        z-index: 1;
        background-color: #0E1117; 

       }
   </style>
   """
st.markdown(style, unsafe_allow_html=True)




os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

## Function to load OpenAI model and get response
def get_gemini_response(input, image, prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input, image[0], prompt])
    return response.text

def input_image_setup(uploaded_file):
    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")
##initialize our streamlit app

#st.set_page_config(page_title="Legal Assistant and Drafter")
# st.markdown("# Legal Assistant and Drafter")

st.header("Legal Assistant and Drafter 📝")



# List images in the specified directory

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = ""   

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

# Display chat history
st.subheader("Chat History")
for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")


with text_col:
    text_input = st.text_input("Input Prompt:", placeholder="search here...", key="text_input")

with button_col:
    submit = st.button("Submit", key="stButtonVoice")

input_prompt = """
               You are an expert in understanding invoices.
               You will receive input images as invoices &
               you will have to answer questions based on the input image
               you will able to create random answer and can fill the details from the input image
               """

# If submit button is clicked


if submit:
    # Process user input
    image_data = input_image_setup(uploaded_file)
    response = get_gemini_response(input_prompt, image_data, text_input)  # Changed input_text to text_input

    # Display response
    st.subheader("The Response is")
    st.write(response)

    # Store user's question and chatbot's response in session state
    st.session_state['chat_history'].append(("User", text_input))  # Changed input_text to text_input
    st.session_state['chat_history'].append(("Chatbot", response))
