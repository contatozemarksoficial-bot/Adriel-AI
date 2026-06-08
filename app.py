import streamlit as st
import pandas as pd
import time

# Configuração premium de layout amplo (Ocupa 100% da largura da tela)
st.set_page_config(page_title="Adriel AI - Painel de Controle", layout="wide", initial_sidebar_state="collapsed")

# =============================================================================================================
# INJEÇÃO DE ÁUDIO REAL VIA JAVASCRIPT (O ROBÔ FALA AO CLICAR NA TELA)
# =============================================================================================================
texto_boas_vindas = "Olá, Comandante José Marques da Silva! Painel estruturado com a esteira completa de seis módulos operacionais. Todos os sistemas prontos."

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
# INJEÇÃO DE CSS DE ALTO PADRÃO (PADRONIZAÇÃO EXATA DE TODA A FAMÍLIA DE PÁGINAS)
# =============================================================================================================
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
    
    /* Oculta os menus e barras nativos */
    [data-testid="stSidebar"] { display: none !important; }
    [data-testid="stHeader"] { display: none !important; }
    
    /* 🚨 ANIMAÇÃO DE SINAL: ALTERNA AS BORDAS DO BOTÃO SELECIONADO (CIANO <-> VERDE) */
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

    /* 🟢 BOTÕES DA ESTEIRA QUE DISPARAM O SINAL PISCANTE NEON COM ZOOM NO MOUSE */
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
    
    /* 📟 ALINHAMENTO CIRÚRGICO DA COLUNA ESQUERDA */
    .menu-lateral-btn {
        display: flex;
        flex-direction: column;
        gap: 2px !important;
        width: 100% !important;
    }
    
    .menu-lateral-btn div.stButton > button {
        background: #0f172a !important; 
        color: #cbd5e1 !important;
        border: 2px solid #1e293b !important;
        text-align: left !important;
        padding: 12px 16px !important;
        font-size: 14px !important;
        width: 95% !important; 
        margin-bottom: 5px !important;
        animation: none !important; 
    }
    
    .menu-lateral-btn div.stButton > button:hover {
        background: #1e293b !important;
        color: #00FF87 !important;
        border-color: #00E5FF !important;
        box-shadow: 0 0 12px rgba(0, 229, 255, 0.5) !important;
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

# 🏢 COLUNA 1 (FIXA E IMUTÁVEL): LOGO ADRIEL AI + BOTÕES DO MENU DE NAVEGAÇÃO
with col_esquerda:
    st.markdown('<div class="coluna-container">', unsafe_allow_html=True)
    st.markdown("<h2 style='color: #60a5fa; font-size: 24px; font-weight: 800; margin-bottom:0;'>🤖 Adriel AI</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #64748b; font-size: 11px; margin-top:-5px; letter-spacing:1px;'>PAINEL DE CONTROLE</p>", unsafe_allow_html=True)
    st.write("---")
    
    st.markdown('<div class="menu-lateral-btn">', unsafe_allow_html=True)
    if st.button("🎛️ Dashboard", key="btn_nav_dash"): st.session_state.pagina_atual = "Dashboard"; st.rerun()
    if st.button("🛰️ 1. Radar de Produtos", key="btn_nav_m1"): st.session_state.pagina_atual = "M1_Radar"; st.rerun()
    if st.button("🔬 2. Auditor de Mercado", key="btn_nav_m2"): st.session_state.pagina_atual = "M2_Auditor"; st.rerun()
    if st.button("📝 3. Gerador de Anúncios", key="btn_nav_m3"): st.session_state.pagina_atual = "M3_Gerador"; st.rerun()
    if st.button("🏹 4. Caçador Ativo", key="btn_nav_m4"): st.session_state.pagina_atual = "M4_Cacador"; st.rerun()
    if st.button("🌐 5. Construtor Pre-Sell", key="btn_nav_m5"): st.session_state.pagina_atual = "M5_Presell"; st.rerun()
    st.write("---")
    st.caption("⚙ ... Configurações SaaS")
    st.markdown('</div></div>', unsafe_allow_html=True)

# =============================================================================================================
# ROTEAMENTO DA ESTEIRA DAS 6 PÁGINAS (MANTENDO O MESMO PADRÃO SEM DESORGANIZAR)
# =============================================================================================================

# 🏠 PÁGINA: DASHBOARD INICIAL COMPLETO
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

# 🛰️ PÁGINA: MÓDULO 1 RADAR DE PRODUTOS
elif st.session_state.pagina_atual == "M1_Radar":
    with col_centro:
        st.markdown('<div class="coluna-container">', unsafe_allow_html=True)
        st.markdown('<div class="header-box-real">🔬 Parâmetros Ativos de Mineração na Gringa</div>', unsafe_allow_html=True)
        st.markdown('<p class="subtitulo-bloco-real">🛰️ RADAR: EXTRAÇÃO DE PRODUTOS</p>', unsafe_allow_html=True)
        st.selectbox("Selecione a Plataforma Espião:", ["ClickBank 🇺🇸", "BuyGoods 🇺🇸", "Digistore24 🇩🇪"])
        st.slider("Filtrar por Gravidade:", 0, 300, 140)
        st.markdown('</div>', unsafe_allow_html=True)
    with col_direita:
        st.markdown('<div class="coluna-container" style="border-right: none;">', unsafe_allow_html=True)
