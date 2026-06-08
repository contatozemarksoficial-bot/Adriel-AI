import streamlit as st

st.set_page_config(page_title="AdrielAI", layout="wide")

# Estilo simples e direto para não dar erro de renderização
st.title("🚀 AdrielAI - Central de Comando")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Radar de Produtos")
    st.write("Clique abaixo para iniciar a varredura.")
    if st.button("Executar Radar"):
        st.write("Rodando inteligência...")

with col2:
    st.subheader("✍️ Gerador de Anúncios")
    if st.button("Abrir Gerador"):
        st.switch_page("pages/03_✍️_Gerador.py")

st.sidebar.title("Navegação")
st.sidebar.info("AdrielAI v2026.01")
