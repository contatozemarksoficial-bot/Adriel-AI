import streamlit as st
import pandas as pd
import time

# Configuração de Layout Amplo Premium Black
st.set_page_config(page_title="Adriel AI - Painel de Controle", layout="wide", initial_sidebar_state="expanded")

# =============================================================================================================
# INJEÇÃO DE CSS DE ALTA PERFORMANCE (POLIMENTO DO DASHBOARD E RECURSOS DO ROBOZINHO)
# =============================================================================================================
st.markdown("""
<style>
    /* 🌌 Fundo Escuro Espacial do Aplicativo */
    .stApp {
        background-color: #0b111e !important;
        color: #ffffff !important;
    }
    
    /* 📟 Customização da Barra Lateral Esquerda */
    [data-testid="stSidebar"] {
        background-color: #070c16 !important;
        border-right: 1px solid #1e293b !important;
    }
    
    /* 🤖 Caixa Premium do Robozinho Inteligente */
    .robo-card-top {
        background: linear-gradient(135deg, #111b35 0%, #070c16 100%) !important;
        border: 2px solid #00E5FF !important;
        border-radius: 12px !important;
        padding: 15px !important;
        margin-bottom: 25px !important;
        box-shadow: 0px 4px 15px rgba(0, 229, 255, 0.2) !important;
    }
    
    /* 👨‍✈️ Caixa do Cabeçalho de Boas-Vindas */
    .header-box {
        background-color: #0f172a !important;
        border: 1px solid #1e293b !important;
        border-radius: 8px !important;
        padding: 14px 20px !important;
        margin-bottom: 25px !important;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    
    /* 🎯 Títulos dos Módulos Principais */
    .modulo-titulo {
        font-size: 14px !important;
        font-weight: bold !important;
        color: #60a5fa !important;
        letter-spacing: 0.5px;
        margin-bottom: 15px;
        text-transform: uppercase;
    }
    
    /* 🟢 Botões Dinâmicos Estilo Neon (Módulo 2) */
    div.stButton > button {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%) !important;
        color: white !important;
        font-weight: bold !important;
        border: none !important;
        padding: 12px 20px !important;
        border-radius: 8px !important;
        width: 100% !important;
        transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
        box-shadow: 0px 4px 10px rgba(16, 185, 129, 0.2) !important;
        cursor: pointer !important;
    }
    div.stButton > button:hover {
        transform: scale(1.03) !important;
        box-shadow: 0px 6px 20px rgba(16, 185, 129, 0.5) !important;
        background: linear-gradient(135deg, #00FF87 0%, #10b981 100%) !important;
    }
    
    /* 🛠️ Botões de Navegação Lateral */
    .sidebar-btn > button {
        background: #0f172a !important;
        color: #cbd5e1 !important;
        border: 1px solid #1e293b !important;
        padding: 8px 15px !important;
        font-size: 14px !important;
        text-align: left !important;
        margin-bottom: 5px !important;
    }
    .sidebar-btn > button:hover {
        background: #1e293b !important;
        color: #00FF87 !important;
        border-color: #00E5FF !important;
    }
</style>
""", unsafe_allow_html=True)

# =============================================================================================================
# BARRA LATERAL (MENU COMPLETO DA PLATAFORMA COM ACESSO DIRETO)
# =============================================================================================================
with st.sidebar:
    st.markdown("<h2 style='color: #60a5fa; font-size: 24px; font-weight: 800; margin-bottom:0;'>🤖 Adriel AI</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #64748b; font-size: 11px; margin-top:-5px; letter-spacing:1px;'>PAINEL DE CONTROLE</p>", unsafe_allow_html=True)
    st.write("---")
    
    st.markdown("<p style='color: #94a3b8; font-size: 12px; font-weight: bold;'>🎛️ NAVEGAÇÃO</p>", unsafe_allow_html=True)
    
    # Botões rápidos na barra lateral para direcionar o cliente
    st.button("🖥️ Dashboard Geral", key="nav_dash", help="Página Inicial")
    st.button("🛰️ Módulo 1: Radar", key="nav_m1")
    st.button("🔬 Módulo 2: Auditor", key="nav_m2")
    st.button("📝 Módulo 3: Gerador RSA", key="nav_m3")
    st.button("🏹 Módulo 4: Caçador", key="nav_m4")
    st.button("🌐 Módulo 5: Pre-Sell", key="nav_m5")
    st.button("🚀 Módulo 6: Ativador Google", key="nav_m6")
    st.button("💎 Módulo 7: Assinantes", key="nav_m7")
    
    st.write("---")
    st.caption("⚙️ Configurações do SaaS")
    st.caption("🚪 Sair do Sistema")

# =============================================================================================================
# 🤖 APRESENTAÇÃO DO ROBOZINHO NA CENTRAL SUPERIOR (FIM DO VISUAL VAZIO!)
# =============================================================================================================
st.markdown("""
<div class="robo-card-top">
    <h3 style='margin: 0; color: #00FF87; font-size: 18px;'>🤖 SYSTEM MONITOR: ROBÔ ADRIEL AI</h3>
    <p style='margin: 5px 0 0 0; font-size: 14px; color: #94a3b8; line-height: 1.5;'>
        "Olá, Comandante José Marques! Estou posicionado no topo da infraestrutura. 
        Meus motores de varredura contra fraudes e o chassi de integração da Google Ads API estão 100% síncronos e prontos."
    </p>
</div>
""", unsafe_allow_html=True)

# CABEÇALHO HORIZONTAL DE INFORMAÇÕES DO USUÁRIO
col_h1, col_h2 = st.columns([2, 1])
with col_h1:
    st.markdown("""
    <div class="header-box">
        <span style="font-size: 14px; color: #cbd5e1;">👤 Usuário Ativo: <b>José Marques</b> (Comandante Geral)</span>
    </div>
    """, unsafe_allow_html=True)
with col_h2:
    st.markdown("""
    <div class="header-box" style="text-align: right;">
        <span style="font-size: 14px; color: #10b981;">● Status: <b>Sistema Online</b> 🔗</span>
    </div>
    """, unsafe_allow_html=True)

# =============================================================================================================
# DUAS COLUNAS PRINCIPAIS DO CHASSI OPERACIONAL
# =============================================================================================================
col_modulo1, col_modulo2 = st.columns([1.4, 1])

# 📊 COLUNA 1: MÓDULO RADAR DE PRODUTOS
with col_modulo1:
    st.markdown('<p class="modulo-titulo">🛰️ MÓDULO 1: RADAR DE PRODUTOS [FILTRO XEQUE-MATE]</p>', unsafe_allow_html=True)
    
    # Dataframe alinhado perfeitamente
    dados_produtos = {
        "Name": [f"Produto-acanodiano {i}" for i in range(1, 8)],
        "Comissões": ["3,00%", "2,00%", "1,00%", "1,00%", "1,00%", "2,00%", "2,00%"],
        "Comissão": ["R$ 15% ", "R$ 75% ", "R$ 25% ", "R$ 35% ", "R$ 25% ", "R$ 25% ", "R$ 25% "],
        "Veredito da IA": [
            "APROVADO (Risco Baixo)", 
            "APROVADO (Risco Baixo)", 
            "REVISAR (Risco Médio)", 
            "REVISAR (Risco Médio)", 
            "APROVADO (Risco Baixo)",
            "APROVADO (Risco Baixo)",
            "APROVADO (Risco Baixo)"
        ]
    }
    df = pd.DataFrame(dados_produtos)
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.write("")
    st.button("📥 [BAIXAR PLANILHA DE INTELIGÊNCIA (.CSV)]", key="btn_csv_download")

# 📝 COLUNA 2: GERADOR DE ANÚNCIOS MASTER & PRE-SELL
with col_modulo2:
    st.markdown('<p class="modulo-titulo">📝 MÓDULO 2: GERADOR DE ANÚNCIOS MASTER & PRE-SELL</p>', unsafe_allow_html=True)
    
    prod_gringo = st.text_input("PROD_GRINGO:", value="Sugar Defender", key="prod_gringo_input")
    resumo_niche = st.text_area("RESUMO (Niche/Dores):", value="Suplemento natural para equilíbrio do metabolismo.", height=68, key="resumo_niche_input")
    
    st.write("")
    if st.button("🟢 (A) GERAR ANÚNCIOS ADSMaster (Copy + Roteiro Vídeo)", key="btn_ads_master"):
        st.success("Anúncios criados com conformidade digital!")
        
    st.write("")
    if st.button("🟢 [B] FABRICAR PRE-SELL (Landing Page Text) </>", key="btn_fabricar_presell"):
        st.success("Layout HTML estruturado com sucesso!")
        
    # Caixa cinza informativa de propriedades do criativo
    st.markdown("""
    <div style="background-color: #0f172a; border: 1px solid #1e293b; padding: 12px; border-radius: 6px; margin-top: 15px; font-size: 13px; color: #94a3b8;">
        <b>image_7be312.png (Títulos, Descrições, Palavras-chave)</b><br>
        Títulos 15 blocks<br>
        Títulos, Descrições<br>
        Palavras-chave<br>
        Formatas de blocks<br>
        Salvar campanha no blocks
    </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    st.button("💾 [SALVAR CAMPANHA NO HISTÓRICO]", key="btn_save_history")

# Rodapé institucional unificado
st.write("---")
st.markdown("<p style='text-align: center; font-size: 11px; color: #475569;'>© 2026 Adriel AI - Ferramenta Exclusiva de Inteligência para Afiliados Elite. Todos os Direitos Reservados.</p>", unsafe_allow_html=True)
