import streamlit as st, re 

from utils import * 

st.title("Echo Chatbot 2.0")

prompt = st.chat_input()
if prompt:
    st.chat_message(prompt)
