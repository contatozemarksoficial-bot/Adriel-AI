import streamlit as st
import google.generativeai as genai

# Configuração da Página
st.set_page_config(page_title="Adriel AI - Painel Oficial", layout="wide")

# Sidebar
st.sidebar.title("Adriel AI 🤖")
st.sidebar.info("Bem-vindo ao seu sistema de automação.")

st.title("Adriel AI - Central de Operações")
st.write("O sistema está online! Pronto para processar estratégias.")

# Configuração da API (Segurança)
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    st.success("Conexão com a IA estabelecida com sucesso.")
except:
    st.warning("Configure a GEMINI_API_KEY nas Secrets do Streamlit.")
