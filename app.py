import streamlit as st
import pandas as pd
import google.generativeai as genai

# Configuração Global
st.set_page_config(page_title="Painel de Elite", layout="wide")

# Estilo para deixar com cara de painel profissional
st.markdown("""
    <style>
    .main {background-color: #0e1117;}
    .stButton>button {width: 100%; border-radius: 5px; font-weight: bold;}
    </style>
    """, unsafe_allow_html=True)

# Cabeçalho com status
col1, col2 = st.columns([3, 1])
with col1:
    st.title("👑 Painel de Comando Leonardo AI")
with col2:
    st.info("Status: Sistema Online")

# Dados
produtos = pd.DataFrame([
    {"Produto": "Puravive", "Comissão": "$142", "Risco": "Baixo"},
    {"Produto": "Sugar Defender", "Comissão": "$127", "Risco": "Baixo"}
])

# Estrutura em Abas Visuais
aba1, aba2, aba3 = st.tabs(["📊 Radar de Produtos", "🎭 Gerador de Anúncios", "⚙️ Configurações"])

with aba1:
    st.subheader("Radar de Oportunidades [Filtro Xeque-Mate]")
    st.dataframe(produtos, use_container_width=True)

with aba2:
    col_a, col_b = st.columns(2)
    with col_a:
        st.subheader("Entrada de Dados")
        prod_escolhido = st.selectbox("Escolha o produto:", produtos["Produto"])
        nicho = st.text_input("Resumo do Nicho/Dores:")
    with col_b:
        st.subheader("Ações Rápidas")
        if st.button("🚀 Gerar Anúncios Master"):
            st.success("Criativo pronto!")
            st.text_area("Resultado:", "Aqui entrará o copy gerado pela IA...")

with aba3:
    st.subheader("Configurações do Sistema")
    st.write("Chave API: Ativa ✅")
