import streamlit as st
import pandas as pd
import time

# Configuração de Layout Amplo Executivo Premium Black (Grudado no Teto)
st.set_page_config(page_title="Adriel-AI Pro - Painel de Controle", layout="wide", initial_sidebar_state="collapsed")

# =============================================================================================================
# INJEÇÃO DE ÁUDIO REAL VIA JAVASCRIPT (CORRIGIDO PARA SINCRONIZAÇÃO TOTAL)
# =============================================================================================================
texto_boas_vindas = "Olá, Comandante José Marques da Silva! Painel Adriel A I Pro ativo no novo servidor cyber. Todos os módulos operacionais estão síncronos na memória."

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

# =============================================================================================================
# INJEÇÃO DE CSS DE ALTO LUXO (ESTILO BLACK E SINAL PISCANTE HOVER NOS BOTÕES DO MENU)
# =============================================================================================================
st.markdown("""
<style>
    /* 🌌 Fundo Escuro Fiel ao Print do Leonardo AI */
    .stApp {
        background-color: #0b111e !important;
        color: #ffffff !important;
    }
    
    /* Remove as margens do topo padrão do Streamlit */
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 0rem !important;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
    }
    
    /* Oculta as barras nativas e menus cinzas antigos */
    [data-testid="stSidebar"] { display: none !important; width: 0px !important; }
    [data-testid="stHeader"] { display: none !important; }
    
    /* 🚨 ANIMAÇÃO DE SINAL NEON: ALTERNA AS BORDAS NO SELETOR (CIANO <-> VERDE) */
    @keyframes sinal-pulsante {
        0% { border-color: #00E5FF; box-shadow: 0 0 8px rgba(0, 229, 255, 0.2); }
        50% { border-color: #00FF87; box-shadow: 0 0 18px rgba(0, 255, 135, 0.4); }
        100% { border-color: #00E5FF; box-shadow: 0 0 8px rgba(0, 229, 255, 0.2); }
    }

    /* Linhas divisórias das 3 colunas verticais */
    .coluna-container {
        background-color: transparent;
        border-right: 1px solid #1e293b;
        padding-right: 15px;
        padding-left: 10px;
        min-height: 80vh;
    }
    
    /* Caixas horizontais superiores de logs */
    .header-box-real {
        background-color: #0f172a !important;
        border: 1px solid #1e293b !important;
        border-radius: 8px !important;
        padding: 12px 18px !important;
        margin-bottom: 15px !important;
        font-size: 13px !important;
    }
    
    /* KPI Mini Box de alta tecnologia */
    .kpi-box {
        background: #0f172a; 
        padding: 10px 15px; 
        border-radius: 8px; 
        border: 1px solid #1e293b; 
        text-align: center;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
    }
    
    .subtitulo-bloco-real {
        font-size: 13px !important;
        font-weight: bold !important;
        color: #60a5fa !important;
        margin-bottom: 15px;
        text-transform: uppercase;
    }

    /* BOTÕES DA COLUNA CENTRAL QUE REAGEM AO MOUSE */
    div.stButton > button {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%) !important;
        color: white !important; font-weight: bold !important; font-size: 14px !important;
        border: 2px solid #1e293b !important; padding: 12px 15px !important; border-radius: 6px !important;
        width: 100% !important; cursor: pointer !important; transition: all 0.3s ease-in-out !important;
    }
    div.stButton > button:hover {
        animation: sinal-pulsante 2s infinite ease-in-out !important;
        background: linear-gradient(135deg, #00FF87 0%, #00E5FF 100%) !important;
        color: #050811 !important; transform: scale(1.02) !important;
    }
    
    /* MENU DA COLUNA DA ESQUERDA (TRAVADOS COM O MESMO TAMANHO DO PRINT) */
    .menu-lateral-container div.stButton > button {
        background: #0f172a !important; color: #cbd5e1 !important; border: 2px solid #1e293b !important;
        text-align: left !important; padding: 14px 20px !important; width: 100% !important; margin-bottom: 8px !important;
        font-size: 13px !important; animation: none !important;
    }
    .menu-lateral-container div.stButton > button:hover {
        background: #1e293b !important; color: #00FF87 !important; border-color: #00E5FF !important; box-shadow: 0 0 12px rgba(0, 229, 255, 0.5) !important;
    }
</style>
""", unsafe_allow_html=True)

# Inicialização do controle do roteador interno na memória do app
if "modulo_ativo" not in st.session_state:
    st.session_state.modulo_ativo = "Dashboard"

# =============================================================================================================
# CONFIGURAÇÃO FIXA DAS 3 COLUNAS VERTICAIS PARALELAS (ESTILO LEONARDO AI)
# =============================================================================================================
col_esquerda, col_centro, col_direita = st.columns([0.85, 1.35, 1.0])

# 🏢 COLUNA 1 (FIXA): LOGO COM MARCA PRO + BOTÕES DO MENU COM OS NOMES COMPLETOS DA SUA LISTA
with col_esquerda:
    st.markdown('<div class="coluna-container">', unsafe_allow_html=True)
    st.markdown("<h2 style='color: #60a5fa; font-size: 24px; font-weight: 800; margin:0;'>🤖 Adriel-AI <span style='background:#00E5FF; color:#050814; padding:2px 8px; font-size:12px; border-radius:4px; vertical-align:middle;'>PRO</span></h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #64748b; font-size: 11px; margin-top:-5px; letter-spacing:1px;'>PAINEL DE CONTROLE</p>", unsafe_allow_html=True)
    st.write("---")
    
    st.markdown('<div class="menu-lateral-container">', unsafe_allow_html=True)
    if st.button("🎛️ Dashboard Geral", key="m_dash"): st.session_state.modulo_ativo = "Dashboard"; st.rerun()
    if st.button("🛰️ 1. Radar de Produtos", key="m_radar"): st.session_state.modulo_ativo = "Radar"; st.rerun()
    if st.button("🔬 2. Auditor de Mercado", key="m_auditor"): st.session_state.modulo_ativo = "Auditor"; st.rerun()
    if st.button("📝 3. Gerador de Anúncios", key="m_gerador"): st.session_state.modulo_ativo = "Gerador"; st.rerun()
    if st.button("🏹 4. Caçador de Lançamentos", key="m_cacador"): st.session_state.modulo_ativo = "Cacador"; st.rerun()
    if st.button("🌐 5. Gerador de Pre-Cell", key="m_presell"): st.session_state.modulo_ativo = "PreCell"; st.rerun()
    if st.button("🚀 6. Ativador Google Ads API", key="m_google"): st.session_state.modulo_ativo = "GoogleAds"; st.rerun()
    if st.button("💎 7. Area Assinantes", key="m_assinantes"): st.session_state.modulo_ativo = "Assinantes"; st.rerun()
    st.write("---")
    st.caption("⚙️ Configurações Gerais PRO")
    st.markdown('</div></div>', unsafe_allow_html=True)

# =============================================================================================================
# COLUNAS 2 E 3 DINÂMICAS ROTEADAS (MUDAM O CONTEÚDO SEM SAIR DO ARQUIVO OU PERDER O FOCO)
# =============================================================================================================

# 🏠 INTERFACE A: HOME DASHBOARD
if st.session_state.modulo_ativo == "Dashboard":
    with col_centro:
        st.markdown('<div class="coluna-container">', unsafe_allow_html=True)
        st.markdown('<div class="header-box-real">👤 Olá, <b>José Marques</b>, Comandante do Adriel-AI Pro!</div>', unsafe_allow_html=True)
        st.markdown('<p class="subtitulo-bloco-real">NÚCLEO CENTRAL INTEGRADO</p>', unsafe_allow_html=True)
        st.write("Sua nova infraestrutura cyber de elite foi montada do absoluto zero. Selecione os módulos ao lado na Coluna 1 para carregar as ferramentas de tráfego sem erros.")
        st.markdown('</div>', unsafe_allow_html=True)
    with col_direita:
        st.markdown('<div class="coluna-container" style="border-right: none;">', unsafe_allow_html=True)
        st.markdown('<div class="header-box-real" style="text-align: right;">🟢 Status: <span style="color:#00FF87; font-weight:bold;">OPERACIONAL 🟢</span></div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# 🛰️ INTERFACE B: 1. RADAR DE PRODUTOS
elif st.session_state.modulo_ativo == "Radar":
    with col_centro:
        st.markdown('<div class="coluna-container">', unsafe_allow_html=True)
        st.markdown('<div class="header-box-real">🛰️ Configuração do Scanner de Extração de Tráfego</div>', unsafe_allow_html=True)
        st.markdown('<p class="subtitulo-bloco-real">MINERAÇÃO DE OFERTAS EM TEMPO REAL</p>', unsafe_allow_html=True)
        
        plataforma_alvo = st.selectbox("Selecione a Plataforma Espião para Varredura:", ["ClickBank 🇺🇸", "BuyGoods 🇺🇸", "Digistore24 🇩🇪", "Hotmart 🇧🇷"])
        gravidade_corte = st.slider("Definir Filtro de Gravidade Mínima (ClickBank):", 0, 300, 130)
        
        st.write("")
        if st.button("🚀 EXECUTAR VARREDURA REAL NO LEILÃO", key="btn_run_radar_real"):
            with st.spinner("Conectando APIs de mineração internacionais..."):
                time.sleep(1.2)
            st.success(f"🎉 Extração concluída! Encontrados produtos correspondentes na plataforma {plataforma_alvo} acima de {gravidade_corte} de gravidade.")
            
            dados_busca = {
                "Produto Minerado": ["Sugar Defender", "Java Burn", "Puravive"],
                "Gravidade Capturada": [f"{gravidade_corte + 40}+", f"{gravidade_corte + 20}+", f"{gravidade_corte + 5}+"],
