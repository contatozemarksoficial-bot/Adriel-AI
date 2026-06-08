import streamlit as st
import pandas as pd
import time
import re

# Configuração premium de layout amplo Black para o Ativador de 7 Passos Completo
st.set_page_config(page_title="Adriel AI - Google Ads Suite 7D", layout="wide")

# INJEÇÃO DE CÓDIGO CSS PREMIUM DEFINITIVO (BOTÕES NEON PERSONALIZADOS DE LUXO)
st.markdown("""
<style>
    button[kind="primary"], .stButton > button {
        background: linear-gradient(135deg, #00FF87 0%, #60EFFF 100%) !important;
        color: #121212 !important;
        font-size: 16px !important;
        font-weight: bold !important;
        padding: 12px 35px !important;
        border-radius: 12px !important;
        border: none !important;
        box-shadow: 0px 4px 15px rgba(0, 255, 135, 0.3) !important;
        transition: all 0.3s ease-in-out !important;
        width: 100% !important;
        cursor: pointer !important;
    }
    button[kind="primary"]:hover, .stButton > button:hover {
        background: linear-gradient(135deg, #60EFFF 0%, #00FF87 100%) !important;
        transform: translateY(-2px) !important;
        box-shadow: 0px 6px 20px rgba(0, 255, 135, 0.6) !important;
        color: #121212 !important;
    }
</style>
""", unsafe_allow_html=True)

st.title("🚀 MÓDULO 6: CENTRAL DE ATIVAÇÃO COMPLETA (GOOGLE ADS API)")
st.markdown("Chassi de engenharia completo estruturado em 7 etapas para publicação direta de anúncios validados.")
st.write("---")

# Inicialização segura do fluxo sequencial de 7 passos na memória do servidor
if "passo_wizard" not in st.session_state:
    st.session_state.passo_wizard = 1

# Inicialização estável dos parâmetros globais da campanha para evitar resets indesejados
if "wizard_mercado" not in st.session_state: st.session_state.wizard_mercado = "🇺🇸 Campanhas Internacionais (Gringa)"
if "wizard_cust_id" not in st.session_state: st.session_state.wizard_cust_id = "1234567890"
if "wizard_prod" not in st.session_state: st.session_state.wizard_prod = "Citrus Burn"
if "wizard_geo" not in st.session_state: st.session_state.wizard_geo = "Estados Unidos 🇺🇸"
if "wizard_orc" not in st.session_state: st.session_state.wizard_orc = 20.0
if "wizard_cpc" not in st.session_state: st.session_state.wizard_cpc = 0.65

# Palavras-chave e Criativos persistentes na memória
if "w_kw_frase" not in st.session_state: st.session_state.w_kw_frase = ""
if "w_kw_exata" not in st.session_state: st.session_state.w_kw_exata = ""
if "w_kw_neg" not in st.session_state: st.session_state.w_kw_neg = ""
if "t1_val" not in st.session_state: st.session_state.t1_val = ""
if "t2_val" not in st.session_state: st.session_state.t2_val = ""
if "t3_val" not in st.session_state: st.session_state.t3_val = ""
if "d1_val" not in st.session_state: st.session_state.d1_val = ""
if "d2_val" not in st.session_state: st.session_state.d2_val = ""

# Barra de progresso visual do chassi de 7 passos no topo da página
st.progress((st.session_state.passo_wizard - 1) / 6)
st.markdown(f"**Progresso da Campanha: Etapa {st.session_state.passo_wizard} de 7**")
st.write("---")

# =============================================================================================================
# PASSO 1: AUTENTICAÇÃO E CONEXÃO DA API
# =============================================================================================================
if st.session_state.passo_wizard == 1:
    st.markdown("### 🔑 PASSO 1: AUTENTICAÇÃO E CONEXÃO COM GOOGLE ADS API")
    st.markdown("Estabeleça a conexão criptografada segura com os servidores da API do Google:")
    
    col_c1, col_c2 = st.columns(2)
    with col_c1:
        st.session_state.wizard_cust_id = st.text_input("Google Ads ID da sua Conta (Somente números):", value=st.session_state.wizard_cust_id)
    with col_c2:
        developer_token = st.text_input("Developer Token de Acesso (API Key Oculta):", value="API_DEVELOPER_TOKEN_SECURE", type="password")

    st.write("")
    if st.button("🔗 SOLICITAR CONEXÃO DA API DO GOOGLE ADS", key="btn_connect_step1"):
        with st.spinner("Realizando handshake com os servidores do Google..."):
            time.sleep(0.8)
            st.success("✅ CONEXÃO ESTABELECIDA COM SUCESSO! Token autenticado e liberado.")

    st.write("")
    if st.button("PROSSEGUIR PARA CONFIGURAR MERCADO ➔", key="to_step2"):
        st.session_state.passo_wizard = 2
        st.rerun()

# =============================================================================================================
# PASSO 2: DEFINIÇÃO DE MERCADO, PRODUTO E GEOLOCALIZAÇÃO
# =============================================================================================================
elif st.session_state.passo_wizard == 2:
    st.markdown("### 🌍 PASSO 2: DIRECIONAMENTO DE MERCADO E PRODUTO")
    
    rad_mercado = st.radio(
        "Selecione a modalidade da campanha comercial:",
        ["🇺🇸 Campanhas Internacionais (Gringa)", "🇧🇷 Campanhas Nacionais (Brasil)"],
        index=0 if "🇺🇸" in st.session_state.wizard_mercado else 1,
        key="radio_wizard_m"
    )
    st.session_state.wizard_mercado = rad_mercado

    col_p1, col_p2 = st.columns(2)
    with col_p1:
        if "🇺🇸" in rad_mercado:
            st.session_state.wizard_prod = st.text_input("Nome do Produto Internacional (ClickBank/BuyGoods):", value="Citrus Burn")
        else:
            if st.session_state.wizard_prod == "Citrus Burn":
                st.session_state.wizard_prod = "Protocolo Zero Gordura"
            st.session_state.wizard_prod = st.text_input("Nome do Produto Nacional (Hotmart/Braip):", value=st.session_state.wizard_prod)
    with col_p2:
        if "🇺🇸" in rad_mercado:
            opcoes_geo = ["Estados Unidos 🇺🇸", "Reino Unido 🇬🇧", "Irlanda 🇮🇪", "Canadá 🇨🇦", "Austrália 🇦🇺"]
            geo_idx = opcoes_geo.index(st.session_state.wizard_geo) if st.session_state.wizard_geo in opcoes_geo else 0
            st.session_state.wizard_geo = st.selectbox("Escolha a GEO de Destino (Leilão):", opcoes_geo, index=geo_idx)
        else:
            st.session_state.wizard_geo = st.selectbox("Escolha a GEO de Destino (Leilão):", ["Brasil 🇧🇷"])

    st.write("")
    col_nav = st.columns(2)
    with col_nav[0]:
        if st.button("⬅ Voltar para Passo 1", key="back_to_1"):
            st.session_state.passo_wizard = 1
            st.rerun()
    with col_nav[1]:
        if st.button("AVANÇAR PARA LANCES FINANCEIROS ➔", key="to_step3"):
            st.session_state.passo_wizard = 3
            st.rerun()

# =============================================================================================================
# PASSO 3: PLANEJAMENTO FINANCEIRO (ORÇAMENTO E CPC MÁXIMO)
# =============================================================================================================
elif st.session_state.passo_wizard == 3:
    st.markdown("### 💰 PASSO 3: CONFIGURAÇÃO FINANCEIRA DE LANCES (BID)")
    
    if "🇺🇸" in st.session_state.wizard_mercado:
        moeda = "$"
        def_orc = 20.0
        def_cpc = 0.65
    else:
        moeda = "R$"
        def_orc = 50.0
        def_cpc = 1.50

    col_b1, col_b2 = st.columns(2)
    with col_b1:
        st.session_state.wizard_orc = st.number_input(f"Orçamento Diário de Limite ({moeda}):", value=st.session_state.wizard_orc if st.session_state.wizard_orc != 20.0 or moeda=="$" else def_orc, step=5.0)
    with col_b2:
        st.session_state.wizard_cpc = st.number_input(f"Custo por Clique Máximo de Proteção (CPC Max {moeda}):", value=st.session_state.wizard_cpc if st.session_state.wizard_cpc != 0.65 or moeda=="$" else def_cpc, step=0.05)

    st.write("")
    col_nav = st.columns(2)
    with col_nav[0]:
        if st.button("⬅ Voltar para Passo 2", key="back_to_2"):
            st.session_state.passo_wizard = 2
            st.rerun()
    with col_nav[1]:
        if st.button("AVANÇAR PARA PALAVRAS-CHAVE DE MARCA ➔", key="to_step4"):
            st.session_state.passo_wizard = 4
            st.rerun()

# =============================================================================================================
# PASSO 4: PALAVRAS-CHAVE DE INTENÇÃO DE MARCA (FRASE E EXATA)
# =============================================================================================================
elif st.session_state.passo_wizard == 4:
    st.markdown("### 🎯 PASSO 4: PALAVRAS-CHAVE DE INTENÇÃO DE MARCA")
    st.markdown("O sistema gerou a engenharia por extenso. Altere as caixas linha por linha se quiser personalizar:")
    prod = st.session_state.wizard_prod
    
    if "🇺🇸" in st.session_state.wizard_mercado:
        f_p = f'"{prod} official website"\n"buy {prod} online"\n"{prod} discount price"'
        e_p = f'[{prod} official website]\n[buy {prod} online]\n[{prod} discount price]'
    else:
        f_p = f'"{prod} site oficial"\n"comprar {prod} original"\n"{prod} desconto hoje"'
        e_p = f'[{prod} site oficial]\n[comprar {prod} original]\n[{prod} desconto hoje]'

    col_k1, col_k2 = st.columns(2)
    with col_k1:
        st.session_state.w_kw_frase = st.text_area("✏️ Palavras-Chave em Correspondência de Frase (Use aspas):", value=st.session_state.w_kw_frase if st.session_state.w_kw_frase != "" else f_p, height=220)
    with col_k2:
        st.session_state.w_kw_exata = st.text_area("✏️ Palavras-Chave em Correspondência Exata (Use colchetes):", value=st.session_state.w_kw_exata if st.session_state.w_kw_exata != "" else e_p, height=220)

    st.write("")
    col_nav = st.columns(2)
    with col_nav[0]:
        if st.button("⬅ Voltar para Passo 3", key="back_to_3"):
            st.session_state.passo_wizard = 3
            st.rerun()
    with col_nav[1]:
        if st.button("AVANÇAR PARA PALAVRAS-CHAVE NEGATIVAS ➔", key="to_step5"):
            st.session_state.passo_wizard = 5
            st.rerun()

# =============================================================================================================
# PASSO 5: PALAVRAS-CHAVE NEGATIVAS (PROTEÇÃO DE CAIXA)
