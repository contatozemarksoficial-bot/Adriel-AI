import streamlit as st
import pandas as pd
import google.generativeai as genai

# Configuração da API
genai.configure(api_key=st.secrets["GEMINI_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")

st.set_page_config(page_title="Leonardo AI", layout="wide")
st.title("👑 Painel de Comando Leonardo AI")

tab1, tab2, tab3 = st.tabs(["📊 Radar de Produtos", "🎭 Gerador de Anúncios", "⚙️ Configurações"])

with tab2:
    st.subheader("Gerador de Anúncios Master")
    produto = st.text_input("Qual o produto gringo?")
    if st.button("Gerar Estratégia de Vendas"):
        with st.spinner("IA criando seu criativo de alta conversão..."):
            prompt = f"Crie um roteiro de vendas e anúncios para o produto {produto} focado em afiliados."
            response = model.generate_content(prompt)
            st.success("Criativo gerado com sucesso!")
            st.markdown(response.text)
