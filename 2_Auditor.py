import streamlit as st
import google.generativeai as genai

try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
except:
    st.error("Configuração de API pendente.")

st.title("🛡️ 2. Auditor de Mercado")
produto = st.text_input("Produto para auditar:")
if st.button("Executar Auditoria"):
    with st.spinner("Analisando..."):
        model = genai.GenerativeModel("gemini-1.5-flash")
        resposta = model.generate_content(f"Analise o produto {produto} focado em validar se é um bom nicho.")
        st.write(resposta.text)
