import streamlit as st 
import sys
import os
import requests
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend import api
st.title("Welcome to Streamlit Chatbot")

st.caption("This bot capable of answering the questions which asked")

output = st.text_input("Provide info")
if output:
    response = requests.post("http://127.0.0.1:8000/process/", json={"text": output})
    
    if response.status_code == 200:
        result = response.json()
        st.text(f"Processed Text: {result}")
    else:
        st.error("Error: Unable to process request")