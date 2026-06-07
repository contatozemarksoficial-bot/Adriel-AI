import streamlit as st
import google.generativeai as genai

# Configuração da API
try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
except:
    st.error("Erro: API Key não configurada nos Secrets.")

st.title("🚀 5. Estruturador de Pre-sell")
st.write("Crie páginas de alta conversão.")

produto = st.text_input("Qual o nome do produto?")

if st.button("Gerar Estrutura"):
    if produto:
        with st.spinner("O Gemini está criando a estrutura..."):
            model = genai.GenerativeModel("gemini-1.5-flash")
            prompt = f"Crie uma estrutura de página de pre-sell (copywriting) para o produto {produto} focada em alta conversão."
            resposta = model.generate_content(prompt)
            st.markdown(resposta.text)
    else:
        st.warning("Por favor, informe o nome do produto.")
