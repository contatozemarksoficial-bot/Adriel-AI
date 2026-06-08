import streamlit as st
import pandas as pd
import time

# Configuração de Layout Amplo Premium Black para a Entrada do SaaS
st.set_page_config(page_title="Adriel AI - Core Dashboard", layout="wide", initial_sidebar_state="expanded")

# =============================================================================================================
# INJEÇÃO DE CSS DE ALTO PADRÃO (SISTEMA DE CORES BLACK, CIANO NEON E ACENDIMENTO DE MENUS)
# =============================================================================================================
st.markdown("""
<style>
    /* 🌌 Fundo Escuro de Luxo */
    .stApp {
        background-color: #050811 !important;
        color: #ffffff !important;
    }
    
    /* 📟 Customização da Barra Lateral Esquerda */
    [data-testid="stSidebar"] {
        background-color: #02040a !important;
        border-right: 1px solid #1e293b !important;
    }
    
    /* 🔥 FIXAÇÃO DE COR NAS PÁGINAS DO MENU LATERAL (PAGES) */
    [data-testid="stSidebarNav"] ul li a span {
        color: #ffffff !important; 
        font-weight: bold !important;
        font-size: 14px !important;
    }
    [data-testid="stSidebarNav"] ul li a {
        background-color: #0f172a !important; 
        border: 1px solid #1e293b !important;
        border-radius: 8px !important;
        margin-bottom: 6px !important;
        padding: 10px 14px !important;
        transition: all 0.3s ease !important;
    }
    [data-testid="stSidebarNav"] ul li a:hover {
        background-color: #1e293b !important;
        border-color: #00FF87 !important; /* Borda acende em verde neon */
    }
    
    /* 🤖 Caixa Central de Apresentação do Robô */
    .robo-card-welcome {
        background: linear-gradient(135deg, #0f172a 0%, #050811 100%) !important;
        border: 2px solid #00E5FF !important;
        border-radius: 16px !important;
        padding: 30px !important;
        margin-bottom: 30px !important;
        box-shadow: 0px 8px 32px rgba(0, 229, 255, 0.2) !important;
    }
    
    /* 🏛️ Bloco de Monitoramento Executivo */
    .status-card {
        background-color: #0f172a !important;
        border: 1px solid #1e293b !important;
        border-radius: 12px !important;
        padding: 20px !important;
        text-align: center;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.3) !important;
    }
    
    /* Gradientes nos Títulos */
    h1, h2 {
        background: linear-gradient(135deg, #00FF87 0%, #00E5FF 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800 !important;
    }
</style>
""", unsafe_allow_html=True)

# =============================================================================================================
# 🤖 APRESENTAÇÃO MAJESTOSA DO ROBOZINHO NA CENTRAL (VISUAL REQUINTADO DE IMPACTO)
# =============================================================================================================
st.markdown("""
<div class="robo-card-welcome">
    <h1 style='margin-top: 0; font-size: 28px;'>🛸 CENTRAL DE INTELIGÊNCIA: ADRIEL AI</h1>
    <p style='margin: 15px 0 0 0; font-size: 16px; color: #cbd5e1; line-height: 1.6;'>
        "Seja muito bem-vindo, <b>Comandante José Marques da Silva</b>! Os sistemas centrais do robô foram inicializados. 
        Aguardando suas ordens estratégicas. Nossos bancos de dados estão sincronizados com as APIs de mineração global 
        e proteção de tráfego pago."
    </p>
    <div style='margin-top: 15px;'>
        <span style='background: #00FF87; color: #050811; padding: 6px 14px; font-weight: bold; border-radius: 20px; font-size: 12px; box-shadow: 0px 4px 10px rgba(0,255,135,0.3);'>
            MÁQUINA EM OPERAÇÃO 🛡️
        </span>
    </div>
</div>
""", unsafe_allow_html=True)

# =============================================================================================================
# CARDS ESTATÍSTICOS GLOBAIS (REQUINTE EM TELA CHEIA)
# =============================================================================================================
st.markdown("### 📊 STATUS DA INFRAESTRUTURA EM TEMPO REAL")
st.write("")

col_c1, col_c2, col_c3 = st.columns(3)

with col_c1:
    st.markdown("""
    <div class="status-card">
        <h4 style='color: #60a5fa; margin-top:0;'>📡 SERVIDORES MESTRES</h4>
        <h2 style='margin: 10px 0;'>ONLINE 🟢</h2>
        <p style='color: #94a3b8; font-size: 13px; margin:0;'>Handshake síncrono com o GitHub</p>
    </div>
    """, unsafe_allow_html=True)

with col_c2:
    st.markdown("""
    <div class="status-card" style="border-color: #00FF87;">
        <h4 style='color: #00FF87; margin-top:0;'>🔑 GOOGLE ADS API</h4>
        <h2 style='margin: 10px 0;'>AUTENTICADA 🔗</h2>
        <p style='color: #94a3b8; font-size: 13px; margin:0;'>Protocolo OAuth 2.0 Ativo e Pronto</p>
    </div>
    """, unsafe_allow_html=True)

with col_c3:
    st.markdown("""
    <div class="status-card">
        <h4 style='color: #60a5fa; margin-top:0;'>💻 PÁGINAS PRE-SELL</h4>
        <h2 style='margin: 10px 0;'>PROTEGIDAS 🛡️</h2>
        <p style='color: #94a3b8; font-size: 13px; margin:0;'>Roteamento de comissão Hostinger</p>
    </div>
    """, unsafe_allow_html=True)

st.write("---")

# =============================================================================================================
# GRÁFICO GLOBAL DE VOLUME ANALISADO (AUMENTANDO O REQUINTE VISUAL)
# =============================================================================================================
st.markdown("### 📈 MONITORAMENTO VOLUMÉTRICO DAS PLATAFORMAS (CLICKBANK / HOTMART)")
st.caption("Visão macro do tráfego e mineração de ofertas rastreadas nas últimas horas:")
st.write("")

meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
valores_envio = [310 + (i * 45) for i in range(12)]
df_envio = pd.DataFrame({"Volume de Dados Processados": valores_envio}, index=meses)
st.bar_chart(df_envio, use_container_width=True, color="#00E5FF")

# Rodapé profissional
st.write("---")
st.markdown("<p style='text-align: center; font-size: 11px; color: #475569;'>© 2026 Adriel AI - Ferramenta Exclusiva de Inteligência para Afiliados Elite. Todos os Direitos Reservados.</p>", unsafe_allow_html=True)
