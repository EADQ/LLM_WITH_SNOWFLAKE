import streamlit as st, re 

from utils import * 

st.title("Echo Chatbot")

prompt = st.chat_input()
