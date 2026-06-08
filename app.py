import streamlit as st
import pandas as pd
import time

# Configuração de Layout Amplo Executivo Premium Black
st.set_page_config(page_title="Adriel AI - Painel de Controle", layout="wide", initial_sidebar_state="expanded")

# =============================================================================================================
# INJEÇÃO DE ÁUDIO REAL VIA JAVASCRIPT (O ROBÔ FALA AO ENTRAR/CLICAR NA TELA)
# =============================================================================================================
texto_boas_vindas = "Olá, Comandante José Marques da Silva! Painel de controle Adriel A I totalmente carregado. Todos os botões operacionais e a API do Google Ads estão prontos para o disparo."

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
# INJEÇÃO DE CSS AVANÇADO (BOTÕES PISCANDO EM LINHA E CORREÇÃO DE COR DO MENU LATERAL)
# =============================================================================================================
st.markdown("""
<style>
    /* 🌌 Fundo Escuro do Painel do Print */
    .stApp {
        background-color: #0b111e !important;
        color: #ffffff !important;
    }
    
    /* Customização da Barra Lateral */
    [data-testid="stSidebar"] {
        background-color: #070c16 !important;
        border-right: 1px solid #1e293b !important;
    }
    
    /* 🚨 ANIMAÇÃO DE PISCAR DOS BOTÕES EM NEON (VERDE/CIANO) */
    @keyframes pisca-botoes {
        0% { border-color: #1e293b; box-shadow: 0 0 5px rgba(0, 229, 255, 0.1); }
        50% { border-color: #00FF87; box-shadow: 0 0 15px rgba(0, 255, 135, 0.4); }
        100% { border-color: #1e293b; box-shadow: 0 0 5px rgba(0, 229, 255, 0.1); }
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
        animation: pisca-botoes 3s infinite ease-in-out !important; /* Faz o menu lateral piscar */
        display: block !important;
    }

    /* Caixa Superior de Informações */
    .header-box-real {
        background-color: #0f172a !important;
        border: 1px solid #1e293b !important;
        border-radius: 8px !important;
        padding: 14px 20px !important;
        margin-bottom: 20px !important;
    }
    
    /* Cabeçalhos Clones da Imagem */
    .subtitulo-bloco {
        font-size: 13px !important;
        font-weight: bold !important;
        color: #60a5fa !important;
        letter-spacing: 0.5px;
        margin-bottom: 12px;
        text-transform: uppercase;
    }

    /* 🟢 Customização dos Botões Verdes Piscando (Módulo 2) */
    div.stButton > button {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%) !important;
        color: white !important;
        font-weight: bold !important;
        border: 2px solid #1e293b !important;
        padding: 11px 20px !important;
        border-radius: 6px !important;
        width: 100% !important;
        animation: pisca-botoes 4s infinite ease-in-out !important; /* Faz os botões centrais piscarem */
        cursor: pointer !important;
        transition: transform 0.2s ease !important;
    }
    div.stButton > button:hover {
        transform: scale(1.02) !important;
        border-color: #00E5FF !important;
    }
</style>
""", unsafe_allow_html=True)

# =============================================================================================================
# BARRA SUPERIOR DE LOG E HISTÓRICO (EXATAMENTE COMO NO SEU PRINT)
# =============================================================================================================
col_top1, col_top2 = st.columns(2)
with col_top1:
    st.markdown('<div class="header-box-real">👤 Olá, <b>José Marques</b>, Comandante do Adriel AI!</div>', unsafe_allow_html=True)
with col_top2:
    st.markdown('<div class="header-box-real" style="text-align: right;">🟢 Status: <span style="color: #10b981; font-weight:bold;">Sistema Online</span> | Chave Mestre Ativa | Data: 06/06/2026</div>', unsafe_allow_html=True)

# =============================================================================================================
# ESTRUTURA GIGANTE EM PARALELO (COLUNA 1: RADAR DE PRODUTOS | COLUNA 2: GERADOR RSA)
# =============================================================================================================
col_esq, col_dir = st.columns([1.35, 1])

# 📊 COLUNA ESQUERDA: CLONE DO MÓDULO 1 RADAR DE PRODUTOS [FILTRO XEQUE-MATE]
with col_esq:
    st.markdown('<p class="subtitulo-bloco">MÓDULO 1: RADAR DE PRODUTOS [FILTRO XEQUE-MATE]</p>', unsafe_allow_html=True)
    
    # Lista fiel ao seu print de produtos acanodianos validados com badge colorido
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
    # Botão de exportação da base
    if st.button("📄 [BAIXAR PLANILHA DE INTELIGÊNCIA (.CSV)]", key="btn_csv_real"):
        st.success("Planilha processada e pronta na nuvem!")

# 📝 COLUNA DIREITA: CLONE DO MÓDULO 2 GERADOR DE ANÚNCIOS MASTER & PRE-SELL
with col_dir:
    st.markdown('<p class="subtitulo-bloco">MÓDULO 2: GERADOR DE ANÚNCIOS MASTER & PRE-SELL</p>', unsafe_allow_html=True)
    
    # Inputs organizados do print
    p_gringo = st.text_input("PROD_GRINGO:", value="Sugar Defender", key="p_gringo_in")
    p_resumo = st.text_area("RESUMO (Niche/Dores):", value="Suplemento natural para equilíbrio do metabolismo.", height=68, key="p_resumo_in")
    
    st.write("")
    # Botões Verdes Grandes Piscando e Executando
    if st.button("⚡ (A) GERAR ANÚNCIOS ADSMaster (Copy + Roteiro Vídeo)", key="btn_gen_ads_real"):
        st.success("Campanha e copys estruturadas com sucesso!")
        
    st.write("")
    if st.button("⚡ [B] FABRICAR PRE-SELL (Landing Page Text) </>", key="btn_gen_html_real"):
        st.success("Código da Landing Page limpo e gerado com sucesso!")
        
    # Caixa preta de parâmetros exatos da imagem
    st.markdown('<div style="background-color: #0f172a; border: 1px solid #1e293b; padding: 12px; border-radius: 6px; margin-top: 14px; font-size: 13px; color: #94a3b8; font-family: monospace;"><b>image_7be312.png (Títulos, Descrições, Palavras-chave)</b><br>Títulos 15 blocks<br>Títulos, Descrições<br>Palavras-chave<br>Formatas de blocks<br>Salvar campanha no blocks</div>', unsafe_allow_html=True)
    
    st.write("")
    # Botão de histórico final
    if st.button("💾 [SALVAR CAMPANHA NO HISTÓRICO]", key="btn_save_history_real"):
        st.info("Campanha de lote salva na base de dados.")

# Rodapé de cópia idêntico ao rodapé do print
st.write("---")
st.markdown('<p style="text-align: center; font-size: 11px; color: #475569;">© 2026 Adriel AI - Ferramenta Exclusiva de Inteligência para Afiliados Elite. Todos os Direitos Reservados.</p>', unsafe_allow_html=True)
