import streamlit as st
import pandas as pd
import time

# Configuração de Layout Amplo Premium Black para a Entrada do SaaS
st.set_page_config(page_title="Adriel AI - Core Dashboard", layout="wide", initial_sidebar_state="expanded")

# =============================================================================================================
# INJEÇÃO DE ÁUDIO REAL VIA JAVASCRIPT (O ROBÔ FALA AO CLICAR NA TELA)
# =============================================================================================================
texto_boas_vindas = "Olá, Comandante José Marques da Silva! Painel holográfico tridimensional ativado. Motores e chassi síncronos na memória."

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
# INJEÇÃO DE CÓDIGO CSS PREMIUM DEFINITIVO (ANIMAÇÕES DOS ANÉIS HOLOGRÁFICOS E FLUTUAÇÃO)
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
    
    /* 🚨 ANIMAÇÃO PULSAR DO MENU LATERAL */
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
    
    /* 🎨 ANIMAÇÃO DA CAIXA DE BOAS-VINDAS (ALTERNA CIANO <-> VERDE) */
    @keyframes alterna-cores {
        0% { border-color: #00E5FF; box-shadow: 0px 8px 32px rgba(0, 229, 255, 0.2); }
        50% { border-color: #00FF87; box-shadow: 0px 8px 32px rgba(0, 255, 135, 0.3); }
        100% { border-color: #00E5FF; box-shadow: 0px 8px 32px rgba(0, 229, 255, 0.2); }
    }

    .robo-card-welcome {
        background: linear-gradient(135deg, #0f172a 0%, #050811 100%) !important;
        border: 2px solid #00E5FF !important;
        border-radius: 16px !important;
        padding: 25px !important;
        margin-bottom: 25px !important;
        animation: alterna-cores 5s infinite ease-in-out !important;
    }
    
    /* 🔄 ANIMAÇÃO DE ROTAÇÃO DOS FEIXES E PAINÉIS REDONDOS DA FOTO */
    @keyframes girar-holograma {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    @keyframes pulsar-brilho {
        0% { opacity: 0.4; }
        50% { opacity: 1; }
        100% { opacity: 0.4; }
    }

    .anel-rotativo {
        transform-origin: center;
        animation: girar-holograma 20s infinite linear;
    }
    
    .painel-pulsante {
        animation: pulsar-brilho 3s infinite ease-in-out;
    }

    /* Bloco dos Cards de Status */
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
# CLONE OPERACIONAL DA FOTO: O ROBÔ HUMANOIDE COORDENANDO OS PAINÉIS EM CAD-SVG NATIVO
# =============================================================================================================
st.markdown("""
<div style="text-align: center; margin-bottom: 20px;">
    <svg viewBox="0 0 600 240" width="100%" height="240" style="background: transparent;">
        <!-- 🌀 ANÉIS E ARCOS HOLOGRÁFICOS ESQUERDOS (GIRANDO) -->
        <g class="anel-rotativo" style="transform-origin: 120px 120px;">
            <circle cx="120" cy="120" r="50" fill="none" stroke="#00E5FF" stroke-width="2" stroke-dasharray="10, 15" opacity="0.7"/>
            <circle cx="120" cy="120" r="70" fill="none" stroke="#00FF87" stroke-width="1.5" stroke-dasharray="40, 30" opacity="0.5"/>
            <path d="M 60,120 A 60,60 0 0,1 180,120" fill="none" stroke="#00E5FF" stroke-width="4" opacity="0.8"/>
        </g>
        <!-- Painel de Dados Flutuante à Esquerda -->
        <g class="painel-pulsante">
            <rect x="50" y="40" width="80" height="30" rx="5" fill="rgba(0,229,255,0.1)" stroke="#00E5FF" stroke-width="1"/>
            <text x="60" y="60" fill="#00E5FF" font-size="10" font-family="sans-serif" font-weight="bold">AUDIT: OK</text>
            <line x1="120" y1="120" x2="250" y2="100" stroke="#00E5FF" stroke-width="1.5" stroke-dasharray="5,5" opacity="0.6"/>
        </g>

        <!-- 🪐 PAINEL REDONDO DA DIREITA DA FOTO (A ESFERA TECNOLÓGICA) -->
        <g class="anel-rotativo" style="transform-origin: 480px 120px;">
            <circle cx="480" cy="120" r="55" fill="none" stroke="#00E5FF" stroke-width="2" stroke-dasharray="5, 8" opacity="0.8"/>
            <circle cx="480" cy="120" r="40" fill="none" stroke="#00FF87" stroke-width="3" stroke-dasharray="20, 10" opacity="0.6"/>
            <circle cx="480" cy="120" r="20" fill="none" stroke="#00E5FF" stroke-width="1" opacity="0.4"/>
            <!-- Raios do Globo -->
            <line x1="425" y1="120" x2="535" y2="120" stroke="#00E5FF" stroke-width="1" opacity="0.5"/>
            <line x1="480" y1="65" x2="480" y2="175" stroke="#00E5FF" stroke-width="1" opacity="0.5"/>
        </g>
        <g class="painel-pulsante">
            <line x1="480" y1="120" x2="350" y2="100" stroke="#00FF87" stroke-width="1.5" stroke-dasharray="5,5" opacity="0.6"/>
        </g>

        <!-- 🤖 O ROBÔ HUMANOIDE CENTRAL (CORPO, BRAÇOS E MÃOS ACIONANDO OS PAINÉIS) -->
        <g style="transform: translate(220px, 10px);">
            <!-- Cabeça do Robô -->
            <rect x="55" y="20" width="50" height="55" rx="15" fill="#ffffff" stroke="#00E5FF" stroke-width="3"/>
            <!-- Orelhas / Sensores Laterais -->
            <rect x="47" y="35" width="8" height="25" rx="4" fill="#0f172a" stroke="#00E5FF" stroke-width="1.5"/>
            <rect x="105" y="35" width="8" height="25" rx="4" fill="#0f172a" stroke="#00E5FF" stroke-width="1.5"/>
            <!-- Olhos de LED Ciano Acesos -->
            <circle cx="68" cy="42" r="5" fill="#00E5FF"/>
            <circle cx="92" cy="42" r="5" fill="#00E5FF"/>
            <circle cx="68" cy="42" r="1.5" fill="#050811"/>
            <circle cx="92" cy="42" r="1.5" fill="#050811"/>
            <!-- Detalhe da Testa/Neon -->
            <path d="M 65,20 L 80,32 L 95,20" fill="none" stroke="#00FF87" stroke-width="2"/>
            <!-- Boca Eletrônica -->
            <rect x="70" y="58" width="20" height="3" fill="#00FF87" rx="1.5"/>
            
            <!-- Pescoço Articulado -->
            <rect x="70" y="75" width="20" height="12" fill="#334155" stroke="#1e293b"/>
            
            <!-- Torso / Peito Mecânico -->
            <path d="M 40,87 L 120,87 L 110,170 L 50,170 Z" fill="#ffffff" stroke="#00E5FF" stroke-width="2.5"/>
            <!-- Core de Energia Azul no Peito -->
            <rect x="65" y="105" width="30" height="40" rx="6" fill="#0f172a" stroke="#00FF87" stroke-width="2"/>
            <circle cx="80" cy="125" r="8" fill="#00E5FF" class="painel-pulsante"/>

            <!-- 💪 BRAÇO ESQUERDO TOCANDO O PAINEL DE CONEXÃO -->
            <path d="M 40,95 L -10,120 L -60,95" fill="none" stroke="#ffffff" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M 40,95 L -10,120 L -60,95" fill="none" stroke="#0f172a" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
            <!-- Mão tocando o arco holográfico -->
            <circle cx="-60" cy="95" r="8" fill="#00E5FF" class="painel-pulsante"/>

            <!-- 💪 BRAÇO DIREITO OPERANDO A ESFERA -->
            <path d="M 120,95 L 170,120 L 220,95" fill="none" stroke="#ffffff" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M 120,95 L 170,120 L 220,95" fill="none" stroke="#0f172a" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
            <!-- Mão tocando a esfera tecnológica -->
            <circle cx="220" cy="95" r="8" fill="#00FF87" class="painel-pulsante"/>
        </g>
    </svg>
</div>
""", unsafe_allow_html=True)

# =============================================================================================================
# APRESENTAÇÃO MAJESTOSA DA CENTRAL
# =============================================================================================================
st.markdown("""
<div class="robo-card-welcome">
    <h1 style='margin-top: 0; font-size: 28px;'>🛸 INTERFACE HOLOGRÁFICA: ADRIEL AI</h1>
    <p style='margin: 15px 0 0 0; font-size: 16px; color: #cbd5e1; line-height: 1.6;'>
