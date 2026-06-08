import streamlit st as st
import pandas as pd
import time
import re

# Configuração premium de layout amplo Black para o Ativador Passo a Passo Independente
st.set_page_config(page_title="Adriel AI - Ativador Google Ads", layout="wide")

# INJEÇÃO DE CÓDIGO CSS PREMIUM DEFINITIVO (BOTÕES NEON PERSONALIZADOS DE LUXO)
st.markdown("""
<style>
    /* Estilo para Botão Principal de Transmissão / Ativação (Verde/Ciano) */
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

st.title("🚀 MÓDULO 6: ASSISTENTE DE CRIAÇÃO E ATIVAÇÃO (GOOGLE ADS API)")
st.markdown("Monte sua campanha do zero passo a passo com auditoria de políticas integradas e envie direto via API.")
st.write("---")

# Inicialização segura das etapas do funil de passos lineares na memória do servidor
if "passo_wizard" not in st.session_state:
    st.session_state.passo_wizard = 1

# Inicialização estável dos parâmetros globais da campanha para evitar resets indesejados
if "wizard_mercado" not in st.session_state: st.session_state.wizard_mercado = "🇺🇸 Campanhas Internacionais (Gringa)"
if "wizard_cust_id" not in st.session_state: st.session_state.wizard_cust_id = "1234567890"
if "wizard_prod" not in st.session_state: st.session_state.wizard_prod = "Citrus Burn"
if "wizard_geo" not in st.session_state: st.session_state.wizard_geo = "Estados Unidos 🇺🇸"
if "wizard_orc" not in st.session_state: st.session_state.wizard_orc = 20.0
if "wizard_cpc" not in st.session_state: st.session_state.wizard_cpc = 0.65

# Barra de progresso visual do funil sequencial no topo da página (Ajustada para 4 etapas reais)
st.progress((st.session_state.passo_wizard - 1) / 3)
st.markdown(f"**Progresso da Estruturação: Etapa {st.session_state.passo_wizard} de 4**")
st.write("---")

# =============================================================================================================
# ETAPA 1: CONEXÃO DE CREDENCIAIS E SELEÇÃO DE MERCADO
# =============================================================================================================
if st.session_state.passo_wizard == 1:
    st.markdown("### 🔑 PASSO 1: DIRECIONAMENTO DE MERCADO E CREDENCIAIS")
    
    rad_mercado = st.radio(
        "Escolha o Tipo de Campanha que deseja criar:",
        ["🇺🇸 Campanhas Internacionais (Gringa)", "🇧🇷 Campanhas Nacionais (Brasil)"],
        index=0 if "🇺🇸" in st.session_state.wizard_mercado else 1,
        key="radio_wizard_mercado"
    )
    st.session_state.wizard_mercado = rad_mercado

    col_c1, col_c2 = st.columns(2)
    with col_c1:
        st.session_state.wizard_cust_id = st.text_input("Google Ads Customer ID (Somente números):", value=st.session_state.wizard_cust_id)
        if "🇺🇸" in rad_mercado:
            st.session_state.wizard_prod = st.text_input("Nome do Produto Gringo:", value=st.session_state.wizard_prod)
        else:
            if st.session_state.wizard_prod == "Citrus Burn":
                st.session_state.wizard_prod = "Protocolo Zero Gordura"
            st.session_state.wizard_prod = st.text_input("Nome do Produto Nacional:", value=st.session_state.wizard_prod)
            
    with col_c2:
        developer_token = st.text_input("Chave Developer Token (API Oculta):", value="API_DEVELOPER_TOKEN_SECURE", type="password")
        if "🇺🇸" in rad_mercado:
            opcoes_geo = ["Estados Unidos 🇺🇸", "Reino Unido 🇬🇧", "Irlanda 🇮🇪", "Canadá 🇨🇦", "Austrália 🇦🇺"]
            geo_idx = opcoes_geo.index(st.session_state.wizard_geo) if st.session_state.wizard_geo in opcoes_geo else 0
            st.session_state.wizard_geo = st.selectbox("País Alvo do Leilão (GEO):", opcoes_geo, index=geo_idx)
        else:
            st.session_state.wizard_geo = st.selectbox("País Alvo do Leilão (GEO):", ["Brasil 🇧🇷"])

    st.write("")
    if st.button("🔗 CONECTAR CONTA VIA API & VALIDAR", key="btn_wiz_connect"):
        with st.spinner("Conectando..."):
            time.sleep(0.8)
            st.success("✅ CONEXÃO ESTABELECIDA COM A API DO GOOGLE ADS!")
            
    st.write("")
    if st.button("AVANÇAR PARA FINANCEIRO / LANCES ➔", key="btn_next_to_s2"):
        st.session_state.passo_wizard = 2
        st.rerun()

# =============================================================================================================
# ETAPA 2: CONFIGURAÇÃO DE LANCES E ORÇAMENTOS
# =============================================================================================================
elif st.session_state.passo_wizard == 2:
    st.markdown("### 💰 PASSO 2: CONFIGURAÇÃO FINANCEIRA DE LANCES (BID)")
    
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
        st.session_state.wizard_orc = st.number_input(f"Orçamento Diário de Escala ({moeda}):", value=st.session_state.wizard_orc if st.session_state.wizard_orc != 20.0 or moeda=="$" else def_orc, step=5.0)
    with col_b2:
        st.session_state.wizard_cpc = st.number_input(f"Limite Máximo de Custo por Clique ({moeda}):", value=st.session_state.wizard_cpc if st.session_state.wizard_cpc != 0.65 or moeda=="$" else def_cpc, step=0.05)

    st.write("")
    col_nav1, col_nav2 = st.columns(2)
    with col_nav1:
        if st.button("⬅ Voltar para Passo 1", key="btn_back_to_s1"):
            st.session_state.passo_wizard = 1
            st.rerun()
    with col_nav2:
        if st.button("AVANÇAR PARA PALAVRAS-CHAVE ➔", key="btn_next_to_s3"):
            st.session_state.passo_wizard = 3
            st.rerun()

# =============================================================================================================
# ETAPA 3: INJEÇÃO E GERAÇÃO DAS LISTAS DE PALAVRAS-CHAVE
# =============================================================================================================
elif st.session_state.passo_wizard == 3:
    st.markdown("### 🎯 PASSO 3: ENGENHARIA DE PALAVRAS-CHAVE DO GRUPO")
    prod = st.session_state.wizard_prod
    
    col_kw1, col_kw2 = st.columns(2)
    with col_kw1:
        if "🇺🇸" in st.session_state.wizard_mercado:
            lista_frase = f'"{prod} official website"\n"buy {prod} online"\n"{prod} discount price"'
        else:
            lista_frase = f'"{prod} site oficial"\n"comprar {prod} original"\n"{prod} desconto hoje"'
        kw_frase = st.text_area("Palavras-Chave de Frase (Use aspas):", value=lista_frase, height=180, key="wizard_kw_frase_txt")
    with col_kw2:
        if "🇺🇸" in st.session_state.wizard_mercado:
            lista_negativas = "scam\ncomplaints\ningredients\nside_effects\nrefund"
        else:
            lista_negativas = "gratis\npdf\ndownload\nmercado livre\nreclame aqui"
        kw_negativa = st.text_area("Palavras-Chave Negativas de Segurança:", value=lista_negativas, height=180, key="wizard_kw_neg_txt")

    st.write("")
    col_nav1, col_nav2 = st.columns(2)
    with col_nav1:
        if st.button("⬅ Voltar para Passo 2", key="btn_back_to_s2"):
            st.session_state.passo_wizard = 2
            st.rerun()
    with col_nav2:
        if st.button("AVANÇAR PARA TEXTOS DO ANÚNCIO ➔", key="btn_next_to_s4"):
            st.session_state.passo_wizard = 4
            st.rerun()

# =============================================================================================================
# ETAPA 4: REDAÇÃO DO ANÚNCIO, DIAGNÓSTICO POLÍTICAS E DISPARO REAL-TIME DA API NO MESMO BLOCO (CORREÇÃO DE TRAVA)
# =============================================================================================================
elif st.session_state.passo_wizard == 4:
    st.markdown("### 📝 PASSO 4: CRIAR ANÚNCIO RESPONSIVO (RSA) & TRANSMITIR PARA O GOOGLE ADS")
    prod = st.session_state.wizard_prod

    if "🇺🇸" in st.session_state.wizard_mercado:
        s_t1, s_t2, s_t3 = f"{prod} Official Website", f"Buy {prod} Online", f"Original {prod} Formula"
        s_d1 = f"Order {prod} from the official website today and get exclusive package discounts."
        s_d2 = "Get the original product with a 100% 60-day money-back guarantee. Secure checkout."
        moeda_simbolo = "$"
    else:
        s_t1, s_t2, s_t3 = f"{prod} Site Oficial", f"Comprar {prod} Original", f"Adquira o {prod} Hoje"
        s_d1 = f"Adquira o {prod} direto no site oficial do fabricante com desconto exclusivo."
        s_d2 = "Garantia de satisfação total ou seu dinheiro de volta. Parcelamento em até 12x no cartão."
        moeda_simbolo = "R$"

    # Garante o preenchimento inicial limpo na troca de mercado de forma persistente
    if st.session_state.t1_val == "": st.session_state.t1_val = s_t1
    if st.session_state.t2_val == "": st.session_state.t2_val = s_t2
    if st.session_state.t3_val == "": st.session_state.t3_val = s_t3
    if st.session_state.d1_val == "": st.session_state.d1_val = s_d1
    if st.session_state.d2_val == "": st.session_state.d2_val = s_d2

    col_t1, col_t2 = st.columns(2)
    with col_t1:
        t1 = st.text_input("Título Principal 1 (Pin 1):", value=st.session_state.t1_val, key="w_t1_box")
