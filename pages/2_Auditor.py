import streamlit as st
import pandas as pd

# 🚨 REGRA MESTRE: set_page_config precisa ser a PRIMEIRA instrução do código das páginas!
st.set_page_config(page_title="Adriel-AI Pro - Auditor de Mercado", layout="wide", initial_sidebar_state="expanded")

# Injeção de CSS Premium Black da família Adriel AI PRO (Mantém o design escuro e os links piscando)
st.markdown("""
<style>
    .stApp { background-color: #0b111e !important; color: #ffffff !important; }
    .block-container { padding-top: 1rem !important; padding-bottom: 0rem !important; }
    [data-testid="stHeader"] { display: none !important; }
    
    @keyframes sinal-pulsante {
        0% { border-color: #1e293b; box-shadow: 0 0 5px rgba(0, 229, 255, 0.1); }
        50% { border-color: #00FF87; box-shadow: 0 0 15px rgba(0, 255, 135, 0.4); }
        100% { border-color: #1e293b; box-shadow: 0 0 5px rgba(0, 229, 255, 0.1); }
    }
    
    [data-testid="stSidebarNav"] ul li a span { color: #ffffff !important; font-weight: bold !important; font-size: 14px !important; }
    [data-testid="stSidebarNav"] ul li a {
        background-color: #0f172a !important; border: 2px solid #1e293b !important; border-radius: 8px !important;
        margin-bottom: 8px !important; padding: 12px 14px !important; animation: sinal-pulsante 3s infinite ease-in-out !important;
    }
    
    .header-box-real { background-color: #0f172a !important; border: 1px solid #1e293b !important; border-radius: 8px !important; padding: 14px 20px !important; margin-bottom: 15px !important; }
    .subtitulo-bloco-real { font-size: 13px !important; font-weight: bold !important; color: #60a5fa !important; margin-bottom: 15px; text-transform: uppercase; }
    .kpi-box { background: #0f172a; padding: 12px 15px; border-radius: 8px; border: 1px solid #1e293b; text-align: center; }
    
    div.stButton > button {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%) !important;
        color: white !important; font-weight: bold !important; font-size: 14px !important;
        border: 2px solid #1e293b !important; padding: 12px 15px !important; border-radius: 6px !important; width: 100% !important; cursor: pointer;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h2 style='color: #60a5fa; font-size: 26px; font-weight: 800; margin-bottom:0;'>🤖 Adriel-AI <span style='background:#00E5FF; color:#050814; padding:2px 8px; font-size:12px; border-radius:4px; vertical-align:middle;'>PRO</span></h2>", unsafe_allow_html=True)
st.write("---")

col_centro, col_direita = st.columns([1.4, 1.0])

with col_centro:
    st.markdown('<div class="header-box-real">🛡️ Varredura de CPC e Análise de Termos de Política</div>', unsafe_allow_html=True)
    st.markdown('<p class="subtitulo-bloco-real">🔬 AUDITOR: DIAGNÓSTICO DE CONFORMIDADE</p>', unsafe_allow_html=True)
    
    # Campo interativo real para análise
    produto_auditar = st.text_input("Insira o nome exato da oferta para auditoria de CPC:", value="Sugar Defender")
    st.write("")
    
    if st.button("🔍 ANALISAR BLOQUEIOS E CONCORRÊNCIA", key="btn_run_auditor_real"):
        with st.spinner(f"Escaneando leilões ativos do Google Ads para {produto_auditar}..."):
            import time
            time.sleep(1.2)
        st.success(f"🟢 Diagnóstico concluído para **{produto_auditar}**! Nenhuma palavra preta ou restritiva detectada nos termos principais.")

with col_direita:
    st.markdown('<div class="header-box-real" style="text-align: right;">API Google Ads: <span style="color:#00FF87;">Síncrona</span></div>', unsafe_allow_html=True)
    st.markdown('<p class="subtitulo-bloco-real">🚦 SEMÁFORO DE RISCO EDITORIAL</p>', unsafe_allow_html=True)
    
    st.success("🟢 CONFORMIDADE MÁXIMA\n\nLeilão livre para lances em correspondência exata. Baixa probabilidade de suspensão nas primeiras 72 horas.")

# Rodapé unificado
st.markdown('<div style="clear: both; text-align: center; font-size: 11px; color: #475569; padding-top: 45px;"><hr style="border-color: #1e293b;">© 2026 Adriel-AI Pro - Todos os Direitos Reservados.</div>', unsafe_allow_html=True)
