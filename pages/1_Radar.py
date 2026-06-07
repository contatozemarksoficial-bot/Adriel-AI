import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Radar AdrielAI", layout="wide")
st.title("📊 1. Radar de Produtos AdrielAI")

# Configuração API
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")

if st.button("Executar Varredura de Mercado"):
    with st.spinner("Analisando 30 oportunidades com inteligência de dados..."):
        prompt = """
        Atue como um analista sênior de tráfego pago. Liste 30 produtos digitais promissores.
        Divida em duas listas claras:
        
        1. TOP 10 (Alta demanda/Validados): Produtos validados com alta busca.
           - Inclua: Nome, Público, Melhor plataforma para anunciar e POR QUE anunciar lá.
        
        2. Oportunidades (Baixa concorrência/Alta conversão):
           - Inclua: Nome, Público, Diferencial, Melhor local para anunciar e a estratégia para escalar sem bater de frente com grandes players.
           
        Seja técnico e direto.
        """
        resultado = model.generate_content(prompt)
        st.markdown(resultado.text)
