import streamlit as st
import google.generativeai as genai

# Tenta carregar a chave direto dos secrets
api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)

st.title("📊 1. Radar")
# Resto do seu código...
