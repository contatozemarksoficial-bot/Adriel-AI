import streamlit as st
import pandas as pd
import time

# Configuração premium de layout amplo (Ocupa 100% da largura da tela)
st.set_page_config(page_title="Adriel AI - Painel de Controle", layout="wide", initial_sidebar_state="collapsed")

# =============================================================================================================
# INJEÇÃO DE ÁUDIO REAL VIA JAVASCRIPT (O ROBÔ FALA AO CLICAR NA TELA)
# =============================================================================================================
texto_boas_vindas = "Olá, Comandante José Marques da Silva! Painel operacional atualizado com os módulos volumétricos e contadores de mil acessos ativos."

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
# INJEÇÃO DE CSS PREMIUM (BOTÕES QUE PISCAM AUTOMÁTICO, MUDAM DE COR E GANHAM TRACÇÃO NO MOUSE)
# =============================================================================================================
st.markdown("""
<style>
    /* 🌌 Fundo Escuro do Painel Principal */
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
    
    /* 🚨 ANIMAÇÃO DE SINAL NEON: ALTERNA AS BORDAS DO BOTÃO SELECIONADO (CIANO <-> VERDE) */
    @keyframes sinal-pulsante {
        0% { border-color: #00E5FF; box-shadow: 0 0 5px rgba(0, 229, 255, 0.2); }
        50% { border-color: #00FF87; box-shadow: 0 0 15px rgba(0, 255, 135, 0.5); }
        100% { border-color: #00E5FF; box-shadow: 0 0 5px rgba(0, 229, 255, 0.2); }
    }

    /* Linhas divisórias das 3 colunas verticais */
    .coluna-container {
        background-color: transparent;
        border-right: 1px solid #1e293b;
        padding-right: 15px;
        padding-left: 10px;
    }
    
    /* Caixas horizontais superiores de logs e mini-dashboards */
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
        letter-spacing: 0.5px;
        margin-bottom: 15px;
        text-transform: uppercase;
    }

    /* 🟢 BOTÕES CENTRAIS PISCANTES QUE DESACELERAM E CRESCEM NO MOUSE */
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
        animation: sinal-pulsante 3s infinite ease-in-out !important; /* Pisca automático rápido */
        transition: all 0.4s ease-in-out !important;
    }
    
    /* Efeito ao passar o mouse: Desacelera a animação, dá zoom e brilha fixo */
    div.stButton > button:hover {
        animation: none !important; /* Desacelera/para de piscar */
        background: linear-gradient(135deg, #00FF87 0%, #00E5FF 100%) !important;
        color: #050811 !important;
        transform: scale(1.03) translateY(-2px) !important; /* Cresce de tamanho */
        box-shadow: 0px 10px 25px rgba(0, 255, 135, 0.6) !important;
        border-color: #ffffff !important;
    }
    
    /* 📟 POLIMENTO DA BARRA LATERAL ESQUERDA */
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
        animation: sinal-pulsante 4s infinite ease-in-out !important; /* Pulsação lenta contínua */
    }
    
    .menu-lateral-btn div.stButton > button:hover {
        animation: none !important;
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

# 🏢 COLUNA 1 (FIXA E IMUTÁVEL): LOGO ADRIEL AI + BOTÕES DO MENU LATERAL
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
    st.caption("⚙️ Configurações Gerais")
    st.caption("🚪 Sair do Sistema")
    st.markdown('</div></div>', unsafe_allow_html=True)

# =============================================================================================================
# ROTEAMENTO DA ESTEIRA DAS PÁGINAS (ADICIONADOS OS MENUS VOLUMÉTRICOS DE TOPO CONTRA O VAZIO)
# =============================================================================================================

# 🏠 PÁGINA: DASHBOARD INICIAL COMPLETO (RECHEADO CONTRA O VAZIO)
if st.session_state.pagina_atual == "Dashboard":
    with col_centro:
        st.markdown('<div class="coluna-container">', unsafe_allow_html=True)
        
        # Bloco Superior do Comandante
        st.markdown('<div class="header-box-real">👤 Olá, <b>José Marques</b>, Comandante do Adriel AI!</div>', unsafe_allow_html=True)
        
        # 📈 INJEÇÃO DE CONTADORES EM LINHA NO MÓDULO 1 (PREENCHIMENTO VISUAL DOS MIL ACESSOS)
        col_mini1, col_mini2 = st.columns(2)
        with col_mini1:
            st.markdown('<div class="kpi-box"><span style="font-size: 11px; color: #64748b; font-weight: bold; text-transform: uppercase;">🔥 Cliques Analisados</span><br><span style="font-size: 20px; color: #00FF87; font-weight: 800;">14.250 mil</span></div>', unsafe_allow_html=True)
        with col_mini2:
            st.markdown('<div class="kpi-box"><span style="font-size: 11px; color: #64748b; font-weight: bold; text-transform: uppercase;">📡 Ofertas Ativas</span><br><span style="font-size: 20px; color: #00E5FF; font-weight: 800;">1.840 mil</span></div>', unsafe_allow_html=True)
        
        st.write("")
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
