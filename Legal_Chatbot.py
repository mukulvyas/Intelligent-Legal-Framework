from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

load_dotenv()

# Configure API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize chat model
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response

# Initialize Streamlit app
st.set_page_config(page_title="Legal Chatbot")
st.header("Legal ChatBot 🤖")

# Initialize session state for chat history and input value
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []
if 'input_value' not in st.session_state:
    st.session_state['input_value'] = " "

# Display chat history with a horizontal line between each question and its response
st.subheader("Chat History")
for i, (role, text) in enumerate(st.session_state['chat_history']):
    if i > 0 and role == "You" and st.session_state['chat_history'][i - 1][0] == "Bot":
        st.markdown("<hr style='border: 1px solid black;'>", unsafe_allow_html=True)  # Add a horizontal line in black
    st.write(f"{role}: {text}")

# User input and submission
with st.form("input_form"):
    input_question = st.text_input("Input: ", key="input", placeholder="Type your question here...",
                                   value=st.session_state['input_value'])

    form_submitted = st.form_submit_button("Ask the question")

    if form_submitted:
        response = get_gemini_response(input_question)

        # Display Gemini response
        st.subheader("Response:")
        for chunk in response:
            st.write(chunk.text)

        # Add user query and response to session state chat history
        st.session_state['chat_history'].append(("You", input_question))
        for chunk in response:
            st.session_state['chat_history'].append(("Bot", chunk.text))

        # Update input value in session state
        st.session_state['input_value'] = " "