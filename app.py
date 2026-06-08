import streamlit as st
import pandas as pd
import time

# Configuração premium de layout amplo (Ocupa 100% da largura da tela)
st.set_page_config(page_title="Adriel AI - Painel de Controle", layout="wide", initial_sidebar_state="collapsed")

# INJEÇÃO DE CSS DE ALTA PERFORMANCE (CORREÇÃO DE ESPAÇAMENTO FANTASMA E ALINHAMENTO NO TETO)
st.markdown("""
<style>
    /* 🌌 Fundo Escuro Fiel ao Print da Imagem */
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
    
    /* Oculta as bordas e menus nativos */
    [data-testid="stSidebar"] { display: none !important; }
    [data-testid="stHeader"] { display: none !important; }
    
    /* 🚨 ANIMAÇÃO DE SINAL: ALTERNA AS BORDAS DO BOTÃO SELECIONADO (CIANO <-> VERDE) */
    @keyframes sinal-pulsante {
        0% { border-color: #00E5FF; box-shadow: 0 0 8px rgba(0, 229, 255, 0.2); }
        50% { border-color: #00FF87; box-shadow: 0 0 18px rgba(0, 255, 135, 0.4); }
        100% { border-color: #00E5FF; box-shadow: 0 0 8px rgba(0, 229, 255, 0.2); }
    }

    /* Linhas divisórias das 3 colunas verticais (CORRIGIDO SEM HEIGHT FIXO) */
    .coluna-container {
        background-color: transparent;
        border-right: 1px solid #1e293b;
        padding-right: 15px;
        padding-left: 10px;
        margin-top: 0px !important;
    }
    
    /* Caixas horizontais superiores de logs */
    .header-box-real {
        background-color: #0f172a !important;
        border: 1px solid #1e293b !important;
        border-radius: 8px !important;
        padding: 12px 18px !important;
        margin-bottom: 20px !important;
        font-size: 13px !important;
    }
    
    .subtitulo-bloco-real {
        font-size: 13px !important;
        font-weight: bold !important;
        color: #60a5fa !important;
        letter-spacing: 0.5px;
        margin-bottom: 15px;
        text-transform: uppercase;
    }

    /* BOTÕES DA ESTEIRA QUE DISPARAM O SINAL PISCANTE NEON */
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
    
    /* Ativa o sinal piscante na interação do mouse */
    div.stButton > button:hover {
        animation: sinal-pulsante 2s infinite ease-in-out !important;
        background: linear-gradient(135deg, #00FF87 0%, #00E5FF 100%) !important;
        color: #050811 !important;
        transform: scale(1.02) !important;
    }
    
    /* Customização dos botões pretos chapados do menu esquerdo */
    .menu-lateral-btn > div.stButton > button {
        background: transparent !important;
        color: #94a3b8 !important;
        border: 1px solid transparent !important;
        text-align: left !important;
        padding: 10px 15px !important;
        font-size: 14px !important;
    }
    .menu-lateral-btn > div.stButton > button:hover {
        animation: none !important;
        background: #1e293b !important;
        color: #00FF87 !important;
        border-color: #1e293b !important;
    }
</style>
""", unsafe_allow_html=True)

# Inicialização segura do controle do roteamento do menu na memória do servidor
if "pagina_atual" not in st.session_state:
    st.session_state.pagina_atual = "Dashboard"

# =============================================================================================================
# MONTAGEM RIGOROSA DA ESTRUTURA DE 3 COLUNAS SIMULTÂNEAS
# =============================================================================================================
col_esquerda, col_centro, col_direita = st.columns([0.75, 1.4, 1])

# 🏢 COLUNA 1 (FIXA E IMUTÁVEL): LOGO ADRIEL AI + BOTÕES DO MENU LATERAL
with col_esquerda:
    st.markdown('<div class="coluna-container">', unsafe_allow_html=True)
    st.markdown("<h2 style='color: #60a5fa; font-size: 24px; font-weight: 800; margin-bottom:0;'>🤖 Adriel AI</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #64748b; font-size: 11px; margin-top:-5px; letter-spacing:1px;'>PAINEL DE CONTROLE</p>", unsafe_allow_html=True)
    st.write("---")
    
    st.markdown('<div class="menu-lateral-btn">', unsafe_allow_html=True)
    if st.button("🎛️ Dashboard", key="btn_nav_dash"): st.session_state.pagina_atual = "Dashboard"; st.rerun()
    if st.button("🛰️ Radar de Produtos", key="btn_nav_radar"): st.session_state.pagina_atual = "Radar"; st.rerun()
    if st.button("🚀 Ativador Google Ads", key="btn_nav_google"): st.session_state.pagina_atual = "GoogleAds"; st.rerun()
    st.write("---")
    st.caption("⚙️ Configurações Gerais")
    st.caption("🚪 Sair")
    st.markdown('</div></div>', unsafe_allow_html=True)

# =============================================================================================================
# ROTEAMENTO DA FAMÍLIA DE PÁGINAS (MANTENDO O MESMO CORTE SEM MUDAR O ESTLO)
# =============================================================================================================

# 🏠 INTERFACE 1: DASHBOARD COMPLETO (PADRÃO DE INSTALAÇÃO DO SEU PRINT)
if st.session_state.pagina_atual == "Dashboard":
    with col_centro:
        st.markdown('<div class="coluna-container">', unsafe_allow_html=True)
        st.markdown('<div class="header-box-real">👤 Olá, <b>José Marques</b>, Comandante do Adriel AI!</div>', unsafe_allow_html=True)
        st.markdown('<p class="subtitulo-bloco-real">MÓDULO 1: RADAR DE PRODUTOS [FILTRO XEQUE-MATE]</p>', unsafe_allow_html=True)
        
        dados_tabela = {
            "Name": [f"Produto-acanodiano {i}" for i in range(1, 10)],
            "Comissões": ["3,00%", "2,00%", "1,00%", "1,00%", "1,00%", "2,00%", "2,00%", "1,00%", "1,00%"],
            "Comissão": ["R$,15%", "R$,75%", "R$,25%", "R$,35%", "R$,25%", "R$,25%", "R$,25%", "R$,60%", "R$,60%"],
            "Veredito da IA": ["APROVADO (Risco Baixo)"] * 9
        }
        st.dataframe(pd.DataFrame(dados_tabela), use_container_width=True, hide_index=True)
        st.write("")
        st.button("📄 [BAIXAR PLANILHA DE INTELIGÊNCIA (.CSV)]", key="btn_csv_dash")
        st.markdown('</div>', unsafe_allow_html=True)

    with col_direita:
        st.markdown('<div class="coluna-container" style="border-right: none;">', unsafe_allow_html=True)
        st.markdown('<div class="header-box-real" style="text-align: right;">🟢 Status: <span style="color: #10b981; font-weight:bold;">Sistema Online</span> | Chave Mestre Ativa</div>', unsafe_allow_html=True)
        st.markdown('<p class="subtitulo-bloco-real">MÓDULO 2: GERADOR DE ANÚNCIOS MASTER & PRE-SELL</p>', unsafe_allow_html=True)
        
        st.text_input("PROD_GRINGO:", value="Sugar Defender", key="p_gringo_dash")
        st.text_area("RESUMO (Niche/Dores):", value="Suplemento natural para equilíbrio do metabolismo.", height=68, key="p_resumo_dash")
        st.write("")
        st.button("🔥 (A) GERAR ANÚNCIOS ADSMaster", key="btn_ads_dash")
        st.markdown('</div>', unsafe_allow_html=True)

# 🛰️ INTERFACE 2: PÁGINA RECORTE DO RADAR DE PRODUTOS COMPLETO
elif st.session_state.pagina_atual == "Radar":
    with col_centro:
        st.markdown('<div class="coluna-container">', unsafe_allow_html=True)
        st.markdown('<div class="header-box-real">🛰️ Filtros de Mineração Ativos no Servidor</div>', unsafe_allow_html=True)
        st.markdown('<p class="subtitulo-bloco-real">🔬 PARÂMETROS DO SCANNER AVANÇADO</p>', unsafe_allow_html=True)
        
        st.selectbox("Selecione a Origem das Ofertas:", ["ClickBank 🇺🇸", "BuyGoods 🇺🇸", "Hotmart 🇧🇷"])
        st.slider("Filtrar por Gravidade Mínima:", 0, 300, 150)
        st.markdown('</div>', unsafe_allow_html=True)

    with col_direita:
        st.markdown('<div class="coluna-container" style="border-right: none;">', unsafe_allow_html=True)
        st.markdown('<div class="header-box-real" style="text-align: right;">Volume Escaneado: <b>1.420 Produtos</b></div>', unsafe_allow_html=True)
        st.markdown('<p class="subtitulo-bloco-real">🏆 AS 3 OFERTAS DE MAIOR GRAVIDADE</p>', unsafe_allow_html=True)
        st.info("🔥 1. Java Burn - Gravidade 240\n\n⭐ 2. Puravive - Gravidade 190\n\n⚡ 3. Sugar Defender - Gravidade 180")
        st.markdown('</div>', unsafe_allow_html=True)

# 🚀 INTERFACE 3: PÁGINA RECORTE DO ATIVADOR GOOGLE ADS API
elif st.session_state.pagina_atual == "GoogleAds":
    with col_centro:
        st.markdown('<div class="coluna-container">', unsafe_allow_html=True)
        st.markdown('<div class="header-box-real">🚀 Painel de Conexão com os Servidores de Tráfego</div>', unsafe_allow_html=True)
        st.markdown('<p class="subtitulo-bloco-real">🤖 CONFIGURAÇÕES DA CAMPANHA (GOOGLE ADS API)</p>', unsafe_allow_html=True)
        
        st.text_input("Nome Técnico da Campanha:", value="Sales-Search-2026")
        st.selectbox("Métrica de Foco do Leilão:", ["Conversões", "Cliques", "Parcela de impressões"])
        st.number_input("Orçamento Financeiro Diário (R$):", min_value=10.0, value=50.0, step=5.0)
        st.markdown('</div>', unsafe_allow_html=True)

    with col_direita:
        st.markdown('<div class="coluna-container" style="border-right: none;">', unsafe_allow_html=True)
        st.markdown('<div class="header-box-real" style="text-align: right;">Handshake: <span style="color:#10b981;">Aprovado 🟢</span></div>', unsafe_allow_html=True)
