import streamlit as st

# Configuração da página para modo wide (tela cheia)
st.set_page_config(page_title="AdrielAI - Central", layout="wide", page_icon="🚀")

# Sidebar estilizada
st.sidebar.title("🛠️ AdrielAI Control")
st.sidebar.markdown("---")
st.sidebar.info("Bem-vindo, Adriel. O sistema está operacional.")

# Cabeçalho Profissional
st.title("🚀 Dashboard AdrielAI")
st.markdown("### Inteligência Estratégica para Tráfego Pago")

# Métricas rápidas (Simulando um painel de controle)
col1, col2, col3, col4 = st.columns(4)
col1.metric("Status API", "Ativo", delta="Online")
col2.metric("Oportunidades", "30", delta="+12 hoje")
col3.metric("Criativos Gerados", "142")
col4.metric("Versão", "2026.01")

st.markdown("---")

# Seção de Acesso Rápido
col_a, col_b = st.columns(2)

with col_a:
    st.subheader("💡 Acesso Rápido")
    if st.button("📊 Abrir Radar de Produtos"):
        st.switch_page("pages/1_Radar.py")
    if st.button("🛡️ Abrir Auditor de Mercado"):
        st.switch_page("pages/2_Auditor.py")

with col_b:
    st.subheader("📈 Gestão de Vendas")
    if st.button("✍️ Gerador de Criativos"):
        st.switch_page("pages/3_Gerador.py")
    if st.button("🌐 Fabricante de Pre-sell"):
        st.switch_page("pages/5_Presell.py")

st.markdown("---")
st.warning("O sistema está configurado com o motor Gemini 1.5 Flash.")
