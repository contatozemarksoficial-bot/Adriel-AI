import streamlit as st

# 1. Configuração do ambiente "Dark Tech"
st.set_page_config(page_title="AdrielAI - Painel", layout="wide")

# CSS para bordas arredondadas e estilo Dark
st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: white; }
    div[data-testid="stVerticalBlockBorderWrapper"] { 
        background-color: #161b22; border-radius: 15px; border: 1px solid #30363d; 
    }
    .stButton>button { width: 100%; border-radius: 8px; background-color: #238636; color: white; }
    </style>
    """, unsafe_allow_html=True)

# 2. Cabeçalho do Dashboard
st.title("🚀 AdrielAI | PAINEL DE CONTROLE")
st.markdown("---")

# 3. Layout Principal: Duas colunas grandes
col1, col2 = st.columns([2, 1])

with col1:
    with st.container(border=True):
        st.subheader("📊 MÓDULO 1: RADAR DE PRODUTOS")
        # Aqui você pode chamar uma função que gera sua tabela
        st.write("Tabela de produtos e comissões sendo carregada...")
        st.button("📥 BAIXAR PLANILHA DE INTELIGÊNCIA (.CSV)")

with col2:
    with st.container(border=True):
        st.subheader("✍️ MÓDULO 2: GERADOR DE ANÚNCIOS")
        produto = st.text_input("PRODUTO Gringo:")
        resumo = st.text_area("RESUMO (Nicho/Dores):")
        st.button("🚀 (A) GERAR ANÚNCIOS ADSMASTER")
        st.button("🌐 (B) FABRICAR PRE-SELL")
        st.text_area("Resultado do Gerador:", height=150)
        st.button("💾 [SALVAR CAMPANHA NO HISTÓRICO]")

# 4. Rodapé Profissional
st.markdown("<br><center>© 2026 AdrielAI - Ferramenta Exclusiva de Inteligência para Afiliados Elite.</center>", unsafe_allow_html=True)
