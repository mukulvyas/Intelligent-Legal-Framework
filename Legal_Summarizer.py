from dotenv import load_dotenv
load_dotenv() ## loading all the environment variables

import os
import google.generativeai as genai
import streamlit as st

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

def main():
    st.header("Legal Summarizer App 📑")

    # Input from user
    paragraph = st.text_area('Enter your paragraph')

    # Radio buttons for selecting summary length
    summary_length = st.radio("Select summary length:", ["50 words", "100 words", "200 words", "300 words"])

    if paragraph:
        # Do Something
        if st.button('Summarize'):
            # Extracting the selected number of words from the summary_length string
            num_words = int(summary_length.split()[0])
            summary_text = chat.send_message(f"Summarize the paragraph for the user in {num_words} words only {paragraph}")

            st.subheader('Summary')
            st.write(summary_text.text)

if __name__ == "__main__":
    main()
