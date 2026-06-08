import streamlit as st
import pandas as pd

# Define o layout da página
st.set_page_config(layout="wide", page_title="Radar de Produtos")

# Define as colunas principais
col_centro, col_direita = st.columns([2, 1])

with col_centro:
    st.markdown('<div class="coluna-container">', unsafe_allow_html=True)
    st.markdown('<div class="header-box-real">👤 Comandante: <b>José Marques</b> | Mapeamento de Leilão Ativo</div>', unsafe_allow_html=True)
    
    col_mini1, col_mini2 = st.columns(2)
    with col_mini1: 
        st.markdown('<div class="kpi-box"><span style="font-size:11px;color:#64748b;font-weight:bold;text-transform:uppercase;">🔥 CLIQUES HOJE</span><br><span style="font-size:20px;color:#00FF87;font-weight:800;">14.250 mil</span></div>', unsafe_allow_html=True)
    with col_mini2: 
        st.markdown('<div class="kpi-box"><span style="font-size:11px;color:#64748b;font-weight:bold;text-transform:uppercase;">📡 OFERTAS ATIVAS NO MUNDO</span><br><span style="font-size:20px;color:#00E5FF;font-weight:800;">1.840 mil</span></div>', unsafe_allow_html=True)
    
    st.write("")
    st.markdown('<p class="subtitulo-bloco-real">MÓDULO 1: RADAR DE PRODUTOS [FILTRO XEQUE-MATE]</p>', unsafe_allow_html=True)
    
    dados_tabela = {
        "Nome do Produto": ["Sugar Defender", "Java Burn", "Puravive", "Prodentim", "GlucoBerry", "Citrus Burn", "Metanail Complex"],
        "Plataforma / Origem": ["BuyGoods 🇺🇸", "ClickBank 🇺🇸", "ClickBank 🇺🇸", "BuyGoods 🇺🇸", "Hotmart 🇧🇷", "ClickBank 🇺🇸", "BuyGoods 🇺🇸"],
        "Comissão Média": ["$ 118.20", "$ 135.00", "$ 142.50", "$ 125.00", "R$ 247,00", "$ 95.00", "$ 107.40"],
        "Veredito da IA": ["APROVADO (Risco Baixo)", "APROVADO (Risco Baixo)", "REVISAR (Risco Médio)", "APROVADO (Risco Baixo)", "APROVADO (Risco Baixo)", "REVISAR (Risco Médio)", "APROVADO (Risco Baixo)"]
    }
    st.dataframe(pd.DataFrame(dados_tabela), use_container_width=True, hide_index=True)
    
    if st.button("📄 [EXPORTAR PLANILHA COMPLETA DO RADAR EM LOTE .CSV]"):
        st.success("✅ Extração executada!")
    st.markdown('</div>', unsafe_allow_html=True)

with col_direita:
    st.markdown('<div class="coluna-container" style="border-right: none;">', unsafe_allow_html=True)
    st.markdown('<div class="header-box-real" style="text-align: right;">Filtro Especial: <b>Top 22 Ativos</b></div>', unsafe_allow_html=True)
    st.info("🔥 **Módulo Espião Operando**\n\nO robô Adriel-AI Pro vasculha as variações de mercado em tempo síncrono.")
    st.markdown('</div>', unsafe_allow_html=True)
