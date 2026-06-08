import streamlit as st

# 1. Configuração do Layout "Dark Theme" e Wide
st.set_page_config(page_title="AdrielAI - Dashboard", layout="wide", page_icon="🚀")

# 2. Estilização CSS para deixar com cara de SaaS profissional
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #1f2937; color: white; }
    .css-1544g2n { padding: 1rem 0; }
    </style>
    """, unsafe_allow_html=True)

# 3. Cabeçalho Executivo
st.title("🚀 AdrielAI | PAINEL DE CONTROLE")
st.markdown("---")
col_header1, col_header2 = st.columns([3, 1])
col_header1.subheader("👋 Olá, Comandante Adriel!")
col_header2.caption("Status: Sistema Online | Chave Mestra: Ativa")

# 4. Estrutura de Grid (O "Coração" do seu design)
col_left, col_right = st.columns([2, 1])

with col_left:
    st.container(border=True).markdown("### 📊 MÓDULO 1: RADAR DE PRODUTOS [FILTRO XEQUE-MATE]")
    # Aqui você chamaria o seu código da página de Radar
    st.write("Tabela de produtos e comissões processando...")

with col_right:
    st.container(border=True).markdown("### ✍️ MÓDULO 2: GERADOR DE ANÚNCIOS")
    produto = st.text_input("Produto Gringo:")
    resumo = st.text_area("Resumo (Nicho/Dores):")
    if st.button("🚀 (A) GERAR ANÚNCIOS"):
        st.success("Anúncios Gerados!")
    if st.button("🌐 (B) FABRICAR PRE-SELL"):
        st.info("Estrutura criada!")

# 5. Rodapé
st.markdown("---")
st.markdown("<center>© 2026 AdrielAI - Ferramenta Exclusiva de Inteligência para Afiliados Elite.</center>", unsafe_allow_html=True)
