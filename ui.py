import streamlit as st
import subprocess

st.set_page_config(page_title="Legal Assistant Application")

# with open('style.css') as f:
#     st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Streamlit UI
def main():
    st.title("Legal Assistant Application 🏛️")
    st.sidebar.title("Navigation")
    pages = {
        "🏠 Home": home_page,
        "📝 Legal Assistant and Drafter": legal_drafter_assistant_page,
        "📑 Legal Summarizer": legal_summarizer_page,
        "🤖 Legal Chatbot": legal_chatbot_page,
        "📚 Legal Multi-PDF Chat": legal_multi_pdf_chat_page
    }
    app_mode = st.sidebar.radio("Go to", list(pages.keys()))
    pages[app_mode]()

    if st.sidebar.button("Go"):
        run_subprocess(app_mode)

# Home Page
def home_page():
    st.header("Welcome to Legal Assistant Application ⚖️")
    st.write("""
        This application provides various tools to assist with legal tasks. 
        Select an option from the sidebar to get started.
    """)
    st.image("image.png", use_column_width=True)

# Legal Drafter and Assistant Page
def legal_drafter_assistant_page():
    st.header("Legal Assistant and Drafter 📝")
    
    st.write("""
        The Legal Assistant and Drafter feature provides a comprehensive suite of tools to streamline legal document drafting and support tasks. From drafting contracts and agreements to assisting with legal research and document review, our tool simplifies complex legal processes and enhances productivity.
             Whether you're a legal professional or handling legal matters as a business owner or individual, our Legal Assistant and Drafter feature equips you with the resources and functionality needed to succeed in the practice of law.
    """)
    st.image("image.png", use_column_width=True)
# Legal Summarizer Page
def legal_summarizer_page():
    st.header("Legal Summarizer 📑")
    st.write("""The legal summarizer tool condenses lengthy legal documents into concise summaries, 
        providing a quick overview of the key points and arguments within the text. This can save valuable time for legal professionals by allowing them to focus 
        on the most relevant information without having to read through every detail.
    """)
    st.image("image.png", use_column_width=True)
# Legal Chatbot Page
def legal_chatbot_page():
    st.header("Legal Chatbot 🤖")
    st.write("""
        The legal chatbot is an interactive tool that provides legal guidance and answers 
        to common legal questions. Users can ask the chatbot about various legal topics 
        such as contract law, intellectual property, and employment law, and receive 
        accurate and reliable information in real-time. The chatbot can help users 
        understand their rights, obligations, and potential legal risks, making it a 
        valuable resource for both individuals and businesses.
    """)
    st.image("image.png", use_column_width=True)
# Legal Multi-PDF Chat Page
def legal_multi_pdf_chat_page():
    st.header("Legal Multi-PDF Chat 📚")
    st.write("""
        The legal multi-PDF chat page allows users to upload multiple legal documents in PDF format 
        and engage in a real-time chat to discuss and collaborate on the content. This feature 
        facilitates collaboration among legal professionals, enabling them to review documents, 
        exchange ideas, and provide feedback in a collaborative environment. Users can highlight 
        specific sections of the documents, ask questions, and share insights, enhancing 
        communication and productivity in legal workflows.
    """)
    st.image("image.png", use_column_width=True)
# Function to run subprocess based on selected option
def run_subprocess(selected_option):
    if selected_option == "📝 Legal Assistant and Drafter":
        subprocess.run(["streamlit", "run", "Legal_Assistant_and_Drafter.py"])
    elif selected_option == "📑 Legal Summarizer":
        subprocess.run(["streamlit", "run", "Legal_Summarizer.py"])
    elif selected_option == "🤖 Legal Chatbot":
        subprocess  .run(["streamlit", "run", "Legal_Chatbot.py"])
    elif selected_option == "📚 Legal Multi-PDF Chat":
        subprocess.run(["streamlit", "run", "Legal_Multi_PDF_Chat.py"])

if __name__ == "__main__":
    main()
