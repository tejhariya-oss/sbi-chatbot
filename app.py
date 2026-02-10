import streamlit as st
from chatbot import get_bot_response

st.set_page_config(page_title="SBI Banking FAQ Chatbot")

st.title("🏦 SBI Banking FAQ Chatbot")

# -------------------------
# Store chat history
# -------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -------------------------
# Display old messages
# -------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# -------------------------
# Chat input (AUTO CLEAR)
# -------------------------
user_input = st.chat_input("Type your question here...")

if user_input:
    # show user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    # get bot reply
    reply = get_bot_response(user_input)

    # show bot reply
    st.session_state.messages.append({"role": "assistant", "content": reply})

    st.rerun()
