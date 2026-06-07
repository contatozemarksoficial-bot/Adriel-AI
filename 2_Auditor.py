import streamlit as st
import google.generativeai as genai

# Configuração Padrão
try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
except:
    st.error("Configuração de API pendente.")

st.title("🛡️ Auditor de Mercado")
st.write("Análise de viabilidade e contingência.")

produto = st.text_input("Produto para auditar:")

if st.button("Executar Auditoria"):
    with st.spinner("Analisando..."):
        model = genai.GenerativeModel("gemini-1.5-flash")
        prompt = f"Analise o produto {produto} focado em validar se é um bom nicho."
        resposta = model.generate_content(prompt)
        st.write(resposta.text)
