import streamlit as st

# Configuração premium de layout amplo para a entrada do SaaS PRO
st.set_page_config(page_title="Adriel-AI Pro - Core Dashboard", layout="wide", initial_sidebar_state="expanded")

# INJEÇÃO DE ÁUDIO REAL VIA JAVASCRIPT (O ROBÔ PRO FALA AO ENTRAR NA HOME)
texto_boas_vindas = "Olá, Comandante José Marques da Silva! O núcleo de Inteligência Artificial tridimensional está ativo nos servidores do Adriel A I Pro. Selecione os módulos numerados na barra lateral."

st.markdown(f"""
<script>
    document.addEventListener('click', function() {{
        if (!window.audioDisparado) {{
            var msg = new SpeechSynthesisUtterance();
            msg.text = "{texto_boas_vindas}";
            msg.lang = "pt-BR";
            msg.rate = 1.0;
            msg.pitch = 0.92;
            window.speechSynthesis.speak(msg);
            window.audioDisparado = true;
        }}
    }});
</script>
""", unsafe_allow_html=True)

# INJEÇÃO DE CSS DE ALTO LUXO (ESTILO BLACK E LINKS NATIVOS DA BARRA LATERAL DA REGRA PAGES)
st.markdown("""
<style>
    /* 🌌 Fundo Escuro Fiel ao Print do Leonardo AI */
    .stApp { background-color: #0b111e !important; color: #ffffff !important; }
    .block-container { padding-top: 1rem !important; padding-bottom: 0rem !important; }
    
    /* Oculta o cabeçalho padrão feio do Streamlit */
    [data-testid="stHeader"] { display: none !important; }
    
    /* 🚨 ANIMAÇÃO DE SINAL NEON QUE PISCA NOS LINKS DA LATERAL AUTOMATICAMENTE */
    @keyframes sinal-pulsante {
        0% { border-color: #1e293b; box-shadow: 0 0 5px rgba(0, 229, 255, 0.1); }
        50% { border-color: #00FF87; box-shadow: 0 0 15px rgba(0, 255, 135, 0.4); }
        100% { border-color: #1e293b; box-shadow: 0 0 5px rgba(0, 229, 255, 0.1); }
    }
    
    /* Customização dos links nativos da barra lateral da regra pages */
    [data-testid="stSidebarNav"] ul li a span { color: #ffffff !important; font-weight: bold !important; font-size: 14px !important; }
    [data-testid="stSidebarNav"] ul li a {
        background-color: #0f172a !important; border: 2px solid #1e293b !important; border-radius: 8px !important;
        margin-bottom: 8px !important; padding: 12px 14px !important; animation: sinal-pulsante 3s infinite ease-in-out !important;
    }
    
    /* Caixas personalizadas centrais */
    .header-box-real { background-color: #0f172a !important; border: 1px solid #1e293b !important; border-radius: 8px !important; padding: 14px 20px !important; margin-bottom: 15px !important; }
    .kpi-box { background: #0f172a; padding: 12px 15px; border-radius: 8px; border: 1px solid #1e293b; text-align: center; }
</style>
""", unsafe_allow_html=True)

# Título de Identificação Superior da Central Master
st.markdown("<h2 style='color: #60a5fa; font-size: 26px; font-weight: 800; margin-bottom:0;'>🤖 Adriel-AI <span style='background:#00E5FF; color:#050814; padding:2px 8px; font-size:12px; border-radius:4px; vertical-align:middle;'>PRO</span></h2>", unsafe_allow_html=True)
st.markdown("<p style='color: #64748b; font-size: 11px; margin-top:-5px; letter-spacing:1px;'>SaaS PLATFORM MASTER • DASHBOARD GERAL</p>", unsafe_allow_html=True)
st.write("---")

# Interface do Painel Central Geral em 2 Colunas Paralelas Livres
col_centro, col_direita = st.columns([1.4, 1.0])

with col_centro:
    st.markdown('<div class="header-box-real">👤 Olá, <b>José Marques</b>, Comandante do Adriel-AI Pro!</div>', unsafe_allow_html=True)
    st.write("### 🎛️ CENTRAL OPERACIONAL DE TRÁFEGO")
    st.write("Sua nova infraestrutura modular baseada em subpáginas nativas está ativa. Use o menu lateral esquerdo expandido e numerado para alternar de forma síncrona entre os recursos de mineração.")
    
with col_direita:
    st.markdown('<div class="header-box-real" style="text-align: right;">🟢 Licença PRO: <span style="color:#00FF87; font-weight:bold;">Ativa e Vitalícia</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="kpi-box"><span style="font-size:11px;color:#64748b;font-weight:bold;">🔥 STATUS DO SERVIDOR</span><br><span style="font-size:20px;color:#00FF87;font-weight:800;">TOTALMENTE ONLINE 🟢</span></div>', unsafe_allow_html=True)

# Rodapé institucional unificado da família (Sempre idêntico!)
st.markdown('<div style="clear: both; text-align: center; font-size: 11px; color: #475569; padding-top: 45px;"><hr style="border-color: #1e293b;">© 2026 Adriel-AI Pro - Todos os Direitos Reservados.</div>', unsafe_allow_html=True)
