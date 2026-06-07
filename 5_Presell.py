import streamlit as st
import google.generativeai as genai

try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
except:
    st.error("Configuração de API pendente.")

st.title("🚀 Estruturador de Pre-sell")
st.write("Crie páginas de pre-sell blindadas.")

produto = st.text_input("Qual o nome do produto?")

if st.button("Gerar Estrutura"):
    with st.spinner("Estruturando sua página..."):
        model = genai.GenerativeModel("gemini-1.5-flash")
        prompt = f"Crie uma estrutura de página de pre-sell para o produto {produto} focada em alta conversão."
        resultado = model.generate_content(prompt)
        st.markdown(resultado.text)
