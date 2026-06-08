import streamlit as st
import time

# Configuração de layout amplo e profissional Black para a Base do SaaS
st.set_page_config(page_title="Adriel AI - Core System", layout="wide")

# INJEÇÃO DO CHASSI DE ESTILO DA FAMÍLIA (BOTÕES CRESCENTES COM SELETOR HOVER)
st.markdown("""
<style>
    /* 📟 Estilização de Títulos Principais em Gradiente Líquido */
    h1, h2, h3 {
        background: linear-gradient(135deg, #00FF87 0%, #00E5FF 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800 !important;
    }
    
    /* 🤖 Card do Chassi do Robô com Animação de Entrada */
    .robo-card-main {
        background: radial-gradient(circle at top left, #0e172a, #050811);
        border: 2px solid #00E5FF;
        border-radius: 16px;
        padding: 25px;
        box-shadow: 0px 8px 32px rgba(0, 229, 255, 0.15);
        margin-bottom: 25px;
        animation: flutuar 1.5s ease-out;
    }
    
    @keyframes flutuar {
        from { opacity: 0; transform: translateY(15px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    /* 🕹️ OS BOTÕES CRESCENTES DA FAMÍLIA (ZOOM HOVER AUTOMÁTICO) */
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
    
    /* 🔥 O efeito onde o botão cresce e acende em verde neon */
    div.stButton > button:hover {
        background: linear-gradient(135deg, #00FF87 0%, #00E5FF 100%) !important;
        color: #050811 !important;
        transform: scale(1.04) translateY(-3px) !important;
        box-shadow: 0px 10px 30px rgba(0, 255, 135, 0.4) !important;
        border-color: #ffffff !important;
    }
</style>
""", unsafe_allow_html=True)

st.title("🛸 ADRIEL AI — ECOSSISTEMA REVOLUCIONÁRIO DE TRÁFEGO")
st.markdown("Central automatizada de inteligência para gerenciamento de campanhas fundo de funil nacionais e internacionais.")
st.write("---")

# Divisão de tela: Robô se apresentando vs Menu da Esteira Crescente
col_avatar, col_botoes = st.columns([1.3, 1])

with col_avatar:
    st.markdown("""
    <div class="robo-card-main">
        <h2 style='margin-top: 0;'>🤖 CAPACIDADE DE IA INSTALADA</h2>
        <p style='font-size: 16px; line-height: 1.6; color: #cbd5e1;'>
            "Olá, Comandante José Marques! A estrutura visual mestre da nossa família de módulos está 
            fixada no servidor de produção. Estou pronto para rodar os scanners de conformidade, 
            geração de pre-sells e envio automatizado via Google Ads API."
        </p>
        <span style='background: #00FF87; color: #050811; padding: 5px 12px; font-weight: bold; border-radius: 20px; font-size: 13px;'>
            ESTEIRA DE CONVENÇÃO HOMOLOGADA 🟢
        </span>
    </div>
    """, unsafe_allow_html=True)
    
    # KPIs de controle do SaaS
    c_st1, c_st2 = st.columns(2)
    with c_st1: st.metric(label="Integridade do Servidor GitHub", value="100% Conectado", delta="Estável")
    with c_st2: st.metric(label="Família de Páginas Ativas", value="7 Módulos", delta="Operacionais")

with col_botoes:
    st.markdown("### 🕹️ ESTEIRA DE COMANDO CRESCENTE")
    st.markdown("Navegue pelos módulos de luxo da plataforma utilizando os botões de atalho ou a barra lateral:")
    st.write("")
    
    # Botões que crescem ao passar o mouse e indicam qual página abrir
    if st.button("🛰️ MÓDULO 1: Radar de Produtos", key="h_m1"):
        st.info("Acesse a página **1_Radar** no menu esquerdo para operar.")
    if st.button("📊 MÓDULO 2: Auditor de Mercado", key="h_m2"):
        st.info("Acesse a página **2_Auditor** no menu esquerdo para operar.")
    if st.button("📝 MÓDULO 3: Gerador de Anúncios", key="h_m3"):
        st.info("Acesse a página **3_Gerador** no menu esquerdo para operar.")
    if st.button("🏹 MÓDULO 4: Caçador Ativo", key="h_m4"):
        st.info("Acesse a página **4_Cacador** no menu esquerdo para operar.")
    if st.button("🌐 MÓDULO 5: Construtor Pre-Sell", key="h_m5"):
        st.info("Acesse a página **5_Presell** no menu esquerdo para operar.")
    if st.button("🚀 MÓDULO 6: Ativador Google Ads", key="h_m6"):
        st.info("Acesse a página **6_Ativador_Google_Ads** no menu esquerdo para operar.")
    if st.button("💎 MÓDULO 7: Gestão de Assinantes", key="h_m7"):
        st.info("Acesse a página **7_Area_Assinantes** no menu esquerdo para operar.")
