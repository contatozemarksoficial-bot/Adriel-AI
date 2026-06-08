import streamlit as st

# 1. Configuração do ambiente profissional
st.set_page_config(page_title="AdrielAI - Elite", layout="wide", page_icon="⚡")

# 2. Estilização CSS para o visual 'Dark Tech'
st.markdown("""
    <style>
    /* Fundo escuro elegante */
    .stApp { background-color: #050505; }
    /* Estilo das caixas (Containers) */
    [data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #111111;
        border: 1px solid #333333;
        border-radius: 12px;
        padding: 20px;
    }
    /* Estilo dos títulos */
    h1, h2, h3 { color: #ffffff !important; }
    </style>
""", unsafe_allow_html=True)

# 3. Cabeçalho Minimalista
st.title("⚡ AdrielAI")
st.markdown("### A Inteligência de Elite para Google Ads")

# 4. Layout em Colunas (O design da imagem)
col1, col2 = st.columns([2, 1])

with col1:
    with st.container(border=True):
        st.subheader("📊 Módulo de Radar")
        st.write("Varredura de mercado em tempo real ativa.")
        if st.button("Executar Radar Completo"):
            st.info("Varredura iniciada...")

with col2:
    with st.container(border=True):
        st.subheader("⚙️ Configurações")
        st.toggle("API Google Ads Ativa")
        st.toggle("Modo de Performance")
        st.button("Resetar Sistema")

# 5. Área de Acesso Rápido (Estilo ícones)
st.markdown("---")
cols = st.columns(5)
with cols[0]: st.button("📊 Radar")
with cols[1]: st.button("🛡️ Auditor")
with cols[2]: st.button("✍️ Gerador")
with cols[3]: st.button("🔍 Caçador")
with cols[4]: st.button("🌐 Pre-sell")
