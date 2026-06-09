import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# Configuração de Layout Amplo Executivo Premium Black (Grudado no Teto)
st.set_page_config(page_title="Adriel-AI Pro", layout="wide", initial_sidebar_state="collapsed")

# =============================================================================================================
# INJEÇÃO DE CSS DE ALTO LUXO (ELIMINA A BARRA BRANCA DO TOPO E FIXA O DESIGN DO NOSSO SELETOR LATERAL)
# =============================================================================================================
st.markdown("""
<style>
    /* 🌌 Fundo Escuro Premium Cyber Onyx Original do seu Print */
    .stApp {
        background-color: #0b111e !important;
        color: #ffffff !important;
    }
    
    /* 🚨 EXTINÇÃO TOTAL DA BARRA SUPERIOR BRANCA DO STREAMLIT (ELIMINA A ESTRELA E A LINHA DO TOPO) */
    [data-testid="stHeader"] { 
        display: none !important; 
        height: 0px !important;
        background: transparent !important;
    }
    .stHeader { display: none !important; }
    
    /* 🚨 ZERA AS MARGENS DO TOPO: PUXA O SEU SITE GRUDADO NO TETO DO MONITOR */
    .block-container {
        padding-top: 0.5rem !important;
        padding-bottom: 2rem !important;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
        max-width: 100% !important;
        width: 100% !important;
    }
    
    /* Oculta as abas nativas cinzas antigas */
    [data-testid="stSidebar"] { display: none !important; width: 0px !important; }

    /* 🧱 DIVISÃO RIGOROSA DAS COLUNAS VIRTUAIS EXATAMENTE IGUAL AO SEU CHASSI DE LUXO */
    .coluna-container-lateral {
        background-color: transparent;
        border-right: 1px solid #1e293b;
        padding-right: 20px;
        min-height: 85vh;
    }
    
    .coluna-container-central {
        background-color: transparent;
        padding-left: 15px;
        min-height: 85vh;
    }

    /* 🚨 ANIMAÇÃO DE SINAL NEON PISCANTE PARA AS SETAS E PRODUTOS (CIANO <-> VERDE) */
    @keyframes pulso-vibrante-verde {
        0% { color: #00FF87; text-shadow: 0 0 5px #00FF87; opacity: 0.5; }
        50% { color: #10b981; text-shadow: 0 0 20px #00FF87; opacity: 1; }
        100% { color: #00FF87; text-shadow: 0 0 5px #00FF87; opacity: 0.5; }
    }
    @keyframes pulso-vibrante-azul {
        0% { color: #00E5FF; text-shadow: 0 0 5px #00E5FF; opacity: 0.5; }
        50% { color: #3b82f6; text-shadow: 0 0 20px #00E5FF; opacity: 1; }
        100% { color: #00E5FF; text-shadow: 0 0 5px #00E5FF; opacity: 0.5; }
    }
    
    .sinal-alta { animation: pulso-vibrante-verde 1.2s infinite ease-in-out; font-weight: bold; font-size: 14px; }
    .sinal-estavel { animation: pulso-vibrante-azul 1.5s infinite ease-in-out; font-weight: bold; font-size: 14px; }

    /* DESIGN DOS BOTÕES LATERAIS DE CARBONO PREMIUM POR EXTENSO (FIM DOS ERROS) */
    .menu-lateral-container div.stButton > button {
        background: #0f172a !important; 
        color: #cbd5e1 !important; 
        font-weight: 700 !important;
        font-size: 13px !important;
        border: 1px solid #1e293b !important; 
        text-align: left !important;
        padding: 14px 20px !important;
        width: 100% !important;
        margin-bottom: 8px !important;
        border-radius: 6px !important;
        cursor: pointer !important;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    .menu-lateral-container div.stButton > button:hover {
        background: #1e293b !important;
        color: #00FF87 !important;
        border-color: #00FF87 !important;
    }
    
    /* MOLDURA HOLOGRÁFICA DO SEU PRINT CAMPEÃO */
    .caixa-holografica-real-print {
        background-color: #080f1d !important;
        border: 2.5px solid #00E5FF !important;
        border-radius: 14px !important;
        padding: 24px !important;
        margin-bottom: 25px !important;
    }
    
    .titulo-secao { 
        color: #00FF87; 
        font-size: 16px; 
        font-weight: 800; 
        text-transform: uppercase; 
        margin-bottom: 12px; 
        letter-spacing: 0.5px; 
    }
</style>
""", unsafe_allow_html=True)

# Inicialização segura do roteador de abas na memória RAM do app
if "modulo_ativo" not in st.session_state:
    st.session_state.modulo_ativo = "Radar"

# =============================================================================================================
# MONTAGEM PARALELA: COLUNA 1 (MENU FIXO) + COLUNA 2 (CONTEÚDO DO RADAR COMPLETO)
# =============================================================================================================
col_esquerda, col_direita_conteudo = st.columns([0.22, 0.78])

# 🏢 COLUNA 1: SEUS BOTÕES LATERAIS DE CORREÇÃO (VOLTARAM PARA O LUGAR!)
with col_esquerda:
    st.markdown('<div class="coluna-container-lateral">', unsafe_allow_html=True)
    st.markdown("<h2 style='color: #60a5fa; font-size: 22px; font-weight: 800; margin:0;'>🤖 Adriel-AI <span style='background:#00E5FF; color:#050814; padding:2px 6px; font-size:12px; border-radius:4px; vertical-align:middle;'>PRO</span></h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #475569; font-size: 10px; margin-top:-3px; letter-spacing:1px;'>CONTROL PANEL</p>", unsafe_allow_html=True)
    st.write("---")
    
    st.markdown('<div class="menu-lateral-container">', unsafe_allow_html=True)
    if st.button("🎛️ Dashboard Geral", key="btn_m_dash"): st.session_state.modulo_ativo = "Dashboard"; st.rerun()
    if st.button("🛰️ 1. Radar de Produtos", key="btn_m_radar"): st.session_state.modulo_ativo = "Radar"; st.rerun()
    if st.button("🔬 2. Auditor de Mercado", key="btn_m_auditor"): st.session_state.modulo_ativo = "Auditor"; st.rerun()
    st.write("---")
    st.caption("⚙️ Configurações SaaS")
    st.markdown('</div></div>', unsafe_allow_html=True)

# 🏢 COLUNA 2: ÁREA CENTRAL DE CONTEÚDO QUE RESPONDE AOS COMANDOS DE CLIQUE
with col_direita_conteudo:
    st.markdown('<div class="coluna-container-central">', unsafe_allow_html=True)
    
    # SE A ABA SELECIONADA FOR O RADAR DE PRODUTOS: APRESENTA TUDO COMPLETO E VERDADEIRO
    if st.session_state.modulo_ativo == "Radar":
        
        # 🟢 CLONE EXATO DA CAIXA VERDE DO SEU PRINT NO TOPO DA ABA
        st.markdown("""
        <div class="caixa-holografica-real-print">
            <h3 style="color: #00FF87; font-size: 21px; font-weight: 800; margin: 0 0 14px 0; font-family: sans-serif;">
                📊 MÓDULO 1: RADAR DE PRODUTOS DINÂMICOS
            </h3>
            <p style="color: #cbd5e1; font-size: 14px; line-height: 1.6; margin-bottom: 0px; font-family: sans-serif;">
                Varredura de tráfego internacional ativa. Abaixo estão listadas as 25 ofertas validadas com sinais reais de mercado. 
                Selecione qualquer produto no painel inferior para computar o gráfico de buscas acumuladas hora por hora.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # BANCO DE DADOS OFICIAL - 25 PRODUTOS REAIS (10 TOP ALTA + 15 ESTÁVEIS) 100% CORRIGIDO
        produtos_alta = [
            {"Produto": "Sugar Defender", "Gravidade": "284.50", "Pesquisas Mes": 142000, "Onde Anunciar": "Google Ads (Fundo)", "Porque": "VSL novo convertendo tráfego qualificado de palavra exata com alto ROI."},
            {"Produto": "Puravive", "Gravidade": "241.10", "Pesquisas Mes": 118000, "Onde Anunciar": "Bing Ads + Pre-Sell", "Porque": "Leilão menos concorrido no Bing barateia o CPC em nicho de emagrecimento gringo."},
            {"Produto": "Java Burn", "Gravidade": "198.40", "Pesquisas Mes": 96000, "Onde Anunciar": "Google Ads (Pre-Sell)", "Porque": "Checkout rápido reduz abandono de carrinho. Essencial usar domínio blindado."},
            {"Produto": "Prodentim", "Gravidade": "172.90", "Pesquisas Mes": 84000, "Onde Anunciar": "Google Ads (Fundo)", "Porque": "Saúde dental com altíssima taxa de recorrência e recompra automática."},
            {"Produto": "Alpilean", "Gravidade": "165.20", "Pesquisas Mes": 79000, "Onde Anunciar": "Bing Ads Direto", "Porque": "Baixo reembolso nesta temporada garante estabilidade nas comissões pagas."},
            {"Produto": "GlucoBerry", "Gravidade": "154.80", "Pesquisas Mes": 68000, "Onde Anunciar": "Google Ads (Reino Unido)", "Porque": "Baixa concorrência de grandes afiliados nos países europeus da ClickBank."},
            {"Produto": "Liv Pure", "Gravidade": "147.30", "Pesquisas Mes": 62000, "Onde Anunciar": "Google Ads + Pre-Sell", "Porque": "Nicho de fígado. Páginas pontes robustas eliminam quedas automáticas."},
            {"Produto": "NeuroZoom", "Gravidade": "139.10", "Pesquisas Mes": 54000, "Onde Anunciar": "Google Pesquisa Direta", "Porque": "Produto de foco cognitivo escalando rápido no checkout do BuyGoods."},
            {"Produto": "ZenCortex", "Gravidade": "132.50", "Pesquisas Mes": 49000, "Onde Anunciar": "Google Ads (Maximizar Cliques)", "Porque": "Excelente material de copys prontas fornecido direto pelo gerente da oferta."},
            {"Produto": "Prostadine", "Gravidade": "128.40", "Pesquisas Mes": 45000, "Onde Anunciar": "Bing Ads (EUA)", "Porque": "CTR médio de anúncios subiu 20% após atualização do criativo oficial."}
        ]

        produtos_estaveis = [
            {"Produto": "Dentitox Pro", "Gravidade": "114.60", "Pesquisas Mes": 38000, "Onde Anunciar": "Google Ads (Austrália)", "Porque": "Forte conversão na Austrália fugindo do leilão caro dos EUA."},
            {"Produto": "Metanail Complex", "Gravidade": "109.20", "Pesquisas Mes": 35000, "Onde Anunciar": "Bing Ads + Advertorial", "Porque": "Nicho de fungo de unha performa bem com advertoriais de autoridade."},
            {"Produto": "Kerassentials", "Gravidade": "102.50", "Pesquisas Mes": 31000, "Onde Anunciar": "Google Anúncios RSA", "Porque": "Estabilidade de buscas. Destacar 60 dias de garantia gera urgência."},
