import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from htmlTemplate import css, bot_template, user_template
from langchain.llms import HuggingFaceHub

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text        

def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks

def get_vectorstore(text_chunks):
    # embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore

def get_conversation_chain(vectorstore):
    llm = ChatOpenAI()
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory 
    )
    return conversation_chain

def handle_userinput(user_question):
    response = st.session_state.conversation({"question": user_question})
    st.session_state.chat_history = response['chat_history']

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)
            

def main():
    load_dotenv()
    st.set_page_config(page_title="PDF Chat Bot 🤖", page_icon="\U0001F916")
    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None
    
    st.markdown("<h1 style='text-align: center; color: white;'>Ask You PDF</h1>", unsafe_allow_html=True)
    
    
    user_question = st.text_input("⸮ Ask any question about the PDFs:")
    
    if user_question:
        handle_userinput(user_question)

    # Uncomment the following commands to preview what the chat will look like:
    # st.write(user_template.replace("{{MSG}}", "Hey! Bot"), unsafe_allow_html=True)
    # st.write(bot_template.replace("{{MSG}}", "Hi! Human"), unsafe_allow_html=True)

    with st.sidebar:
        img_url = "M.png"

        st.image(img_url)

        st.subheader("Your Documents: :memo:")

        upload_pdf = st.toggle("Select prexisting PDFs")
        
        if not upload_pdf:
            pdf_docs = st.file_uploader(":books: Upload PDFs here :books:", accept_multiple_files=True)   
        else:
            selected_pdfs = st.multiselect('Select Files', ['1.', '2.', '3.', '4.', '5.', '6.'])
            pdf_docs = []

        if st.button("Upload",):
            with st.spinner("Training AI model..."):
                    
                raw_text = get_pdf_text(pdf_docs)
                
                text_chunks = get_text_chunks(raw_text)
                
                vectorstore = get_vectorstore(text_chunks)

                st.session_state.conversation = get_conversation_chain(vectorstore)



if __name__ == "__main__":
    main()
