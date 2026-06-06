import streamlit as st

st.title("Teste de Chave")

if "GEMINI_KEY" in st.secrets:
    chave = st.secrets["GEMINI_KEY"]
    st.success(f"Chave encontrada! Primeiros caracteres: {chave[:5]}...")
else:
    st.error("A chave não está sendo lida pelo Streamlit. O arquivo Secrets está vazio ou incorreto.")
