import streamlit as st
import google.generativeai as genai
import pandas as pd

# Configuração de Layout
st.set_page_config(page_title="Adriel AI - Painel Oficial", layout="wide")

# Sidebar - Navegação com o novo nome
st.sidebar.title("Adriel AI 🤖")
st.sidebar.markdown("---")
pagina = st.sidebar.radio("Navegação", ["Dashboard", "Radar de Produtos", "Gerador de Anúncios"])

# Conexão com a IA de forma segura
try:
    # A chave será configurada no Streamlit Cloud -> Secrets
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.generativeai.GenerativeModel("gemini-1.5-flash")
except:
    st.error("Erro: Configure a sua chave 'GEMINI_API_KEY' nas configurações de 'Secrets' do Streamlit!")

# Dashboard
if pagina == "Dashboard":
    st.title("Bem-vindo, Comandante!")
    st.write("### Status: Sistema Adriel AI Online")
    st.info("Utilize o menu lateral para acessar os módulos de inteligência.")

# Radar
elif pagina == "Radar de Produtos":
    st.subheader("📊 Adriel Radar [Filtro Xeque-Mate]")
    # Aqui entra o seu banco de dados ou lógica de filtros
    st.write("O Adriel está scaneando o mercado global...")

# Gerador de Ads
elif pagina == "Gerador de Anúncios":
    st.subheader("🎭 Adriel Ads Master")
    produto = st.text_input("Produto:")
    resumo = st.text_area("Resumo/Dores:")
    
    if st.button("🚀 Gerar Estrutura de Anúncio"):
        with st.spinner("Adriel está criando sua estratégia..."):
            prompt = f"Crie uma estrutura de anúncio Fundo de Funil para {produto}. Resumo: {resumo}. Foque em conversão."
            resposta = model.generate_content(prompt)
            st.text_area("Resultado Final:", value=resposta.text, height=400)
