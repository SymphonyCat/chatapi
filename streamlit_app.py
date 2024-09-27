import streamlit as st
from llama_client import LlamaClient  # Suponiendo que tienes un cliente para LLaMA

# Configura el cliente de LLaMA (asegúrate de que esté bien configurado)
llama_model = LlamaClient(model_path="path/to/your/llama/model")

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

    # Generate a response using the LLaMA model.
    response = llama_model.generate_response(
        prompt,
        history=st.session_state.messages  # Si tu cliente admite el historial
    )

    # Stream the response to the chat.
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
