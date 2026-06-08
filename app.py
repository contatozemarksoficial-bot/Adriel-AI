import streamlit as st
import pandas as pd

# Configuração premium de layout amplo (Ocupa 100% da largura da tela)
st.set_page_config(page_title="Adriel AI - Painel de Controle", layout="wide", initial_sidebar_state="collapsed")

# =============================================================================================================
# INJEÇÃO DE ÁUDIO REAL VIA JAVASCRIPT (O ROBÔ FALA AO CLICAR NA TELA)
# =============================================================================================================
texto_boas_vindas = "Olá, Comandante José Marques da Silva! Painel de controle Adriel A I totalmente carregado e integrado em três colunas paralelas."

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
# INJEÇÃO DE CSS DE ALTO PADRÃO (ESTILO BLACK E SINAL PISCANTE HOVER NOS BOTÕES)
# =============================================================================================================
st.markdown("""
<style>
    /* 🌌 Fundo Escuro Fiel ao Print da Imagem */
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
    
    /* Oculta as barras e menus nativos */
    [data-testid="stSidebar"] { display: none !important; }
    [data-testid="stHeader"] { display: none !important; }
    
    /* 🚨 ANIMAÇÃO DE SINAL NEON: ALTERNA AS BORDAS (CIANO <-> VERDE) */
    @keyframes sinal-pulsante {
        0% { border-color: #00E5FF; box-shadow: 0 0 5px rgba(0, 229, 255, 0.2); }
        50% { border-color: #00FF87; box-shadow: 0 0 15px rgba(0, 255, 135, 0.4); }
        100% { border-color: #00E5FF; box-shadow: 0 0 5px rgba(0, 229, 255, 0.2); }
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
    
    .subtitulo-bloco-real {
        font-size: 13px !important;
        font-weight: bold !important;
        color: #60a5fa !important;
        margin-bottom: 15px;
        text-transform: uppercase;
    }

    /* BOTÕES GERAIS QUE ENVIAM O SINAL PISCANTE E ZOOM */
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
    
    /* MENU DA COLUNA 1 DA ESQUERDA (TAMANHO PADRONIZADO DO PRINT) */
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
</style>
""", unsafe_allow_html=True)

# Gerenciamento seguro de rotas de páginas na memória ativa
if "pagina_atual" not in st.session_state:
    st.session_state.pagina_atual = "Dashboard"

# =============================================================================================================
# CONFIGURAÇÃO DE 3 COLUNAS VERTICAIS PARALELAS (CLONE DO LEONARDO AI)
# =============================================================================================================
col_esquerda, col_centro, col_direita = st.columns([0.85, 1.35, 1])

# 🏢 COLUNA 1: LOGO ADRIEL AI + NOMES EXATOS EXTEMSADOS DA SUA LISTA
with col_esquerda:
    st.markdown('<div class="coluna-container">', unsafe_allow_html=True)
    st.markdown("<h2 style='color: #60a5fa; font-size: 24px; font-weight: 800; margin:0;'>🤖 Adriel AI</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #64748b; font-size: 11px; margin-top:-5px;'>PAINEL DE CONTROLE</p>", unsafe_allow_html=True)
    st.write("---")
    
    st.markdown('<div class="menu-lateral-container">', unsafe_allow_html=True)
    if st.button("🎛️ Dashboard Geral", key="n_dash"): st.session_state.pagina_atual = "Dashboard"; st.rerun()
    if st.button("🛰️ 1. Radar de Produtos", key="n_m1"): st.session_state.pagina_atual = "Radar"; st.rerun()
    if st.button("🔬 2. Auditor de Mercado", key="n_m2"): st.session_state.pagina_atual = "Auditor"; st.rerun()
    if st.button("📝 3. Gerador de Anúncios", key="n_m3"): st.session_state.pagina_atual = "Gerador"; st.rerun()
    if st.button("🏹 4. Caçador de Lançamentos", key="n_m4"): st.session_state.pagina_atual = "Cacador"; st.rerun()
    if st.button("🌐 5. Gerador de Pre-Cell", key="n_m5"): st.session_state.pagina_atual = "PreCell"; st.rerun()
    if st.button("🚀 6. Ativador Google Ads API", key="n_m6"): st.session_state.pagina_atual = "GoogleAds"; st.rerun()
    if st.button("💎 7. Área de Assinantes", key="n_m7"): st.session_state.pagina_atual = "Assinantes"; st.rerun()
    st.write("---")
    st.caption("⚙️ Configurações SaaS")
    st.markdown('</div></div>', unsafe_allow_html=True)

# =============================================================================================================
# ROTEAMENTO SEGURO — ENCAIXANDO SEUS ARQUIVOS DE BACKUP NAS COLUNAS 2 E 3
# =============================================================================================================

# 🏠 INTERFACE: DASHBOARD GERAL E PREENCHIDO
if st.session_state.pagina_atual == "Dashboard":
    with col_centro:
        st.markdown('<div class="coluna-container">', unsafe_allow_html=True)
        st.markdown('<div class="header-box-real">👤 Olá, <b>José Marques</b>, Comandante do Adriel AI!</div>', unsafe_allow_html=True)
        st.markdown('<p class="subtitulo-bloco-real">MÓDULO 1: RADAR DE PRODUTOS [FILTRO XEQUE-MATE]</p>', unsafe_allow_html=True)
        
        # Tabela clonada fiel
        dados_tabela = {
            "Name": [f"Produto-acanodiano {i}" for i in range(1, 8)],
            "Comissões": ["3,00%", "2,00%", "1,00%", "1,00%", "1,00%", "2,00%", "2,00%"],
            "Comissão": ["R$,15%", "R$,75%", "R$,25%", "R$,35%", "R$,25%", "R$,25%", "R$,25%"],
            "Veredito da IA": ["APROVADO (Risco Baixo)"] * 7
        }
        st.dataframe(pd.DataFrame(dados_tabela), use_container_width=True, hide_index=True)
        st.write("")
        st.button("📄 [BAIXAR PLANILHA DE INTELIGÊNCIA (.CSV)]", key="btn_csv_dash")
        st.markdown('</div>', unsafe_allow_html=True)

    with col_direita:
        st.markdown('<div class="coluna-container" style="border-right: none;">', unsafe_allow_html=True)
        st.markdown('<div class="header-box-real" style="text-align: right;">🟢 Status: <span style="color: #10b981; font-weight:bold;">Online</span></div>', unsafe_allow_html=True)
        st.markdown('<p class="subtitulo-bloco-real">MÓDULO 2: GERADOR DE ANÚNCIOS MASTER & PRE-SELL</p>', unsafe_allow_html=True)
        st.text_input("PROD_GRINGO:", value="Sugar Defender")
        st.text_area("RESUMO (Niche/Dores):", value="Suplemento natural para equilíbrio do metabolismo.", height=68)
        st.write("")
        st.button("🔥 (A) GERAR ANÚNCIOS ADSMaster (Copy + Roteiro Vídeo)", key="btn_ads")
        st.write("")
        st.markdown('<div style="background-color: #0f172a; border: 1px solid #1e293b; padding: 12px; border-radius: 6px; font-size: 13px; color: #94a3b8; font-family: monospace;"><b>image_7be312.png (Títulos, Descrições)</b><br>Títulos 15 blocks | Formatas de blocks</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# 🛰️ INTERFACE: 1. RADAR DE PRODUTOS RESTAURADO DO SEU BACKUP
elif st.session_state.pagina_atual == "Radar":
    with col_centro:
        st.markdown('<div class="coluna-container">', unsafe_allow_html=True)
        st.markdown('<div class="header-box-real">🛰️ Filtros de Mineração Ativos no Servidor</div>', unsafe_allow_html=True)
        st.markdown('<p class="subtitulo-bloco-real">🔬 BANCO DE DADOS: 22 PRODUTOS CAMPEÕES</p>', unsafe_allow_html=True)
        st.write("• **Sugar Defender** (Diabetes / Açúcar)")
        st.write("• **Obsesta** (Perda de Peso)")
        st.write("• **ProDentim** (Saúde Dental)")
        st.write("• **Java Burn** (Metabolismo)")
