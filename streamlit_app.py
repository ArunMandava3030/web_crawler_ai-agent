#streamlit_app
import streamlit as st
from app.rag_agent import answer_query

st.set_page_config(page_title="Website → LLM Knowledge", layout="centered")
st.title("🌐 Website → LLM Knowledge")
query = st.text_input("Ask something based on the crawled site:")

if query:
    with st.spinner("Thinking..."):
        answer = answer_query(query)
    st.markdown("### Answer")
    st.write(answer)
