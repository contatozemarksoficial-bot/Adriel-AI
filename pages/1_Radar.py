import streamlit as st
import google.generativeai as genai

# Configuração de Segurança
try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    model = genai.GenerativeModel("gemini-1.5-flash")
except Exception as e:
    st.error(f"Erro na conexão com a IA: {e}")

st.title("📊 1. Radar de Produtos AdrielAI")

if st.button("Gerar 30 Oportunidades de Mercado"):
    with st.spinner("Varredura em tempo real..."):
        prompt = """
        Atue como um analista de tráfego pago de alta performance.
        Liste 30 oportunidades de produtos digitais.
        
        1. TOP 10 (Validados e com alta demanda):
           - Inclua: Nome, Público, Melhor plataforma para anunciar (ex: Google, FB), Por que anunciar.
           
        2. 20 Oportunidades (Baixa concorrência/Nicho):
           - Inclua: Nome, Público, Por que é uma oportunidade, Diferencial competitivo.
           
        Para TUDO, informe a estratégia de anúncio.
        """
        response = model.generate_content(prompt)
        st.markdown(response.text)
