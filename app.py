import streamlit as st
from cycrew import ask_question  

st.title("Cybersecurity Assistant")
st.write("Ask your cybersecurity questions here. This assistant provides simple, safe explanations from trusted sources.")

user_question = st.text_input("Enter your question:")

if user_question:
    with st.spinner("Finding answer..."):
        answer = ask_question(user_question)
    st.markdown(answer)
