import streamlit as st

# Configuração global
st.set_page_config(page_title="AdrielAI - Controle", layout="wide")

# Estilo para forçar o visual escuro e profissional
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    </style>
""", unsafe_allow_html=True)

# Cabeçalho do Dashboard
st.title("🚀 Painel de Controle AdrielAI")
st.markdown("---")

# Métricas de Status
col1, col2, col3 = st.columns(3)
col1.metric("Status API", "Ativo")
col2.metric("Oportunidades", "30")
col3.metric("Versão", "2026.01")

st.markdown("---")

# Aqui entram os botões que levam para as páginas da pasta /pages/
col_a, col_b = st.columns(2)
with col_a:
    st.subheader("📊 Módulos Principais")
    st.page_link("pages/01_📊_Radar.py", label="Radar de Produtos", icon="📊")
    st.page_link("pages/02_🛡️_Auditor.py", label="Auditor de Mercado", icon="🛡️")

with col_b:
    st.subheader("⚙️ Ações")
    st.page_link("pages/03_✍️_Gerador.py", label="Gerador de Anúncios", icon="✍️")
    st.page_link("pages/06_⚙️_Ativador_Google_Ads_API.py", label="Ativador API", icon="⚙️")
