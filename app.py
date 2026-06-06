import streamlit as st
import pandas as pd
import google.generativeai as genai
from datetime import datetime

# 1. CONFIGURAÇÃO
st.set_page_config(page_title="Super Cérebro V3", layout="wide")
st.title("👑 Super Cérebro Supremo Unificado V3")

# Configuração da API (Recomendo usar st.secrets para segurança)
genai.configure(api_key="SUA_CHAVE_AQUI")
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# 2. DADOS DO FILTRO XEQUE-MATE
produtos_mercado = [
    {"Produto": "Puravive", "Plataforma": "ClickBank", "Comissão": "$142.10", "País": "Canadá", "CPC": "$0.35", "Vantagem": "70% Mais Barato que nos EUA"},
    {"Produto": "Sugar Defender", "Plataforma": "BuyGoods", "Comissão": "$127.30", "País": "Reino Unido", "CPC": "$0.42", "Vantagem": "Alta busca orgânica"},
    {"Produto": "Java Burn", "Plataforma": "ClickBank", "Comissão": "$118.00", "País": "Austrália", "CPC": "$0.38", "Vantagem": "Nicho de café matinal"},
    {"Produto": "ProDentim", "Plataforma": "ClickBank", "Comissão": "$122.50", "País": "Irlanda", "CPC": "$0.28", "Vantagem": "Alta conversão local"},
    {"Produto": "Alpha Tonic", "Plataforma": "MaxWeb", "Comissão": "$155.00", "País": "Nova Zelândia", "CPC": "$0.45", "Vantagem": "Tráfego livre"},
    {"Produto": "Pineal Guard", "Plataforma": "Digistore24", "Comissão": "$129.50", "País": "África do Sul", "CPC": "$0.18", "Vantagem": "Cliques baixíssimos"},
    {"Produto": "SightCare", "Plataforma": "ClickBank", "Comissão": "$147.00", "País": "Cingapura", "CPC": "$0.50", "Vantagem": "Público rico"}
]

# 3. INTERFACE DE VISUALIZAÇÃO
st.subheader("📊 Filtro Xeque-Mate: Os 7 Alvos")
df = pd.DataFrame(produtos_mercado)
st.table(df)

# 4. INTERFACE DO GERADOR DE ANÚNCIO (PARTE 2)
st.subheader("🎭 Criador de Conteúdo: Modo Avatar Real")
produto_escolhido = st.selectbox("Escolha o produto para gerar o anúncio:", df["Produto"].tolist())

if st.button("Gerar Roteiro e Prompt"):
    with st.spinner("O Super Cérebro está criando seu anúncio..."):
        contexto = f"""
        Você é o maior especialista em tráfego de afiliados. Crie para o produto {produto_escolhido}:
        1. Prompt em inglês para Leonardo.ai (avatar).
        2. História de 30 segundos em inglês para narração.
        3. 5 Hashtags em inglês.
        Responda os títulos em português e o conteúdo na língua pedida.
        """
        try:
            resposta = model.generate_content(contexto)
            st.markdown(resposta.text)
        except Exception as e:
            st.error(f"Erro ao gerar conteúdo: {e}")
