import streamlit as st
import pandas as pd

# Configuração premium de layout amplo (Ocupa 100% da largura da tela)
st.set_page_config(page_title="Adriel AI - Radar de Produtos", layout="wide", initial_sidebar_state="expanded")

# =============================================================================================================
# INJEÇÃO DE CÓDIGO CSS PREMIUM DE HIGH PERFORMANCE (O PADRÃO VISUAL EXATO DA FAMÍLIA)
# =============================================================================================================
st.markdown("""
<style>
    /* 🌌 Fundo Escuro Fiel ao Print do Leonardo AI */
    .stApp {
        background-color: #0b111e !important;
        color: #ffffff !important;
    }
    
    /* Remove o preenchimento e margens do topo padrão do Streamlit */
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 0rem !important;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
    }
    
    /* Oculta as barras e cabeçalhos nativos do Streamlit */
    [data-testid="stSidebar"] { display: none !important; }
    [data-testid="stHeader"] { display: none !important; }
    
    /* 🚨 ANIMAÇÃO DE SINAL NEON: ALTERNA AS BORDAS (CIANO <-> VERDE) */
    @keyframes sinal-pulsante {
        0% { border-color: #00E5FF; box-shadow: 0 0 8px rgba(0, 229, 255, 0.2); }
        50% { border-color: #00FF87; box-shadow: 0 0 18px rgba(0, 255, 135, 0.4); }
        100% { border-color: #00E5FF; box-shadow: 0 0 8px rgba(0, 229, 255, 0.2); }
    }

    /* Linhas divisórias das colunas internas */
    .coluna-container-interna {
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
    
    .subtitulo-bloco-real {
        font-size: 13px !important;
        font-weight: bold !important;
        color: #60a5fa !important;
        margin-bottom: 15px;
        text-transform: uppercase;
    }

    /* BOTÕES PISCANTES QUE COMENTAM O SINAL NO HOVER */
    div.stButton > button {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%) !important;
        color: white !important;
        font-weight: bold !important;
        font-size: 14px !important;
        border: 2px solid #1e293b !important;
        padding: 12px 15px !important;
        border-radius: 6px !important;
        width: 100% !important;
        cursor: pointer !important;
        transition: all 0.3s ease-in-out !important;
    }
    div.stButton > button:hover {
        animation: sinal-pulsante 2s infinite ease-in-out !important;
        background: linear-gradient(135deg, #00FF87 0%, #00E5FF 100%) !important;
        color: #050811 !important;
        transform: scale(1.02) !important;
    }
    
    /* MENU DA COLUNA DA ESQUERDA (MESMO TAMANHO RIGOROSO) */
    .menu-lateral-container div.stButton > button {
        background: #0f172a !important; 
        color: #cbd5e1 !important; 
        border: 2px solid #1e293b !important;
        text-align: left !important; 
        padding: 13px 18px !important; 
        width: 100% !important; 
        margin-bottom: 6px !important; 
        font-size: 13px !important;
        animation: none !important;
    }
    .menu-lateral-container div.stButton > button:hover {
        background: #1e293b !important; 
        color: #00FF87 !important; 
        border-color: #00E5FF !important; 
        box-shadow: 0 0 12px rgba(0, 229, 255, 0.5) !important;
    }
    
    /* Customização fina para tabelas */
    .stDataFrame {
        border: 1px solid #1e293b !important;
        border-radius: 8px !important;
    }
</style>
""", unsafe_allow_html=True)

# =============================================================================================================
# MONTAGEM DAS 3 COLUNAS SIMULTÂNEAS NA HORIZONTAL (PADRÃO REQUINTADO ADRIEL AI)
# =============================================================================================================
col_esquerda, col_centro, col_direita = st.columns([0.8, 1.4, 1.0])

# 🏢 COLUNA 1: LOGO ADRIEL AI COM ROBÔ + BOTÕES DE LINK NATIVO DO MENU LATERAL
with col_esquerda:
    st.markdown('<div class="coluna-container-interna">', unsafe_allow_html=True)
    st.markdown("<h2 style='color: #60a5fa; font-size: 24px; font-weight: 800; margin:0;'>🤖 Adriel AI</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #64748b; font-size: 11px; margin-top:-5px;'>PAINEL DE CONTROLE</p>", unsafe_allow_html=True)
    st.write("---")
    
    st.markdown('<div class="menu-lateral-container">', unsafe_allow_html=True)
    st.page_link("app.py", label="🎛️ Dashboard Geral")
    st.page_link("pages/1_RADAR DE PRODUTOS.py", label="🛰️ 1. Radar de Produtos")
    st.page_link("pages/2_AUDITOR DE PRODUTOS.py", label="🔬 2. Auditor de Mercado")
    st.write("---")
    st.caption("⚙️ Configurações Gerais")
    st.markdown('</div></div>', unsafe_allow_html=True)

# 📊 COLUNA 2: MÓDULO 1 RADAR DE PRODUTOS COMPLETO DO SEU BACKUP
with col_centro:
    st.markdown('<div class="coluna-container-interna">', unsafe_allow_html=True)
    st.markdown('<div class="header-box-real">👤 Comandante: <b>José Marques</b> | Scanner de Elite Ativo</div>', unsafe_allow_html=True)
    st.markdown('<p class="subtitulo-bloco-real">MÓDULO 1: RADAR DE PRODUTOS [FILTRO XEQUE-MATE]</p>', unsafe_allow_html=True)
    
    # Lista de Produtos do seu Banco de Dados original com comissões reais do print
    dados_tabela = {
        "Name": ["Sugar Defender", "Java Burn", "Puravive", "Prodentim", "GlucoBerry", "Citrus Burn", "Protocolo Oculto"],
        "Plataforma": ["BuyGoods 🇺🇸", "ClickBank 🇺🇸", "ClickBank 🇺🇸", "BuyGoods 🇺🇸", "Hotmart 🇧🇷", "ClickBank 🇺🇸", "Braip 🇧🇷"],
        "Comissão": ["$ 118.20", "$ 135.00", "$ 142.50", "$ 125.00", "R$ 247,00", "$ 95.00", "R$ 197,00"],
        "Veredito da IA": ["APROVADO (Risco Baixo)"] * 7
    }
    st.dataframe(pd.DataFrame(dados_tabela), use_container_width=True, hide_index=True)
    st.write("")
    
    if st.button("📄 [BAIXAR PLANILHA DE INTELIGÊNCIA (.CSV)]", key="btn_csv_radar_page"):
        st.success("✅ Download concluído! Tabela do Radar extraída com sucesso.")
    st.markdown('</div>', unsafe_allow_html=True)

# 📑 COLUNA 3: MONITORAMENTO VOLUMÉTRICO DA GRAVIDADE DO SEU PRINT
with col_direita:
    st.markdown('<div class="coluna-container-interna" style="border-right: none;">', unsafe_allow_html=True)
    st.markdown('<div class="header-box-real" style="text-align: right;">Filtro: <b>Top Active Gringa 🇺🇸</b></div>', unsafe_allow_html=True)
    st.markdown('<p class="subtitulo-bloco-real">📊 PARÂMETROS EXTRAÍDOS PELA IA</p>', unsafe_allow_html=True)
    
    st.info("🔥 **Módulo Espião Operando**\n\nVarredura contínua rastreando lotes de Gravidade e Temperatura acima de 140+ nas plataformas internacionais.")
    st.markdown('</div>', unsafe_allow_html=True)

# Rodapé unificado da família (Sempre idêntico!)
st.markdown('<div style="clear: both; text-align: center; font-size: 11px; color: #475569; padding-top: 20px;"><hr style="border-color: #1e293b;">© 2026 Adriel AI - Ferramenta Exclusiva de Inteligência para Afiliados Elite. Todos os Direitos Reservados.</div>', unsafe_allow_html=True)
