import streamlit as st

# Configuração global da página
st.set_page_config(
    page_title="Adriel AI - Painel Master",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Cabeçalho do Painel
st.title("🚀 Adriel AI - Sistema Master 2026")
st.markdown("---")

# Mensagem de Boas-vindas
st.subheader("Bem-vindo ao seu Centro de Operações de Afiliado")
st.write("""
Este painel centraliza todas as suas ferramentas de inteligência. 
Utilize a barra lateral à esquerda para navegar entre os módulos:
""")

# Cards de Acesso Rápido
col1, col2, col3 = st.columns(3)
with col1:
    st.info("📊 **Radar:** Análise de produtos")
with col2:
    st.info("🛡️ **Auditor:** Validação estratégica")
with col3:
    st.info("✍️ **Gerador:** Criativos de alta conversão")

st.markdown("---")
st.caption("Status do Sistema: **Online** | Versão: **Master 2026**")
