import streamlit as st
import google.generativeai as genai

# Configuração da API
try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
except:
    st.error("Configuração de API não encontrada nos Secrets.")

st.title("📊 1. Radar de Produtos")
st.write("Identifique tendências e oportunidades de mercado.")

# Lógica da ferramenta
termo = st.text_input("Qual nicho ou produto você quer analisar?")

if st.button("Analisar Radar"):
    if termo:
        with st.spinner("Escaneando o mercado..."):
            model = genai.GenerativeModel("gemini-1.5-flash")
            prompt = f"Faça uma análise de mercado para o nicho: {termo}. Identifique tendências, dores do público e potenciais diferenciais."
            resposta = model.generate_content(prompt)
            st.markdown(resposta.text)
    else:
        st.warning("Por favor, digite um produto ou nicho.")
