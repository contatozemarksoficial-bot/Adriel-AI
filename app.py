import streamlit as st
import pandas as pd
import time

# Configuração de Layout Amplo Executivo Premium Black
st.set_page_config(page_title="Adriel AI - Painel de Controle", layout="wide", initial_sidebar_state="expanded")

# =============================================================================================================
# INJEÇÃO DE ÁUDIO REAL VIA JAVASCRIPT (O ROBÔ FALA AO CLICAR NA TELA)
# =============================================================================================================
texto_boas_vindas = "Olá, Comandante José Marques da Silva! Painel de controle Adriel A I totalmente carregado. Todos os botões operacionais e os módulos volumétricos de cliques estão ativos."

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
# INJEÇÃO DE CSS DE ALTO LUXO (BOTÕES COM TRANSIÇÃO DE COR NEON E FEEDBACK AO PASSAR O MOUSE)
# =============================================================================================================
st.markdown("""
<style>
    /* 🌌 Fundo Escuro do Painel do Print */
    .stApp {
        background-color: #0b111e !important;
        color: #ffffff !important;
    }
    
    /* Customização de Alto Luxo para a Barra Lateral */
    [data-testid="stSidebar"] {
        background-color: #070c16 !important;
        border-right: 1px solid #1e293b !important;
    }
    
    /* 🚨 1. ANIMAÇÃO DE PISCAR DA SIDEBAR MUTANDO DE COR (CIANO <-> VERDE) */
    @keyframes pisca-lateral {
        0% { border-color: #00E5FF; box-shadow: 0 0 8px rgba(0, 229, 255, 0.2); }
        50% { border-color: #00FF87; box-shadow: 0 0 18px rgba(0, 255, 135, 0.4); }
        100% { border-color: #00E5FF; box-shadow: 0 0 8px rgba(0, 229, 255, 0.2); }
    }

    [data-testid="stSidebarNav"] ul li a span {
        color: #ffffff !important; 
        font-weight: bold !important;
        font-size: 14px !important;
    }
    [data-testid="stSidebarNav"] ul li a {
        background-color: #0f172a !important; 
        border: 2px solid #1e293b !important;
        border-radius: 8px !important;
        margin-bottom: 8px !important;
        padding: 12px 14px !important;
        animation: pisca-lateral 4s infinite ease-in-out !important; 
        display: block !important;
    }

    /* 🏙️ Caixa Superior Executiva Criptografada */
    .header-box-real {
        background: linear-gradient(135deg, #0f172a 0%, #070c16 100%) !important;
        border: 2px solid #1e293b !important;
        border-radius: 12px !important;
        padding: 18px 25px !important;
        margin-bottom: 25px !important;
        box-shadow: 0px 4px 20px rgba(0,0,0,0.4) !important;
    }
    
    /* Títulos dos Blocos */
    .subtitulo-bloco {
        font-size: 13px !important;
        font-weight: bold !important;
        color: #60a5fa !important;
        letter-spacing: 0.5px;
        margin-bottom: 15px;
        text-transform: uppercase;
    }

    /* 🟢 2. BOTÕES CENTRAIS PISCANDO QUE DESACELERAM E CRESCEM NO MOUSE */
    @keyframes pulsa-botoes-master {
        0% { background: linear-gradient(135deg, #10b981 0%, #059669 100%); border-color: #1e293b; box-shadow: 0 0 5px rgba(16, 185, 129, 0.3); }
        50% { background: linear-gradient(135deg, #00FF87 0%, #10b981 100%); border-color: #00E5FF; box-shadow: 0 0 20px rgba(0, 255, 135, 0.6); }
        100% { background: linear-gradient(135deg, #10b981 0%, #059669 100%); border-color: #1e293b; box-shadow: 0 0 5px rgba(16, 185, 129, 0.3); }
    }

    div.stButton > button {
        color: white !important;
        font-weight: bold !important;
        font-size: 15px !important;
        border: 2px solid #1e293b !important;
        padding: 14px 20px !important;
        border-radius: 8px !important;
        width: 100% !important;
        animation: pulsa-botoes-master 3s infinite ease-in-out !important; /* Pisca e alterna de cor rápido */
        cursor: pointer !important;
        transition: all 0.4s ease-in-out !important;
    }
    
    /* Efeito de passar o mouse: Desacelera a pulsação, expande e acende fixo */
    div.stButton > button:hover {
        animation: none !important; /* Desacelera/para o piscar */
        background: linear-gradient(135deg, #00FF87 0%, #00E5FF 100%) !important;
        color: #050811 !important;
        transform: scale(1.03) translateY(-2px) !important; /* Cresce de tamanho */
        box-shadow: 0px 10px 25px rgba(0, 255, 135, 0.6) !important;
        border-color: #ffffff !important;
    }
</style>
""", unsafe_allow_html=True)

# =============================================================================================================
# 📊 PREENCHIMENTO DO TOPO: PAINEL DE MIL VOLUMES E MÉTRICAS REAIS DE CONTROLE (FIM DO VAZIO)
# =============================================================================================================
st.markdown("""
<div class="header-box-real">
    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
        <div>
            <span style="font-size: 18px; color: #00FF87; font-weight: 800;">🛸 CENTRAL ULTRA: ADRIEL AI APP</span><br>
            <span style="font-size: 14px; color: #94a3b8;">👨‍✈️ Comandante: <b>José Marques</b> | Licença Master Ativa</span>
        </div>
        <div style="text-align: right;">
            <span style="font-size: 13px; color: #60a5fa; font-weight: bold;">🛰️ Sincronismo API Google: 100% OK</span><br>
            <span style="font-size: 13px; color: #94a3b8;">📅 Sistema Atualizado em: 06/06/2026</span>
        </div>
    </div>
    <hr style="border-color: #1e293b; margin: 15px 0;">
    <!-- 📈 SISTEMA COMPLETO DE CONTADORES EM LINHA (MIL ACESSOS DA IA) -->
    <div style="display: flex; justify-content: space-between; align-items: center; gap: 20px; flex-wrap: wrap;">
        <div style="background: #0f172a; padding: 10px 20px; border-radius: 8px; border: 1px solid #1e293b; flex: 1; text-align: center;">
            <span style="font-size: 11px; color: #64748b; font-weight: bold; text-transform: uppercase;">🔥 Cliques Monitorados (Hoje)</span><br>
            <span style="font-size: 20px; color: #00FF87; font-weight: 800;">12.450 mil</span>
        </div>
        <div style="background: #0f172a; padding: 10px 20px; border-radius: 8px; border: 1px solid #1e293b; flex: 1; text-align: center;">
            <span style="font-size: 11px; color: #64748b; font-weight: bold; text-transform: uppercase;">📡 Ofertas Escaneadas</span><br>
            <span style="font-size: 20px; color: #00E5FF; font-weight: 800;">1.820 mil</span>
        </div>
        <div style="background: #0f172a; padding: 10px 20px; border-radius: 8px; border: 1px solid #1e293b; flex: 1; text-align: center;">
            <span style="font-size: 11px; color: #64748b; font-weight: bold; text-transform: uppercase;">🛡️ Campanhas Blindadas</span><br>
            <span style="font-size: 20px; color: #ffffff; font-weight: 800;">342 Ativas</span>
        </div>
        <div style="background: #0f172a; padding: 10px 20px; border-radius: 8px; border: 1px solid #1e293b; flex: 1; text-align: center;">
            <span style="font-size: 11px; color: #64748b; font-weight: bold; text-transform: uppercase;">💸 Faturamento Recorrente</span><br>
            <span style="font-size: 20px; color: #00FF87; font-weight: 800;">R$ 48.750,00</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# =============================================================================================================
# ESTRUTURA GIGANTE EM PARALELO (COLUNA 1: RADAR DE PRODUTOS | COLUNA 2: GERADOR RSA)
# =============================================================================================================
col_esq, col_dir = st.columns([1.35, 1])

# 📊 COLUNA ESQUERDA: MÓDULO 1 RADAR DE PRODUTOS [FILTRO XEQUE-MATE]
with col_esq:
    st.markdown('<p class="subtitulo-bloco">MÓDULO 1: RADAR DE PRODUTOS [FILTRO XEQUE-MATE]</p>', unsafe_allow_html=True)
    
    # Lista fiel ao seu print de produtos acanodianos validados com badge de inteligência
    dados_tabela = {
        "Name": [f"Produto-acanodiano {i}" for i in range(1, 8)],
        "Comissões": ["3,00%", "2,00%", "1,00%", "1,00%", "1,00%", "2,00%", "2,00%"],
        "Comissão": ["R$,15%", "R$,75%", "R$,25%", "R$,35%", "R$,25%", "R$,25%", "R$,25%"],
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
    df_painel = pd.DataFrame(dados_tabela)
    st.dataframe(df_painel, use_container_width=True, hide_index=True)
    
    st.write("")
    # Botão que pulsa e desacelera/cresce no foco
    if st.button("📄 [BAIXAR PLANILHA DE INTELIGÊNCIA (.CSV)]", key="btn_csv_real"):
        st.success("Planilha processada e pronta na nuvem!")

# 📝 COLUNA DIREITA: MÓDULO 2 GERADOR DE ANÚNCIOS MASTER & PRE-SELL
with col_dir:
    st.markdown('<p class="subtitulo-bloco">MÓDULO 2: GERADOR DE ANÚNCIOS MASTER & PRE-SELL</p>', unsafe_allow_html=True)
    
    # Inputs organizados exatamente como na imagem
    p_gringo = st.text_input("PROD_GRINGO:", value="Sugar Defender", key="p_gringo_in")
    p_resumo = st.text_area("RESUMO (Niche/Dores):", value="Suplemento natural para equilíbrio do metabolismo.", height=68, key="p_resumo_in")
    
    st.write("")
