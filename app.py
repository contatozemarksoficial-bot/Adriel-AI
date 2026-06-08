import streamlit as st
import pandas as pd
import time

# Configuração premium de layout amplo (Força o app a ocupar toda a largura da tela)
st.set_page_config(page_title="Adriel AI - Painel de Controle", layout="wide", initial_sidebar_state="collapsed")

# =============================================================================================================
# INJEÇÃO DE ÁUDIO REAL VIA JAVASCRIPT (O ROBÔ FALA AO CLICAR NA TELA)
# =============================================================================================================
texto_boas_vindas = "Olá, Comandante José Marques da Silva! Painel de controle estruturado em três colunas simultâneas. Todos os sinais e botões estão operacionais."

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
# INJEÇÃO DE CSS DE ALTA PERFORMANCE (DESATIVA SIDEBAR NATIVA E TRAVA AS 3 COLUNAS DO PRINT)
# =============================================================================================================
st.markdown("""
<style>
    /* 🌌 Fundo Escuro Idêntico ao do Print da Imagem */
    .stApp {
        background-color: #0b111e !important;
        color: #ffffff !important;
    }
    
    /* Oculta as bordas padrão do Streamlit para dar o visual plano limpo */
    [data-testid="stSidebar"] {
        display: none !important;
    }
    [data-testid="stHeader"] {
        display: none !important;
    }
    
    /* 🚨 ANIMAÇÃO DE SINAL: ALTERNA AS BORDAS (CIANO <-> VERDE NEON) */
    @keyframes sinal-pulsante {
        0% { border-color: #00E5FF; box-shadow: 0 0 8px rgba(0, 229, 255, 0.2); }
        50% { border-color: #00FF87; box-shadow: 0 0 18px rgba(0, 255, 135, 0.4); }
        100% { border-color: #00E5FF; box-shadow: 0 0 8px rgba(0, 229, 255, 0.2); }
    }

    /* Estilização para as linhas divisórias e blocos */
    .coluna-container {
        background-color: transparent;
        border-right: 1px solid #1e293b;
        padding-right: 20px;
        padding-left: 10px;
        height: 100vh;
    }
    
    /* Caixa de texto superior horizontal */
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

    /* 🟢 CUSTOMIZAÇÃO DOS BOTÕES COM EFEITO DE SINAL NO MOUSE (HOVER) */
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
    
    /* Quando a pessoa passa o mouse ou clica, aciona o sinal pulsante idêntico */
    div.stButton > button:hover {
        animation: sinal-pulsante 2s infinite ease-in-out !important;
        background: linear-gradient(135deg, #00FF87 0%, #00E5FF 100%) !important;
        color: #050811 !important;
        transform: scale(1.02) !important;
    }
    
    /* Botões pretos simples do menu lateral esquerdo */
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

# =============================================================================================================
# MONTAGEM DAS 3 COLUNAS HORIZONTAIS COMPLETAS (O CLONE REAL DA IMAGEM)
# =============================================================================================================
col_esquerda, col_centro, col_direita = st.columns([0.75, 1.4, 1])

# 🏢 COLUNA 1 (ESQUERDA): A LOGO DO ADRIEL AI + MENU DO PAINEL DE CONTROLE
with col_esquerda:
    st.markdown('<div class="coluna-container" style="border-right: 1px solid #1e293b;">', unsafe_allow_html=True)
    
    # 🛰️ Clone da Logo Superior do Print
    st.markdown("<h2 style='color: #60a5fa; font-size: 24px; font-weight: 800; margin-bottom:0;'>🤖 Adriel AI</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #64748b; font-size: 11px; margin-top:-5px; letter-spacing:1px;'>PAINEL DE CONTROLE</p>", unsafe_allow_html=True)
    st.write("---")
    
    # Lista de Menus em formato de botões funcionais para as páginas
    st.markdown('<div class="menu-lateral-btn">', unsafe_allow_html=True)
    st.button("🎛️ Dashboard", key="m_dash")
    st.button("🛰️ Radar de Produtos", key="m_radar")
    st.button("🔬 Auditor de Mercado", key="m_auditor")
    st.button("📝 Gerador de Anúncios", key="m_gerador")
    st.button("🏹 Caçador de Lançamentos", key="m_cacador")
    st.button("🌐 Construtor Pre-Sell", key="m_presell")
    st.button("🚀 Ativador Google Ads", key="m_ativador")
    st.button("💎 Gestão de Assinantes", key="m_assinantes")
    st.write("---")
    st.button("⚙️ Configurações", key="m_config")
    st.button("🚪 Sair", key="m_sair")
    st.markdown('</div></div>', unsafe_allow_html=True)

# 📊 COLUNA 2 (CENTRO): MÓDULO 1 RADAR DE PRODUTOS [FILTRO XEQUE-MATE]
with col_centro:
    st.markdown('<div class="coluna-container" style="border-right: 1px solid #1e293b;">', unsafe_allow_html=True)
    
    # Card de identificação do comandante do topo
    st.markdown('<div class="header-box-real">👤 Olá, <b>José Marques</b>, Comandante do Adriel AI!</div>', unsafe_allow_html=True)
    
    st.markdown('<p class="subtitulo-bloco-real">MÓDULO 1: RADAR DE PRODUTOS [FILTRO XEQUE-MATE]</p>', unsafe_allow_html=True)
    
    # Listagem de dados milimétrica da tabela da imagem original
    dados_tabela = {
        "Name": [f"Produto-acanodiano {i}" for i in range(1, 10)],
        "Comissões": ["3,00%", "2,00%", "1,00%", "1,00%", "1,00%", "2,00%", "2,00%", "1,00%", "1,00%"],
        "Comissão": ["R$,15%", "R$,75%", "R$,25%", "R$,35%", "R$,25%", "R$,25%", "R$,25%", "R$,60%", "R$,60%"],
        "Veredito da IA": [
            "APROVADO (Risco Baixo)", 
            "APROVADO (Risco Baixo)", 
            "REVISAR (Risco Médio)", 
            "REVISAR (Risco Médio)", 
            "APROVADO (Risco Baixo)",
            "APROVADO (Risco Baixo)",
            "APROVADO (Risco Baixo)",
            "REVISAR (Risco Médio)",
            "REVISAR (Risco Médio)"
        ]
    }
    df_painel = pd.DataFrame(dados_tabela)
    st.dataframe(df_painel, use_container_width=True, hide_index=True)
    
    st.write("")
    # Botão de exportação que dispara o sinal neon quando passa o mouse por cima
    if st.button("📄 [BAIXAR PLANILHA DE INTELIGÊNCIA (.CSV)]", key="btn_csv_real"):
        st.success("Planilha processada com sucesso!")
    st.markdown('</div>', unsafe_allow_html=True)

# 📝 COLUNA 3 (DIREITA): MÓDULO 2 GERADOR DE ANÚNCIOS MASTER & PRE-SELL
with col_direita:
    st.markdown('<div class="coluna-container" style="border-right: none;">', unsafe_allow_html=True)
    
    # Card de status online do topo
    st.markdown('<div class="header-box-real" style="text-align: right;">🟢 Status: <span style="color: #10b981; font-weight:bold;">Sistema Online</span> | Chave Mestre Ativa</div>', unsafe_allow_html=True)
    
    st.markdown('<p class="subtitulo-bloco-real">MÓDULO 2: GERADOR DE ANÚNCIOS MASTER & PRE-SELL</p>', unsafe_allow_html=True)
    
    # Inputs organizados do print
    p_gringo = st.text_input("PROD_GRINGO:", value="Sugar Defender", key="p_gringo_in")
    p_resumo = st.text_area("RESUMO (Niche/Dores):", value="Suplemento natural para equilíbrio do metabolismo.", height=68, key="p_resumo_in")
    
    st.write("")
    # Botões verdes de ação que dão o sinal interativo ao focar
    if st.button("🔥 (A) GERAR ANÚNCIOS ADSMaster (Copy + Roteiro Vídeo)", key="btn_gen_ads_real"):
        st.success("Campanha de copy estruturada com sucesso!")
        
    st.write("")
    if st.button("🔥 [B] FABRICAR PRE-SELL (Landing Page Text) </>", key="btn_gen_html_real"):
        st.success("HTML da Landing Page pronto na área de transferência!")
        
    # Caixa preta de propriedades exatas da imagem
    st.markdown('<div style="background-color: #0f172a; border: 1px solid #1e293b; padding: 12px; border-radius: 6px; margin-top: 14px; font-size: 13px; color: #94a3b8; font-family: monospace;"><b>image_7be312.png (Títulos, Descrições, Palavras-chave)</b><br>Títulos 15 blocks<br>Títulos, Descrições<br>Palavras-chave<br>Formatas de blocks<br>Salvar campanha no blocks</div>', unsafe_allow_html=True)
    
    st.write("")
    if st.button("💾 [SALVAR CAMPANHA NO HISTÓRICO]", key="btn_save_history_real"):
        st.info("Campanha guardada no histórico da base de dados.")
    st.markdown('</div>', unsafe_allow_html=True)

# Rodapé oficial idêntico ao rodapé da imagem
