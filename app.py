import streamlit as st

st.set_page_config(page_title="AdrielAI - Central", layout="wide", page_icon="🚀")

# Header com estilo
st.title("🚀 AdrielAI - Dashboard Executivo")
st.markdown("---")

# Métricas que transmitem autoridade
col1, col2, col3 = st.columns(3)
col1.metric("API Status", "Online ✅")
col2.metric("Oportunidades", "30+", "Dados em tempo real")
col3.metric("Versão", "v2026.01")

st.markdown("---")

# Navegação visual (Grid de botões)
st.subheader("Acesse suas Ferramentas")
c1, c2 = st.columns(2)

with c1:
    st.info("### 📊 Radar de Mercado")
    if st.button("Explorar Oportunidades"):
        st.switch_page("pages/1_Radar.py")

with c2:
    st.info("### 🛡️ Auditoria")
    if st.button("Validar Produto"):
        st.switch_page("pages/2_Auditor.py")
