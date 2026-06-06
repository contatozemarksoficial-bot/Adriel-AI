import streamlit as st
import pandas as pd
import google.generativeai as genai

# 1. Configuração da API
try:
    genai.configure(api_key=st.secrets["GEMINI_KEY"])
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
except:
    st.error("Erro: Configure a chave GEMINI_KEY nas Secrets do Streamlit.")

# 2. Configuração da página
st.set_page_config(page_title="Super Cérebro V3", layout="wide")
st.title("👑 Super Cérebro Supremo Unificado V3")

# 3. Dados
produtos_mercado = [
    {"Produto": "Puravive", "Plataforma": "ClickBank", "Comissão": "$142.10"},
    {"Produto": "Sugar Defender", "Plataforma": "BuyGoods", "Comissão": "$127.30"}
]

# 4. Definição das Abas (Aqui o tab1, tab2, tab3 são criados!)
tab1, tab2, tab3 = st.tabs(["📊 Filtro", "🎭 Avatar", "⚙️ Máquina de Ads"])

with tab1:
    st.subheader("📊 Filtro Xeque-Mate")
    st.table(pd.DataFrame(produtos_mercado))

with tab2:
    st.subheader("🎭 Modo Avatar Real")
    produto_sel = st.selectbox("Selecione o produto:", [p["Produto"] for p in produtos_mercado])
    if st.button("Gerar Roteiro"):
        res = model.generate_content(f"Crie um roteiro em inglês para {produto_sel}")
        st.markdown(res.text)

with tab3:
    st.subheader("⚙️ Máquina de Ads")
    prod_ads = st.text_input("Qual o produto?")
    if "res_ads" not in st.session_state: st.session_state.res_ads = None
    
    if st.button("Gerar Estrutura"):
        st.session_state.res_ads = model.generate_content(f"Campanha de Ads para {prod_ads}")
        st.code(st.session_state.res_ads.text)
    
    if st.session_state.res_ads:
        st.download_button("📥 Baixar", st.session_state.res_ads.text, file_name="campanha.txt")
