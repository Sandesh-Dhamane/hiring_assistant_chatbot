# app.py
import streamlit as st
from chatbot import HiringAssistant

st.set_page_config(page_title="Hiring Assistant Chatbot")

# Session State Initialization
if "assistant" not in st.session_state:
    st.session_state.assistant = HiringAssistant()
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Chat Interface
st.title("🤖 Hiring Assistant Chatbot")

user_input = st.chat_input("Type your message here...")

if user_input:
    assistant = st.session_state.assistant
    response = assistant.respond(user_input)

    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", response))

# Display chat history
for sender, msg in st.session_state.chat_history:
    with st.chat_message(sender):
        st.markdown(msg)
