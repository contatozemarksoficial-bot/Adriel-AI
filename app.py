import streamlit as st
import google.generativeai as genai
import pandas as pd

# Configuração da Página
st.set_page_config(page_title="Leonardo AI - Painel Oficial", layout="wide")

# Sidebar - Navegação
st.sidebar.title("Leonardo AI")
st.sidebar.markdown("---")
pagina = st.sidebar.radio("Navegação", ["Dashboard", "Radar de Produtos", "Gerador de Anúncios", "Consultor"])

# Configuração da IA (Use as Secrets do Streamlit para segurança depois)
genai.configure(api_key="SUA_CHAVE_AQUI")
model = genai.GenerativeModel("gemini-1.5-flash")

# --- LÓGICA DO DASHBOARD ---
if pagina == "Dashboard":
    st.title("Bem-vindo, Comandante!")
    st.write("Status: Sistema Online | Chave Mestre Ativa")
    st.info("Use o menu lateral para acessar os módulos de inteligência.")

# --- LÓGICA DO RADAR (Parte 1) ---
elif pagina == "Radar de Produtos":
    st.subheader("📊 Radar de Produtos [Filtro Xeque-Mate]")
    # Aqui entra a sua lista de produtos
    produtos = [{"Produto": "Sugar Defender", "CPC": "$0.42", "Veredito": "APROVADO"}]
    st.table(pd.DataFrame(produtos))
    if st.button("Baixar Planilha .CSV"):
        st.download_button("Download", data="csv_data", file_name="produtos.csv")

# --- LÓGICA DO GERADOR DE ADS (Parte 4) ---
elif pagina == "Gerador de Anúncios":
    st.subheader("🎭 Gerador de Anúncios Master")
    produto = st.text_input("Produto:")
    resumo = st.text_area("Resumo/Dores:")
    
    if st.button("🚀 Gerar Estrutura de Anúncio"):
        with st.spinner("Leonardo está processando..."):
            prompt = f"Crie anúncios para {produto} sobre {resumo}. Siga a estrutura de headlines, descrições e keywords."
            resposta = model.generate_content(prompt)
            st.text_area("Resultado:", value=resposta.text, height=300)
