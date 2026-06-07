import streamlit as st
import pandas as pd
import time
import re

# Configuração premium de layout amplo Black para o Ativador Inteligente Completo
st.set_page_config(page_title="Adriel AI - Google Ads Suite Pro", layout="wide")

# INJEÇÃO DE CÓDIGO CSS PREMIUM DEFINITIVO (BOTÕES NEON PERSONALIZADOS DE LUXO)
st.markdown("""
<style>
    /* Estilo para Botão Principal de Transmissão / Ativação (Verde/Ciano) */
    button[kind="primary"], .stButton > button {
        background: linear-gradient(135deg, #00FF87 0%, #60EFFF 100%) !important;
        color: #121212 !important;
        font-size: 18px !important;
        font-weight: bold !important;
        padding: 14px 45px !important;
        border-radius: 14px !important;
        border: none !important;
        box-shadow: 0px 5px 20px rgba(0, 255, 135, 0.4) !important;
        transition: all 0.3s ease-in-out !important;
        width: 100% !important;
        cursor: pointer !important;
    }
    button[kind="primary"]:hover, .stButton > button:hover {
        background: linear-gradient(135deg, #60EFFF 0%, #00FF87 100%) !important;
        transform: translateY(-2px) !important;
        box-shadow: 0px 8px 25px rgba(0, 255, 135, 0.7) !important;
        color: #121212 !important;
    }
</style>
""", unsafe_allow_html=True)

st.title("🚀 MÓDULO 6: CENTRAL DE CONSTRUÇÃO E ATIVAÇÃO DIRETA (GOOGLE ADS API)")
st.markdown("Monte sua campanha, gerencie credenciais, verifique políticas anti-bloqueio e publique direto no Google Ads na mesma tela.")
st.write("---")

# Inicialização das chaves dinâmicas na memória persistente para suportar a reedição estável
if "t1_val" not in st.session_state: st.session_state.t1_val = "Citrus Burn Official Website"
if "t2_val" not in st.session_state: st.session_state.t2_val = "Buy Citrus Burn Online"
if "t3_val" not in st.session_state: st.session_state.t3_val = "Original Citrus Burn Formula"
if "d1_val" not in st.session_state: st.session_state.d1_val = "Order Citrus Burn from the official website today and get exclusive package discounts."
if "d2_val" not in st.session_state: st.session_state.d2_val = "Get the original product with a 100% 60-day money-back guarantee. Secure checkout."

# =============================================================================================================
# SEÇÃO 1: CREDENCIAIS E BOTÃO DE INTEGRAÇÃO COM A API DO GOOGLE
# =============================================================================================================
st.markdown("### 🔑 1. AUTENTICAÇÃO E CONEXÃO COM GOOGLE ADS API")
col_c1, col_c2 = st.columns(2)
with col_c1:
    customer_id = st.text_input("Google Ads Customer ID (Apenas números):", value="1234567890")
    produto_input = st.text_input("Nome do Produto Gringo:", value="Citrus Burn")
with col_c2:
    developer_token = st.text_input("Chave Developer Token (API):", value="API_DEVELOPER_TOKEN_SECURE", type="password")
    pais_alvo = st.selectbox("País Alvo do Leilão (GEO):", ["Estados Unidos 🇺🇸", "Reino Unido 🇬🇧", "Irlanda 🇮🇪", "Canadá 🇨🇦", "Austrália 🇦🇺"])

st.write("")
# Botão Secundário Customizado em HTML/CSS para Conexão da API
st.markdown("""
<div style="text-align: center; margin-bottom: 20px;">
    <span style="background: linear-gradient(135deg, #007BFF 0%, #00E5FF 100%); color: white; padding: 12px 35px; font-weight: bold; border-radius: 10px; box-shadow: 0px 4px 15px rgba(0, 229, 255, 0.3); font-size: 16px; cursor: pointer; display: inline-block;">
        🔗 INTERLIGAR CONTA COM O GOOGLE ADS VIA API
    </span>
</div>
""", unsafe_allow_html=True)

st.write("---")

# =============================================================================================================
# SEÇÃO 2: ORÇAMENTO E LANCES
# =============================================================================================================
st.markdown("### 💰 2. CONFIGURAÇÃO FINANCEIRA DE LANCES (BID)")
col_b1, col_b2 = st.columns(2)
with col_b1:
    orcamento_diario = st.number_input("Orçamento Diário de Escala ($):", value=20.0, step=5.0)
with col_b2:
    cpc_maximo = st.number_input("Limite Máximo de Custo por Clique (CPC Max $):", value=0.65, step=0.05)

st.write("---")

# =============================================================================================================
# SEÇÃO 3: PALAVRAS-CHAVE COMPLETA
# =============================================================================================================
st.markdown("### 🎯 3. ENGENHARIA DE PALAVRAS-CHAVE DO GRUPO DE ANÚNCIOS")
prod = produto_input.strip()

col_kw1, col_kw2 = st.columns(2)
with col_kw1:
    lista_frase = f'"{prod} official website"\n"buy {prod} online"\n"{prod} discount price"'
    kw_frase = st.text_area("✏️ Palavras-Chave de Frase (Use aspas):", value=lista_frase, height=130)
with col_kw2:
    lista_negativas = "scam\ncomplaints\ningredients\nside effects\nrefund"
    kw_negativa = st.text_area("✏️ Palavras-Chave Negativas de Segurança:", value=lista_negativas, height=130)

st.write("---")

# =============================================================================================================
# SEÇÃO 4: CONFIGURAÇÃO DE TEXTOS DO ANÚNCIO (RSA)
# =============================================================================================================
st.markdown("### 📝 4. REDAÇÃO DO ANÚNCIO RESPONSIVO (RSA) & PROTOCOLO DE COMPLIANCE")

col_t1, col_t2 = st.columns(2)
with col_t1:
    t1 = st.text_input("Título Principal 1 (Pin 1):", value=st.session_state.t1_val, key="t1_box")
    t2 = st.text_input("Título Principal 2 (Pin 2):", value=st.session_state.t2_val, key="t2_box")
    t3 = st.text_input("Título Principal 3 (Pin 3):", value=st.session_state.t3_val, key="t3_box")
with col_t2:
    d1 = st.text_input("Descrição do Anúncio (Máx 90 letras):", value=st.session_state.d1_val, max_chars=90, key="d1_box")
    d2 = st.text_input("Descrição Secundária:", value=st.session_state.d2_val, max_chars=90, key="d2_box")

# Atualiza os estados na memória a cada modificação na tela
st.session_state.t1_val, st.session_state.t2_val, st.session_state.t3_val = t1, t2, t3
st.session_state.d1_val, st.session_state.d2_val = d1, d2

st.write("---")

# =============================================================================================================
# SEÇÃO 5: SCANNER DE POLÍTICAS REAL-TIME E AUTOCORREÇÃO IMEDIATA
# =============================================================================================================
st.markdown("#### 🔍 DIAGNÓSTICO DO RASTREADOR DE POLÍTICAS (RAIO-X DE BLOQUEIO)")

regras_correcao = {
    "cure": "support formula",
    "heals": "supports health",
    "weight loss instantly": "natural weight support",
    "guaranteed results": "satisfaction guarantee",
    "anxiety cure": "calm support ritual",
    "treat disease": "promote wellness lifestyle"
}

texto_completo_original = (t1 + " " + t2 + " " + t3 + " " + d1 + " " + d2).lower()

violacao_termo = False
violacao_capital = False
gatilho_detalhado = ""

# Varre caçando termos médicos proibidos exatos e isolados
for termo_ruim in regras_correcao.keys():
    padrao_palavra_exata = r'\b' + re.escape(termo_ruim) + r'\b'
    if re.search(padrao_palavra_exata, texto_completo_original):
        violacao_termo = True
        gatilho_detalhado = termo_ruim
        break
        
# Varre caçando letras maiúsculas proibidas
letras_grandes = re.findall(r'\b[A-Z]{3,}\b', t1 + " " + t2 + " " + t3)
if not violacao_termo and letras_grandes:
    violacao_capital = True
    gatilho_detalhado = f"Letras Maiúsculas Abusivas: {letras_grandes}"

if violacao_termo or violacao_capital:
    st.error(f"❌ RISCO DE BLOQUEIO DETECTADO! Motivo: '{gatilho_detalhado}'. Esta estrutura quebra as regras do Google Ads.")
    st.markdown("**💡 O Robô Adriel AI estruturou a correção segura para você. Clique abaixo para aplicar:**")
    if st.button("⚡ CORRIGIR TEXTO AUTOMATICAMENTE (ANTI-BLOQUEIO)", key="btn_autocorrect"):
        for ruim, seguro in regras_correcao.items():
            padrao_sub = r'\b' + re.escape(ruim) + r'\b'
            st.session_state.t1_val = re.sub(padrao_sub, seguro, st.session_state.t1_val, flags=re.IGNORECASE)
            st.session_state.t2_val = re.sub(padrao_sub, seguro, st.session_state.t2_val, flags=re.IGNORECASE)
            st.session_state.t3_val = re.sub(padrao_sub, seguro, st.session_state.t3_val, flags=re.IGNORECASE)
            st.session_state.d1_val = re.sub(padrao_sub, seguro, st.session_state.d1_val, flags=re.IGNORECASE)
            st.session_state.d2_val = re.sub(padrao_sub, seguro, st.session_state.d2_val, flags=re.IGNORECASE)
        if violacao_capital:
            st.session_state.t1_val = st.session_state.t1_val.title()
            st.session_state.t2_val = st.session_state.t2_val.title()
            st.session_state.t3_val = st.session_state.t3_val.title()
        st.success("🔄 Ajuste de Compliance concluído com sucesso!")
        time.sleep(0.3)
        st.rerun()
    botao_bloqueado = True
else:
    st.success("✅ ANÚNCIO 100% LIMPO! Nenhuma violação editorial encontrada nos criativos. Padrão de conformidade anti-bloqueio atingido!")
    botao_bloqueado = False

st.write("---")

# Gráfico de barras verticais ciano na largura total da tela
st.markdown("### 📊 Histórico Volumétrico Estimado Pré-Upload")
meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
valores_envio = [180 + (i * 75) for i in range(12)]
df_envio = pd.DataFrame({"Volume Analisado": valores_envio}, index=meses)
st.bar_chart(df_envio, use_container_width=True, color="#00E5FF")

st.write("---")

# =============================================================================================================
# SEÇÃO 6: DISPARO REAL DA CAMPANHA VIA API DIRETO PARA O GOOGLE ADS
# =============================================================================================================
st.markdown("### 🚀 5. TRANSMISSÃO DA CAMPANHA CONFIGURADA")
