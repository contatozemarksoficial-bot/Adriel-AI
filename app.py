import streamlit as st
import time

# Configuração de layout amplo e profissional Black de Alta Tecnologia
st.set_page_config(page_title="Adriel AI - Painel de Controle", layout="wide")

# INJEÇÃO DE CÓDIGO CSS PREMIUM DE ELITE (BOTÕES NEON E ANIMAÇÕES)
st.markdown("""
<style>
    /* Estilização dos Botões de Navegação Crescente */
    .stButton > button {
        background: linear-gradient(135deg, #007BFF 0%, #00E5FF 100%) !important;
        color: white !important;
        font-size: 16px !important;
        font-weight: bold !important;
        padding: 15px 40px !important;
        border-radius: 12px !important;
        border: none !important;
        box-shadow: 0px 4px 15px rgba(0, 229, 255, 0.3) !important;
        transition: all 0.3s ease-in-out !important;
        width: 100% !important;
        margin-bottom: 10px;
    }
    .stButton > button:hover {
        background: linear-gradient(135deg, #00FF87 0%, #60EFFF 100%) !important;
        color: #121212 !important;
        transform: scale(1.02) translateY(-2px) !important;
        box-shadow: 0px 6px 20px rgba(0, 255, 135, 0.6) !important;
    }
    /* Estilo do Card do Robô */
    .robo-card {
        background: #1e1e24;
        border-left: 5px solid #00FF87;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
    }
</style>
""", unsafe_allow_html=True)

# 🤖 ANIMAÇÃO DO ROBÔ SURGINDO NA TELA (Simulação Inteligente)
with st.spinner("🤖 Inicializando inteligência do Robô Adriel AI..."):
    time.sleep(0.8)

# Cabeçalho de Impacto
st.title("🛰️ ADRIEL AI — ECOSSISTEMA AUTOMATIZADO DE ELITE")
st.markdown("Bem-vindo ao centro de comando. Seu robô está online e pronto para escanear, auditar e disparar campanhas.")
st.write("---")

# Layout de duas colunas: Robô Chegando na Tela vs Menu Crescente de Botões
col_robo, col_menu = st.columns([1.2, 1])

with col_robo:
    st.markdown("""
    <div class="robo-card">
        <h2 style='color: #00FF87; margin-top:0;'>🤖 STATUS: ADRIEL AI EM OPERAÇÃO</h2>
        <p style='font-size: 15px; color: #e0e0e0;'>
            "Olá, Comandante José! Todas as minhas diretrizes de auditoria contra suspensões, 
            criação de Pre-sells blindadas e conexão real-time com a API do Google Ads estão carregadas na memória ativa."
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    # Métricas rápidas de performance do SaaS
    st.metric(label="🟢 Filtro Editorial Anti-Bloqueio", value="100% Ativo")
    st.metric(label="⚡ Conectividade Google Ads API", value="Pronto para Handshake")

with col_menu:
    st.markdown("### 🕹️ MENU CRESCENTE DE COMANDO")
    st.markdown("Navegue pela esteira de produção utilizando os atalhos sequenciais abaixo ou use a barra lateral:")
    
    # Botões sequenciais crescentes que levam o usuário na ordem correta
    if st.button("🛰️ 1. Abrir Radar de Produtos"):
        st.info("Utilize a barra lateral esquerda para acessar a página: **1_Radar**")
        
    if st.button("🔍 2. Acessar Auditor de Mercado"):
        st.info("Utilize a barra lateral esquerda para acessar a página: **2_Auditor**")
        
    if st.button("📝 3. Ir para o Gerador de Criativos"):
        st.info("Utilize a barra lateral esquerda para acessar a página: **3_Gerador**")
        
    if st.button("🏹 4. Ativar Caçador de Lançamentos"):
        st.info("Utilize a barra lateral esquerda para acessar a página: **4_Cacador**")
        
    if st.button("🌐 5. Construir Página Pre-sell"):
        st.info("Utilize a barra lateral esquerda para acessar a página: **5_Presell**")
        
    if st.button("🚀 6. Disparar Construtor Google Ads"):
        st.info("Utilize a barra lateral esquerda para acessar a página: **6_Ativador_Google_Ads**")
