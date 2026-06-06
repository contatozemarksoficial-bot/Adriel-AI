import streamlit as st
import pandas as pd
import google.generativeai as genai

# Configuração da API (A chave vem das Secrets do Streamlit)
try:
    genai.configure(api_key=st.secrets["GEMINI_KEY"])
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
except Exception as e:
    st.error("Erro na API. Verifique se a 'GEMINI_KEY' foi salva nas Secrets.")

# Layout do Painel
st.set_page_config(page_title="Painel de Elite", layout="wide")
st.title("👑 Super Cérebro - Painel de Controle")

# Dados do Filtro
produtos_mercado = [
    {"Produto": "Puravive", "Comissão": "$142.10", "Veredito": "APROVADO"},
    {"Produto": "Sugar Defender", "Comissão": "$127.30", "Veredito": "APROVADO"}
]

# Abas do sistema
tab1, tab2, tab3 = st.tabs(["📊 Filtro Xeque-Mate", "🎭 Avatar Real", "⚙️ Máquina de Ads"])

with tab1:
    st.subheader("Radar de Produtos")
    st.table(pd.DataFrame(produtos_mercado))

with tab2:
    st.subheader("Gerador de Criativos")
    produto_sel = st.selectbox("Selecione o produto:", [p["Produto"] for p in produtos_mercado])
    if st.button("Gerar Roteiro"):
        res = model.generate_content(f"Crie um roteiro de vendas para {produto_sel}")
        st.write(res.text)

with tab3:
    st.subheader("Máquina de Ads")
    prod_ads = st.text_input("Qual o produto para a campanha?")
    if st.button("Gerar Estrutura"):
        res_ads = model.generate_content(f"Crie uma campanha de Google Ads para {prod_ads}")
        st.code(res_ads.text)
