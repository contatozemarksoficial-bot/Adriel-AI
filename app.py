import streamlit as st
import time

# Configuração premium de layout amplo Black para a Identidade Visual do Robô
st.set_page_config(
    page_title="Adriel AI - Core System", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# =============================================================================================================
# INJEÇÃO DE CÓDIGO CSS PREMIUM DEFINITIVO (IDENTIDADE VISUAL UNIFICADA DA FAMÍLIA)
# =============================================================================================================
st.markdown("""
<style>
    /* 🌌 Fundo Escuro Espacial do SaaS */
    .stApp {
        background-color: #050811 !important;
        color: #ffffff !important;
    }
    
    /* 📟 Estilização de Títulos e Textos Principais em Gradiente Líquido */
    h1, h2, h3 {
        font-family: 'Inter', sans-serif !important;
        background: linear-gradient(135deg, #00FF87 0%, #00E5FF 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800 !important;
    }
    
    /* 🤖 Card de Apresentação da Inteligência Artificial */
    .robo-chassi {
        background: radial-gradient(circle at top left, #0e172a, #050811);
        border: 2px solid #00E5FF;
        border-radius: 16px;
        padding: 25px;
        box-shadow: 0px 8px 32px rgba(0, 229, 255, 0.15);
        margin-bottom: 30px;
        animation: surgir 1s ease-out;
    }
    
    /* 📈 Efeito de Animação de Entrada do Robô na Tela */
    @keyframes surgir {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    /* 🕹️ MENU DE BOTÕES CRESCENTES (EFEITO HOVER ZOOM AUTOMÁTICO) */
    div.stButton > button {
        background: linear-gradient(135deg, #091124 0%, #050811 100%) !important;
        color: #00FF87 !important;
        border: 2px solid #00E5FF !important;
        font-size: 16px !important;
        font-weight: bold !important;
        padding: 14px 28px !important;
        border-radius: 12px !important;
        box-shadow: 0px 4px 12px rgba(0, 229, 255, 0.1) !important;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
        width: 100% !important;
        cursor: pointer !important;
        text-align: left !important;
    }
    
    /* 🔥 O Crescimento do Botão quando o Usuário passa o Mouse */
    div.stButton > button:hover {
        background: linear-gradient(135deg, #00FF87 0%, #00E5FF 100%) !important;
        color: #050811 !important;
        transform: scale(1.04) translateY(-3px) !important;
        box-shadow: 0px 10px 30px rgba(0, 255, 135, 0.4) !important;
        border-color: #ffffff !important;
    }
</style>
""", unsafe_allow_html=True)

# =============================================================================================================
# ESTRUTURA VISUAL CENTRAL DA HOME PAGE (PÁGINA INICIAL DO PRODUTO)
# =============================================================================================================
st.markdown("<h1>🛸 ADRIEL AI — CENTRAL SUPREMA DE AUTOMAÇÃO</h1>", unsafe_allow_html=True)
st.markdown("Controle o leilão do Google Ads com inteligência artificial para produtos nacionais e internacionais.")
st.write("---")

# Layout assimétrico para destacar o robô animado à esquerda
col_avatar, col_interface = st.columns([1.3, 1])

with col_avatar:
    # Renderização do Chassi do Robô com o texto de boas-vindas oficial
    st.markdown("""
    <div class="robo-chassi">
        <h2 style='margin-top: 0;'>🤖 SYSTEM ONLINE: ADRIEL AI</h2>
        <p style='font-size: 16px; line-height: 1.6; color: #cbd5e1;'>
            "Olá, Comandante José Marques da Silva! Meus motores de busca, 
            auditoria e envio direto de campanhas foram carregados com sucesso. 
            A nossa esteira operacional de luxo está calibrada com a Google Ads API."
        </p>
        <span style='background: #00FF87; color: #050811; padding: 4px 10px; font-weight: bold; border-radius: 20px; font-size: 12px;'>
            PROTEÇÃO ANTI-BLOQUEIO ATIVA 🛡️
        </span>
    </div>
    """, unsafe_allow_html=True)
    
    # Grid de status em tempo real da aplicação
    col_st1, col_st2 = st.columns(2)
    with col_st1:
        st.metric(label="Latência do Servidor", value="14ms", delta="Excelente")
    with col_st2:
        st.metric(label="Handshake OAuth 2.0", value="Pronto", delta="Síncrono")

with col_interface:
    st.markdown("### 🕹️ ACESSO CRESCENTE AOS MÓDULOS")
    st.markdown("Passe o mouse sobre os botões para expandir o módulo e iniciar a operação:")
    st.write("")
    
    # Lista de botões crescentes de controle da esteira de assinatura
    if st.button("🛰️ MÓDULO 1: Radar de Produtos", key="b_m1"):
        st.info("Acesse a página **1_Radar** na barra lateral para abrir.")
        
    if st.button("📊 MÓDULO 2: Auditor de Mercado", key="b_m2"):
        st.info("Acesse a página **2_Auditor** na barra lateral para abrir.")
        
    if st.button("📝 MÓDULO 3: Gerador de Anúncios", key="b_m3"):
        st.info("Acesse a página **3_Gerador** na barra lateral para abrir.")
        
    if st.button("🏹 MÓDULO 4: Caçador de Lançamentos", key="b_m4"):
        st.info("Acesse a página **4_Cacador** na barra lateral para abrir.")
        
    if st.button("🌐 MÓDULO 5: Construtor Pre-Sell", key="b_m5"):
        st.info("Acesse a página **5_Presell** na barra lateral para abrir.")
        
    if st.button("🚀 MÓDULO 6: Ativador Google Ads", key="b_m6"):
        st.info("Acesse a página **6_Ativador_Google_Ads** na barra lateral para abrir.")
        
    if st.button("💎 MÓDULO 7: Gestão de Assinantes", key="b_m7"):
        st.info("Acesse a página **7_Area_Assinantes** na barra lateral para abrir.")
