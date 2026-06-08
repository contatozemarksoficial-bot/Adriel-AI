import streamlit as st

st.set_page_config(page_title="AdrielAI", layout="wide")

# Estilo CSS para o visual Dark Tech
st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: #c9d1d9; }
    [data-testid="stVerticalBlockBorderWrapper"] { background-color: #161b22; border: 1px solid #30363d; border-radius: 12px; }
    </style>
""", unsafe_allow_html=True)

st.title("🚀 AdrielAI | PAINEL DE CONTROLE")

col1, col2 = st.columns([2, 1])

with col1:
    with st.container(border=True):
        st.subheader("📊 MÓDULO 1: RADAR")
        st.write("Aguardando varredura de mercado...")
        if st.button("Executar Radar"):
            st.success("Radar ativo!")

with col2:
    with st.container(border=True):
        st.subheader("✍️ MÓDULO 2: GERADOR")
        st.text_input("Produto Gringo:")
        st.button("Gerar Anúncios")
