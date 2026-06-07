import streamlit as st
import google.generativeai as genai

# Configuração da API
try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
except:
    st.error("Configuração de API pendente.")

st.title("✍️ Gerador de Criativos")
st.write("Crie anúncios de alta conversão em segundos.")

nicho = st.text_input("Qual o nicho do produto?")
publico = st.text_input("Qual o público-alvo?")

if st.button("Gerar Anúncio"):
    with st.spinner("Escrevendo copy persuasiva..."):
        model = genai.GenerativeModel("gemini-1.5-flash")
        prompt = f"Crie um anúncio de alta conversão para o nicho {nicho} focado em {publico}."
        resposta = model.generate_content(prompt)
        st.write(resposta.text)
