import streamlit as st
import google.generativeai as genai

# Configuração da API
try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
except:
    st.error("Erro: API Key não configurada nos Secrets.")

st.title("✍️ 3. Gerador de Criativos")
st.write("Crie textos de anúncios de alta conversão.")

# Campos de entrada
nicho = st.text_input("Qual o nicho do produto?")
publico = st.text_input("Quem é o público-alvo?")

if st.button("Gerar Criativo"):
    if nicho and publico:
        with st.spinner("O Gemini está criando seu criativo..."):
            model = genai.GenerativeModel("gemini-1.5-flash")
            prompt = f"Escreva 3 variações de textos de anúncios focados em conversão para o nicho {nicho} atingindo o público {publico}."
            resposta = model.generate_content(prompt)
            st.markdown(resposta.text)
    else:
        st.warning("Preencha o nicho e o público para continuar.")
