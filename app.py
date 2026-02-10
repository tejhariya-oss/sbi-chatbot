import streamlit as st
from chatbot import get_bot_response

st.set_page_config(page_title="SBI Banking FAQ Chatbot")

st.title("🏦 SBI Banking FAQ Chatbot")

if "chat" not in st.session_state:
    st.session_state.chat = []

user_input = st.text_input("Ask your question:")

if st.button("Send") and user_input:
    reply = get_bot_response(user_input)

    st.session_state.chat.append(("You", user_input))
    st.session_state.chat.append(("Bot", reply))


for sender, msg in st.session_state.chat:
    if sender == "You":
        st.markdown(f"🔴 **You:** {msg}")
    else:
        st.markdown(f"🟢 **Bot:** {msg}")

