import streamlit as st
import pandas as pd
import google.generativeai as genai

# Configuração da chave diretamente no código (modo de emergência)
API_KEY = "SUA_CHAVE_REAL_AQUI" 
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

st.set_page_config(page_title="Adriel AI", layout="wide")
st.title("🚀 Adriel AI - Painel de Comando")

tab1, tab2, tab3 = st.tabs(["📊 Radar de Produtos", "🎭 Gerador de Anúncios", "⚙️ Configurações"])

with tab2:
    st.subheader("Gerador de Anúncios")
    produto = st.text_input("Qual o produto?")
    if st.button("Gerar Anúncios"):
        with st.spinner("Processando..."):
            try:
                response = model.generate_content(f"Crie um anúncio de vendas para {produto}")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"Erro: {e}")

with tab3:
    st.subheader("Status do Sistema")
    st.success("Motor de IA: Conectado e operando.")
