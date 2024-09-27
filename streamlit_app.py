import streamlit as st
import requests

# Predefined LLaMA API Key and endpoint
LLAMA_API_KEY = "LA-ea099ef9395941abb1a724a831fe15d7ef19fd4c47c042069fc859f7d9389e23"  # Reemplaza esto con tu clave API real
LLAMA_API_URL = "https://api.llama-api.com"  # Cambia a tu endpoint

# Show title and description.
st.title("💬 Chatbot LLaMA")
st.write(
    "This is a simple chatbot that uses LLaMA to generate responses. "
    "You can learn how to build this app step by step by [following our tutorial](https://docs.streamlit.io/develop/tutorials/llms/build-conversational-apps)."
)

# Create a session state variable to store the chat messages.
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display the existing chat messages.
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Create a chat input field to allow the user to enter a message.
if prompt := st.chat_input("What is up?"):
    # Store and display the current prompt.
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Prepare the request to the LLaMA API.
    headers = {
        "Authorization": f"Bearer {LLAMA_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "prompt": prompt,
        "history": st.session_state.messages  # Si tu API soporta el historial
    }

    # Generate a response using the LLaMA API.
    response = requests.post(LLAMA_API_URL, headers=headers, json=data)
    
    if response.status_code == 200:
        response_json = response.json()
        assistant_response = response_json.get("response")  # Ajusta esto según la estructura de tu respuesta
        
        # Stream the response to the chat.
        with st.chat_message("assistant"):
            st.markdown(assistant_response)
        st.session_state.messages.append({"role": "assistant", "content": assistant_response})
    else:
        with st.chat_message("assistant"):
            st.markdown("Error: Could not generate response.")
