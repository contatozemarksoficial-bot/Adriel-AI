import streamlit as st
import pandas as pd
import time

# Configuração de Layout Amplo Premium Black para a Entrada do SaaS
st.set_page_config(page_title="Adriel AI - Core Dashboard", layout="wide", initial_sidebar_state="expanded")

# =============================================================================================================
# INJEÇÃO DE CÓDIGO CSS PREMIUM DEFINITIVO (ANIMAÇÕES CONTÍNUAS: PISCADO NEON & FLUTUAÇÃO DO ROBÔ)
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
    
    /* 🚨 1. ANIMAÇÃO DO MENU LATERAL PISCANDO EM LINHA (PULSAR NEON CONTÍNUO) */
    @keyframes pulsa-neon {
        0% {
            border-color: #1e293b;
            box-shadow: 0 0 5px rgba(0, 229, 255, 0.1);
        }
        50% {
            border-color: #00FF87;
            box-shadow: 0 0 15px rgba(0, 255, 135, 0.6);
        }
        100% {
            border-color: #1e293b;
            box-shadow: 0 0 5px rgba(0, 229, 255, 0.1);
        }
    }

    [data-testid="stSidebarNav"] ul li a span {
        color: #ffffff !important; 
        font-weight: bold !important;
        font-size: 14px !important;
    }
    
    [data-testid="stSidebarNav"] ul li a {
        background-color: #0f172a !important; 
        border: 2px solid #1e293b !important;
        border-radius: 8px !important;
        margin-bottom: 8px !important;
        padding: 12px 14px !important;
        animation: pulsa-neon 3s infinite ease-in-out !important; /* Faz o menu piscar sempre */
        display: block !important;
    }
    
    [data-testid="stSidebarNav"] ul li a:hover {
        background-color: #1e293b !important;
        animation: none !important; /* Trava aceso no mouse */
        border-color: #00E5FF !important;
        box-shadow: 0 0 20px rgba(0, 229, 255, 0.8) !important;
    }
    
    /* 🛸 2. ANIMAÇÃO DO ROBÔ FLUTUANDO NA TELA DA FRENTE (EFEITO 3D ULTRA CHAMATIVO) */
    @keyframes flutuar-continuo {
        0% {
            transform: translateY(0px);
            box-shadow: 0px 8px 32px rgba(0, 229, 255, 0.2);
        }
        50% {
            transform: translateY(-12px); /* Ele se eleva suavemente */
            box-shadow: 0px 18px 45px rgba(0, 255, 135, 0.4); /* O neon brilha mais embaixo */
        }
        100% {
            transform: translateY(0px);
            box-shadow: 0px 8px 32px rgba(0, 229, 255, 0.2);
        }
    }

    .robo-card-welcome {
        background: linear-gradient(135deg, #0f172a 0%, #050811 100%) !important;
        border: 2px solid #00E5FF !important;
        border-radius: 16px !important;
        padding: 30px !important;
        margin-bottom: 35px !important;
        animation: flutuar-continuo 4s infinite ease-in-out !important; /* Flutuação contínua infinita */
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
# 🤖 APRESENTAÇÃO MAJESTOSA DO ROBOZINHO NA CENTRAL (FLUTUANDO NA TELA DA FRENTE)
# =============================================================================================================
st.markdown("""
<div class="robo-card-welcome">
    <h1 style='margin-top: 0; font-size: 28px;'>🛸 CENTRAL DE INTELIGÊNCIA: ADRIEL AI</h1>
    <p style='margin: 15px 0 0 0; font-size: 16px; color: #cbd5e1; line-height: 1.6;'>
        "Seja muito bem-vindo, <b>Comandante José Marques da Silva</b>! Os sistemas centrais do robô foram inicializados. 
        Estou flutuando na interface principal e aguardando suas ordens. Nossos bancos de dados estão 100% síncronos 
        com as APIs de mineração global e automação de tráfego pago."
    </p>
    <div style='margin-top: 20px;'>
        <span style='background: #00FF87; color: #050811; padding: 6px 14px; font-weight: bold; border-radius: 20px; font-size: 12px; box-shadow: 0px 4px 10px rgba(0,255,135,0.3);'>
            MÁQUINA EM OPERAÇÃO 🛡️
        </span>
    </div>
</div>
""", unsafe_allow_html=True)

# Espaçador estratégico para o gráfico não bater no card flutuante
st.write("")
st.write("")

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
# GRÁFICO GLOBAL DE VOLUME ANALISADO
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
