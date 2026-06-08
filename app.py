import streamlit as st
import pandas as pd

# Configuração de Layout herdado da família Adriel AI
st.markdown("""
<style>
    .stApp { background-color: #0b111e !important; color: #ffffff !important; }
    h2 { background: linear-gradient(135deg, #00FF87 0%, #00E5FF 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-weight: 800 !important; }
</style>
""", unsafe_allow_html=True)

st.markdown("<h2>🛰️ MÓDULO 1: RADAR DE PRODUTOS [FILTRO XEQUE-MATE]</h2>", unsafe_allow_html=True)
st.write("Filtro analítico focado na extração de ofertas de alta conversão nas plataformas internacionais.")
st.write("---")

# Tabela simplificada temporária para testar o funcionamento da página pages
dados_radar = {
    "Nome do Produto": ["Sugar Defender", "Java Burn", "Puravive"],
    "Gravidade": ["210+", "180+", "150+"],
    "Status": ["Livre 🟢", "Livre 🟢", "Competitivo 🟡"]
}
st.dataframe(pd.DataFrame(dados_radar), use_container_width=True, hide_index=True)
