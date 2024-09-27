import streamlit as st
import requests

LLAMA_API_KEY = "LA-ea099ef9395941abb1a724a831fe15d7ef19fd4c47c042069fc859f7d9389e23"
LLAMA_API_URL = "https://api.llama-api.com" 


st.title("CircuitSage 🧠🤖")


if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("En que puedo ayudarte hoy?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    headers = {
        "Authorization": f"Bearer {LLAMA_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "prompt": prompt,
        "history": st.session_state.messages 
    }

    response = requests.post(LLAMA_API_URL, headers=headers, json=data)
    
    if response.status_code == 200:
        response_json = response.json()
        assistant_response = response_json.get("response")  
        
        with st.chat_message("assistant"):
            st.markdown(assistant_response)
        st.session_state.messages.append({"role": "assistant", "content": assistant_response})
    else:
        with st.chat_message("assistant"):
            st.markdown("Error: Could not generate response.")
