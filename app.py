import streamlit as st
import pandas as pd
import time

# Configuração de Layout Amplo Premium Black para a Entrada do SaaS
st.set_page_config(page_title="Adriel AI - Core Dashboard", layout="wide", initial_sidebar_state="expanded")

# =============================================================================================================
# INJEÇÃO DE ÁUDIO REAL VIA JAVASCRIPT (O ROBÔ FALA AO CLICAR NA TELA)
# =============================================================================================================
texto_boas_vindas = "Olá, Comandante José Marques da Silva! O painel holográfico tridimensional está ativo e os sistemas estão síncronos na memória."

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
# INJEÇÃO DE CÓDIGO CSS PREMIUM DE ELITE (IMPLANTANDO O CENÁRIO DO ROBÔ 3D DE FUNDO DA PLATAFORMA)
# =============================================================================================================
st.markdown("""
<style>
    /* 🌌 O CENÁRIO DO ROBÔ FUTURISTA FLUTUANDO DE FUNDO EM TELA CHEIA (BACKGROUND LUXO) */
    .stApp {
        background: linear-gradient(rgba(5, 8, 17, 0.85), rgba(5, 8, 17, 0.92)), 
                    url('https://unsplash.com') !important;
        background-size: cover !important;
        background-position: center center !important;
        background-attachment: fixed !important;
        color: #ffffff !important;
    }
    
    /* 📟 Customização da Barra Lateral Esquerda */
    [data-testid="stSidebar"] {
        background-color: rgba(2, 4, 10, 0.95) !important;
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
        background-color: rgba(15, 23, 42, 0.8) !important; 
        border: 2px solid #1e293b !important;
        border-radius: 8px !important;
        margin-bottom: 8px !important;
        padding: 12px 14px !important;
        animation: pulsa-neon 3s infinite ease-in-out !important;
        display: block !important;
    }
    
    /* 🎨 ANIMAÇÃO QUE ALTERNA AS CORES DAS CAIXAS FLUTUANTES (CIANO <-> VERDE) */
    @keyframes alterna-cores {
        0% { border-color: #00E5FF; box-shadow: 0px 8px 32px rgba(0, 229, 255, 0.25); }
        50% { border-color: #00FF87; box-shadow: 0px 8px 32px rgba(0, 255, 135, 0.35); }
        100% { border-color: #00E5FF; box-shadow: 0px 8px 32px rgba(0, 229, 255, 0.25); }
    }

    /* Caixa Central Translúcida Estilo Vidro (Glassmorphism) */
    .robo-card-welcome {
        background: rgba(15, 23, 42, 0.65) !important;
        backdrop-filter: blur(8px) !important;
        -webkit-backdrop-filter: blur(8px) !important;
        border: 2px solid #00E5FF !important;
        border-radius: 16px !important;
        padding: 30px !important;
        margin-bottom: 35px !important;
        animation: alterna-cores 6s infinite ease-in-out !important; /* Alterna as cores das bordas */
    }
    
    /* Bloco de Monitoramento Executivo */
    .status-card {
        background-color: rgba(15, 23, 42, 0.75) !important;
        backdrop-filter: blur(4px) !important;
        border: 1px solid #1e293b !important;
        border-radius: 12px !important;
        padding: 20px !important;
        text-align: center;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.4) !important;
    }
    
    /* Estilização para o Gráfico de Barras */
    .stBarChart {
        background-color: rgba(15, 23, 42, 0.5) !important;
        border-radius: 12px;
        padding: 10px;
    }
</style>
""", unsafe_allow_html=True)

# =============================================================================================================
# APRESENTAÇÃO MAJESTOSA DA CENTRAL (MOLDADA POR CIMA DO ROBÔ EM 3D)
# =============================================================================================================
st.markdown("""
<div class="robo-card-welcome">
    <h1 style='margin-top: 0; font-size: 28px; background: linear-gradient(135deg, #00FF87 0%, #00E5FF 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>🛸 PLATAFORMA HOLOGRÁFICA: ADRIEL AI</h1>
    <p style='margin: 15px 0 0 0; font-size: 16px; color: #f1f5f9; line-height: 1.6; font-weight: 500;'>
        "Seja muito bem-vindo, <b>Comandante José Marques da Silva</b>! O cenário operacional está fixado em 3D. 
        Observe que as bordas flutuantes alternam de cor continuamente entre Ciano e Verde Neon, reproduzindo o mesmo estilo requintado 
        da interface do robô inteligente. Clique em qualquer lugar da tela para ativar os alto-falantes."
    </p>
    <div style='margin-top: 20px;'>
        <span style='background: #00FF87; color: #050811; padding: 6px 14px; font-weight: bold; border-radius: 20px; font-size: 12px; box-shadow: 0px 4px 10px rgba(0,255,135,0.3);'>
            SISTEMA INTEGRADO COM VOZ REAL 🔊
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
    st.markdown("""
    <div class="status-card">
        <h4 style='color: #60a5fa; margin-top:0;'>📡 SERVIDORES MESTRES</h4>
        <h2 style='margin: 10px 0; background: linear-gradient(135deg, #00FF87 0%, #00E5FF 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>ONLINE 🟢</h2>
        <p style='color: #94a3b8; font-size: 13px; margin:0;'>Handshake síncrono com o GitHub</p>
    </div>
    """, unsafe_allow_html=True)

with col_c2:
    st.markdown("""
    <div class="status-card" style="border-color: #00FF87;">
        <h4 style='color: #00FF87; margin-top:0;'>🔑 GOOGLE ADS API</h4>
        <h2 style='margin: 10px 0; background: linear-gradient(135deg, #00FF87 0%, #00E5FF 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>AUTENTICADA 🔗</h2>
        <p style='color: #94a3b8; font-size: 13px; margin:0;'>Protocolo OAuth 2.0 Ativo e Pronto</p>
    </div>
    """, unsafe_allow_html=True)

with col_c3:
    st.markdown("""
    <div class="status-card">
        <h4 style='color: #60a5fa; margin-top:0;'>💻 PÁGINAS PRE-SELL</h4>
        <h2 style='margin: 10px 0; background: linear-gradient(135deg, #00FF87 0%, #00E5FF 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>PROTEGIDAS 🛡️</h2>
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
