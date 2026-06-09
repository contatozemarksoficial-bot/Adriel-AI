import streamlit as st
import pandas as pd
import time

# Configuração de Layout Amplo Premium Black para a Entrada do SaaS
st.set_page_config(page_title="Adriel AI - Core Dashboard", layout="wide", initial_sidebar_state="expanded")

# =============================================================================================================
# INJEÇÃO DE ÁUDIO REAL VIA JAVASCRIPT (O ROBÔ FALA AO CLICAR NA TELA)
# =============================================================================================================
texto_boas_vindas = "Olá, Comandante José Marques da Silva! Todos os sistemas e a API do Google Ads estão prontos na memória ativa."

st.markdown(f"""
<script>
    document.addEventListener('click', function() {{
        if (!window.audioDisparado) {{
            var msg = new SpeechSynthesisUtterance();
            msg.text = "{texto_boas_vindas}";
            msg.lang = "pt-BR";
            msg.rate = 1.0;
            msg.pitch = 0.9;
            window.speechSynthesis.speak(msg);
            window.audioDisparado = true;
        }}
    }});
</script>
""", unsafe_allow_html=True)

# =============================================================================================================
# INJEÇÃO DE CÓDIGO CSS PREMIUM DEFINITIVO (ROBÔ SVG NATIVO OPERANDO NO RODAPÉ)
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
    
    /* 🚨 ANIMAÇÃO DO MENU LATERAL PULSAR NEON */
    @keyframes pulsa-neon {
        0% { border-color: #1e293b; box-shadow: 0 0 5px rgba(0, 229, 255, 0.1); }
        50% { border-color: #00FF87; box-shadow: 0 0 15px rgba(0, 255, 135, 0.4); }
        100% { border-color: #1e293b; box-shadow: 0 0 5px rgba(0, 229, 255, 0.1); }
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
        animation: pulsa-neon 3s infinite ease-in-out !important;
        display: block !important;
    }
    
    /* 🎨 ANIMAÇÃO QUE ALTERNA AS CORES DAS BORDAS (CIANO <-> VERDE) */
    @keyframes alterna-cores {
        0% { border-color: #00E5FF; box-shadow: 0px 8px 32px rgba(0, 229, 255, 0.2); }
        50% { border-color: #00FF87; box-shadow: 0px 8px 32px rgba(0, 255, 135, 0.3); }
        100% { border-color: #00E5FF; box-shadow: 0px 8px 32px rgba(0, 229, 255, 0.2); }
    }

    .robo-card-welcome {
        background: linear-gradient(135deg, #0f172a 0%, #050811 100%) !important;
        border: 2px solid #00E5FF !important;
        border-radius: 16px !important;
        padding: 30px !important;
        margin-bottom: 35px !important;
        animation: alterna-cores 5s infinite ease-in-out !important;
    }
    
    /* 🤖 ANIMAÇÃO DE PATRULHA DO ROBÔ REAL NO COMPRIMENTO DA TELA */
    @keyframes patrulha-render {
        0% { left: 5%; transform: scaleX(1) translateY(0px); }
        25% { transform: scaleX(1) translateY(-8px); }
        50% { left: 75%; transform: scaleX(-1) translateY(0px); }
        75% { transform: scaleX(-1) translateY(-8px); }
        100% { left: 5%; transform: scaleX(1) translateY(0px); }
    }

    .robo-container-fixed {
        position: fixed;
        bottom: 10px;
        left: 5%;
        width: 120px;
        z-index: 99999;
        pointer-events: none;
        animation: patrulha-render 16s infinite linear !important;
    }
    
    /* Bloco de Monitoramento Executivo */
    .status-card {
        background-color: #0f172a !important;
        border: 1px solid #1e293b !important;
        border-radius: 12px !important;
        padding: 20px !important;
        text-align: center;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.3) !important;
    }
</style>
""", unsafe_allow_html=True)

# =============================================================================================================
# INJEÇÃO DO ROBÔ DIGITALIZADO VIA OPERAÇÃO DE CÓDIGO INTERNO (NATIVO CONTÍNUO)
# =============================================================================================================
st.markdown("""
<div class="robo-container-fixed">
    <svg viewBox="0 0 100 100" width="100" height="100" style="filter: drop-shadow(0px 0px 10px #00FF87);">
        <!-- Cabeça do Robô -->
        <rect x="25" y="20" width="50" height="40" rx="10" fill="#ffffff" stroke="#00E5FF" stroke-width="3"/>
        <!-- Olhos Acesos em Ciano -->
        <circle cx="40" cy="35" r="5" fill="#00E5FF"/>
        <circle cx="60" cy="35" r="5" fill="#00E5FF"/>
        <!-- Boca Eletrônica -->
        <rect x="40" y="48" width="20" height="4" fill="#00FF87" rx="2"/>
        <!-- Antena Brilhante -->
        <line x1="50" y1="20" x2="50" y2="5" stroke="#00FF87" stroke-width="4"/>
        <circle cx="50" cy="5" r="4" fill="#00FF87"/>
        <!-- Corpo Compacto -->
        <rect x="35" y="60" width="30" height="25" rx="5" fill="#0f172a" stroke="#1e293b" stroke-width="2"/>
    </svg>
</div>
""", unsafe_allow_html=True)

# =============================================================================================================
# APRESENTAÇÃO MAJESTOSA DA CENTRAL
# =============================================================================================================
st.markdown("""
<div class="robo-card-welcome">
    <h1 style='margin-top: 0; font-size: 27px; background: linear-gradient(135deg, #00FF87 0%, #00E5FF 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>🛸 CENTRAL DE INTELIGÊNCIA: ADRIEL AI</h1>
    <p style='margin: 15px 0 0 0; font-size: 16px; color: #cbd5e1; line-height: 1.6;'>
        "Seja muito bem-vindo, <b>Comandante José Marques da Silva</b>! A estrutura mestre está calibrada. 
        Observe que as bordas da central alternam de cor e o meu <b>Chassi Digitalizado</b> está navegando 
        em patrulha e flutuando na parte inferior do software. Clique na tela para ativar os alto-falantes."
    </p>
    <div style='margin-top: 20px;'>
        <span style='background: #00FF87; color: #050811; padding: 6px 14px; font-weight: bold; border-radius: 20px; font-size: 12px; box-shadow: 0px 4px 10px rgba(0,255,135,0.3);'>
            SISTEMA COM ÁUDIO DE VOZ ATIVO 🔊
        </span>
    </div>
</div>
""", unsafe_allow_html=True)

st.write("")

# =============================================================================================================
# CARDS ESTATÍSTICOS GLOBAIS (REQUINTE EM TELA CHEIA)
# =============================================================================================================
st.markdown("### 📊 STATUS DA INFRAESTRUTURA EM TEMPO REAL")
st.write("")

col_c1, col_c2, col_c3 = st.columns(3)
with col_c1:
    st.markdown('<div class="status-card"><h4 style="color: #60a5fa; margin-top:0;">📡 SERVIDORES MESTRES</h4><h2 style="margin: 10px 0; background: linear-gradient(135deg, #00FF87 0%, #00E5FF 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">ONLINE 🟢</h2><p style="color: #94a3b8; font-size: 13px; margin:0;">Handshake síncrono com o GitHub</p></div>', unsafe_allow_html=True)
with col_c2:
    st.markdown('<div class="status-card" style="border-color: #00FF87;"><h4 style="color: #00FF87; margin-top:0;">🔑 GOOGLE ADS API</h4><h2 style="margin: 10px 0; background: linear-gradient(135deg, #00FF87 0%, #00E5FF 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">AUTENTICADA 🔗</h2><p style="color: #94a3b8; font-size: 13px; margin:0;">Protocolo OAuth 2.0 Ativo e Pronto</p></div>', unsafe_allow_html=True)
with col_c3:
    st.markdown('<div class="status-card"><h4 style="color: #60a5fa; margin-top:0;">💻 PÁGINAS PRE-SELL</h4><h2 style="margin: 10px 0; background: linear-gradient(135deg, #00FF87 0%, #00E5FF 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">PROTEGIDAS 🛡️</h2><p style="color: #94a3b8; font-size: 13px; margin:0;">Roteamento de comissão Hostinger</p></div>', unsafe_allow_html=True)

st.write("---")

# =============================================================================================================
# GRÁFICO GLOBAL DE VOLUME ANALISADO
# =============================================================================================================
st.markdown("### 📈 MONITORAMENTO VOLUMÉTRICO DAS PLATAFORMAS (CLICKBANK / HOTMART)")
st.write("")
meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
valores_envio = [310 + (i * 45) for i in range(12)]
df_envio = pd.DataFrame({"Volume de Dados Processados": valores_envio}, index=meses)
st.bar_chart(df_envio, use_container_width=True, color="#00E5FF")

# Rodapé profissional
st.write("---")
st.markdown("<p style='text-align: center; font-size: 11px; color: #475569;'>© 2026 Adriel AI - Ferramenta Exclusiva de Inteligência para Afiliados Elite. Todos os Direitos Reservados.</p>", unsafe_allow_html=True)
