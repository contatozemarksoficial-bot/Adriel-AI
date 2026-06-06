import streamlit as st
import google.generativeai as genai

# 1. Configuração da página e dos segredos
st.set_page_config(page_title="Super Cérebro Supremo Unificado V3", layout="wide")

try:
    api_key = st.secrets["GEMINI_KEY"]
    genai.configure(api_key=api_key)
except KeyError:
    st.error("Erro: Configure a chave GEMINI_KEY nas Secrets do Streamlit.")
    st.stop()

# 2. Definição da estrutura de abas
tab1, tab2, tab3 = st.tabs(["📊 Filtro", "🎭 Avatar", "⚙️ Máquina de Ads"])

# 3. Conteúdo da aba Filtro
with tab1:
    st.header("Filtro Xeque-Mate")
    # Aqui vai a lógica da sua tabela e filtros
    data = {
        "Produto": ["Puravive", "Sugar Defender"],
        "Plataforma": ["ClickBank", "BuyGoods"],
        "Comissão": ["$142.10", "$127.30"]
    }
    st.table(data)

# 4. Conteúdo das outras abas
with tab2:
    st.header("Avatar")
    st.write("Configurações do Avatar aqui...")

with tab3:
    st.header("Máquina de Ads")
    st.write("Configurações da Máquina de Ads aqui...")
