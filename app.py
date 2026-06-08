import streamlit as st
import pandas as pd
import time

# Configuração de Layout Amplo Premium Black
st.set_page_config(page_title="Adriel AI - Painel de Controle", layout="wide", initial_sidebar_state="expanded")

# =============================================================================================================
# INJEÇÃO DE CSS DE ALTA PERFORMANCE (CLONE EXATO DO LAYOUT PREMIUM)
# =============================================================================================================
st.markdown("""
<style>
    /* Fundo Escuro Espacial */
    .stApp {
        background-color: #0b111e !important;
        color: #ffffff !important;
    }
    
    /* Customização Absoluta da Barra Lateral */
    [data-testid="stSidebar"] {
        background-color: #070c16 !important;
        border-right: 1px solid #1e293b !important;
    }
    
    /* Caixa do Cabeçalho de Boas-Vindas */
    .header-box {
        background-color: #0f172a !important;
        border: 1px solid #1e293b !important;
        border-radius: 8px !important;
        padding: 12px 20px !important;
        margin-bottom: 20px !important;
    }
    
    /* Títulos dos Módulos Principais */
    .modulo-titulo {
        font-size: 14px !important;
        font-weight: bold !important;
        color: #60a5fa !important;
        letter-spacing: 0.5px;
        margin-bottom: 15px;
        text-transform: uppercase;
    }
    
    /* Botões Dinâmicos Estilo Neon (Módulo 2) */
    div.stButton > button {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%) !important;
        color: white !important;
        font-weight: bold !important;
        border: none !important;
        padding: 10px 20px !important;
        border-radius: 6px !important;
        width: 100% !important;
        transition: all 0.3s ease !important;
        box-shadow: 0px 4px 10px rgba(16, 185, 129, 0.2) !important;
    }
    div.stButton > button:hover {
        transform: scale(1.02) !important;
        box-shadow: 0px 6px 15px rgba(16, 185, 129, 0.4) !important;
    }
    
    /* Botões Secundários de Histórico/Planilha */
    .stButton-sec > button {
        background: #1e293b !important;
        color: #cbd5e1 !important;
        border: 1px solid #334155 !important;
    }
</style>
""", unsafe_allow_html=True)

# =============================================================================================================
# BARRA LATERAL (MENU COMPLETO DE PROVOCAÇÃO DO SAAS)
# =============================================================================================================
with st.sidebar:
    st.markdown("<h2 style='color: #60a5fa; font-size: 22px; font-weight: 800;'>🌌 Adriel AI</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #64748b; font-size: 12px; margin-top:-15px;'>PAINEL DE CONTROLE</p>", unsafe_allow_html=True)
    st.write("---")
    
    # Links visuais simulando o menu profissional do print
    st.markdown("🖥️ **Dashboard**")
    st.caption("🛰️ Radar de Produtos")
    st.caption("🔬 Auditor de Mercado")
    st.caption("📝 Gerador de Anúncios")
    st.caption("🏹 Caçador de Lançamentos")
    st.write("---")
    st.caption("⚙️ Configurações")
    st.caption("🚪 Sair")

# =============================================================================================================
# CABEÇALHO HORIZONTAL DE BOAS-VINDAS
# =============================================================================================================
col_h1, col_h2 = st.columns([2, 1])
with col_h1:
    st.markdown("""
    <div class="header-box">
        <span style="font-size: 14px; color: #94a3b8;">👨‍✈️ Olá, <b>José Marques</b>, Comandante do Adriel AI!</span>
    </div>
    """, unsafe_allow_html=True)
with col_h2:
    st.markdown("""
    <div class="header-box" style="text-align: right;">
        <span style="font-size: 12px; color: #10b981;">● Status: <b>Sistema Online</b></span>
    </div>
    """, unsafe_allow_html=True)

# =============================================================================================================
# DUAS COLUNAS PRINCIPAIS DO CHASSI (REDUÇÃO E CRIAÇÃO EM PARALELO)
# =============================================================================================================
col_modulo1, col_modulo2 = st.columns([1.4, 1])

# 📊 COLUNA 1: MÓDULO RADAR DE PRODUTOS (FILTRO XEQUE-MATE)
with col_modulo1:
    st.markdown('<p class="modulo-titulo">🛰️ MÓDULO 1: RADAR DE PRODUTOS [FILTRO XEQUE-MATE]</p>', unsafe_allow_html=True)
    
    # Criando a tabela idêntica à do print com badges coloridos de aprovação da IA
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
    # Botão de download da planilha estilo o do print
    st.button("📥 [BAIXAR PLANILHA DE INTELIGÊNCIA (.CSV)]", key="btn_csv_download")

# 📝 COLUNA 2: GERADOR DE ANÚNCIOS MASTER & PRE-SELL
with col_modulo2:
    st.markdown('<p class="modulo-titulo">📝 MÓDULO 2: GERADOR DE ANÚNCIOS MASTER & PRE-SELL</p>', unsafe_allow_html=True)
    
    # Campos de Entrada Estilizados do Print
    prod_gringo = st.text_input("PROD_GRINGO:", value="Sugar Defender")
    resumo_niche = st.text_area("RESUMO (Niche/Dores):", value="Suplemento natural para equilíbrio do metabolismo.", height=68)
    
    st.write("")
    # Botões Verdes Grandes de Ação do Software
    if st.button("🟢 (A) GERAR ANÚNCIOS ADSMaster (Copy + Roteiro Vídeo)", key="btn_ads_master"):
        st.success("Anúncios estruturados com sucesso!")
        
    st.write("")
    if st.button("🟢 [B] FABRICAR PRE-SELL (Landing Page Text) </>", key="btn_fabricar_presell"):
        st.success("Estrutura HTML da Pre-sell copiada!")
        
    # Caixa cinza simulando o bloco de propriedades do criativo
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
    # Botão de salvar no histórico da base
    st.button("💾 [SALVAR CAMPANHA NO HISTÓRICO]", key="btn_save_history")

# Rodapé institucional do Print
st.write("---")
st.markdown("<p style='text-align: center; font-size: 11px; color: #475569;'>© 2026 Adriel AI - Ferramenta Exclusiva de Inteligência para Afiliados Elite. Todos os Direitos Reservados.</p>", unsafe_allow_html=True)
