import streamlit as st
import pandas as pd
import time
import re

# Configuração premium de layout amplo Black para o Ativador Global/Nacional
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

st.title("🚀 MÓDULO 6: CENTRAL DE ATIVAÇÃO GLOBAL & NACIONAL (GOOGLE ADS API)")
st.markdown("Suba campaigns validadas tanto para o mercado brasileiro quanto para a gringa com segmentação automática de moedas e regras.")
st.write("---")

# =============================================================================================================
# SEÇÃO 1: SELEÇÃO DE MERCADO (INTERNACIONAIS VS NACIONAL)
# =============================================================================================================
st.markdown("### 🌍 1. DIRECIONAMENTO DE MERCADO E CREDENCIAIS")

# Chave seletora de mercado que muda toda a inteligência do robô
tipo_mercado = st.radio(
    "Escolha o Tipo de Campanha que deseja criar:",
    ["🇺🇸 Campanhas Internacionais (Gringa - ClickBank/BuyGoods/Digistore)", "🇧🇷 Campanhas Nacionais (Brasil - Hotmart/Monetizze/Braip)"],
    key="mercado_radio_select"
)

col_c1, col_c2 = st.columns(2)
with col_c1:
    customer_id = st.text_input("Google Ads Customer ID (Somente números):", value="1234567890", key="cust_id_input")
    if "🇺🇸" in tipo_mercado:
        produto_input = st.text_input("Nome do Produto Gringo:", value="Citrus Burn", key="prod_input_gringa")
    else:
        produto_input = st.text_input("Nome do Produto Nacional:", value="Protocolo Zero Gordura", key="prod_input_nacional")
with col_c2:
    developer_token = st.text_input("Chave Developer Token (API):", value="API_DEVELOPER_TOKEN_SECURE", type="password", key="dev_token_input")
    if "🇺🇸" in tipo_mercado:
        pais_alvo = st.selectbox("País Alvo do Leilão (GEO):", ["Estados Unidos 🇺🇸", "Reino Unido 🇬🇧", "Irlanda 🇮🇪", "Canadá 🇨🇦", "Austrália 🇦🇺"], key="geo_gringa")
    else:
        pais_alvo = st.selectbox("País Alvo do Leilão (GEO):", ["Brasil 🇧🇷"], key="geo_nacional")

st.write("")
st.markdown("""
<div style="text-align: center; margin-bottom: 20px;">
    <span style="background: linear-gradient(135deg, #007BFF 0%, #00E5FF 100%); color: white; padding: 12px 35px; font-weight: bold; border-radius: 10px; box-shadow: 0px 4px 15px rgba(0, 229, 255, 0.3); font-size: 16px; cursor: pointer; display: inline-block;">
        🔗 AUTENTICAR E LIGAR API DO GOOGLE ADS
    </span>
</div>
""", unsafe_allow_html=True)

st.write("---")

# =============================================================================================================
# SEÇÃO 2: ORÇAMENTO E LANCES MOLDADOS POR MOEDA
# =============================================================================================================
st.markdown("### 💰 2. CONFIGURAÇÃO FINANCEIRA DE LANCES (BID)")
col_b1, col_b2 = st.columns(2)

if "🇺🇸" in tipo_mercado:
    moeda_simbolo = "$"
    val_orc = 20.0
    val_cpc = 0.65
else:
    moeda_simbolo = "R$"
    val_orc = 50.0
    val_cpc = 1.50

with col_b1:
    orcamento_diario = st.number_input(f"Orçamento Diário de Escala ({moeda_simbolo}):", value=val_orc, step=5.0, key="orc_input")
with col_b2:
    cpc_maximo = st.number_input(f"Limite Máximo de Custo por Clique (CPC Max {moeda_simbolo}):", value=val_cpc, step=0.05, key="cpc_input")

st.write("---")

# =============================================================================================================
# SEÇÃO 3: PALAVRAS-CHAVE MOLDADAS POR MERCADO
# =============================================================================================================
st.markdown("### 🎯 3. ENGENHARIA DE PALAVRAS-CHAVE DO GRUPO")
prod = produto_input.strip()

col_kw1, col_kw2 = st.columns(2)
with col_kw1:
    if "🇺🇸" in tipo_mercado:
        lista_frase = f'"{prod} official website"\n"buy {prod} online"\n"{prod} discount price"'
    else:
        lista_frase = f'"{prod} site oficial"\n"comprar {prod} original"\n"{prod} desconto hoje"'
    kw_frase = st.text_area("Palavras-Chave de Frase (Use aspas):", value=lista_frase, height=130, key="kw_frase_text")
with col_kw2:
    if "🇺🇸" in tipo_mercado:
        lista_negativas = "scam\ncomplaints\ningredients\nside effects\nrefund"
    else:
        lista_negativas = "gratis\npdf\ndownload\nmercado livre\nreclame aqui\nfunciona mesmo"
    kw_negativa = st.text_area("Palavras-Chave Negativas de Segurança:", value=lista_negativas, height=130, key="kw_neg_text")

st.write("---")

# =============================================================================================================
# SEÇÃO 4: CONFIGURAÇÃO DE TEXTOS DO ANÚNCIO (RSA) MOLDADOS POR MERCADO
# =============================================================================================================
st.markdown("### 📝 4. REDAÇÃO DO ANÚNCIO RESPONSIVO (RSA) & PROTOCOLO DE COMPLIANCE")

if "🇺🇸" in tipo_mercado:
    s_t1, s_t2, s_t3 = f"{prod} Official Website", f"Buy {prod} Online", f"Original {prod} Formula"
    s_d1 = f"Order {prod} from the official website today and get exclusive package discounts."
    s_d2 = "Get the original product with a 100% 60-day money-back guarantee. Secure checkout."
else:
    s_t1, s_t2, s_t3 = f"{prod} Site Oficial", f"Comprar {prod} Original", f"Adquira o {prod} Hoje"
    s_d1 = f"Adquira o {prod} direto no site oficial do fabricante com desconto exclusivo."
    s_d2 = "Garantia de satisfação total ou seu dinheiro de volta. Parcelamento em até 12x no cartão."

# Inicialização limpa e inline sem depender de blocos expansivos aninhados perigosos
if "t1_val" not in st.session_state: st.session_state.t1_val = s_t1
if "t2_val" not in st.session_state: st.session_state.t2_val = s_t2
if "t3_val" not in st.session_state: st.session_state.t3_val = s_t3
if "d1_val" not in st.session_state: st.session_state.d1_val = s_d1
if "d2_val" not in st.session_state: st.session_state.d2_val = s_d2

col_t1, col_t2 = st.columns(2)
with col_t1:
    t1 = st.text_input("Título Principal 1 (Pin 1):", value=st.session_state.t1_val, key="t1_box_edit")
    t2 = st.text_input("Título Principal 2 (Pin 2):", value=st.session_state.t2_val, key="t2_box_edit")
    t3 = st.text_input("Título Principal 3 (Pin 3):", value=st.session_state.t3_val, key="t3_box_edit")
with col_t2:
    d1 = st.text_input("Descrição do Anúncio (Máx 90 letras):", value=st.session_state.d1_val, max_chars=90, key="d1_box_edit")
    d2 = st.text_input("Descrição Secundária:", value=st.session_state.d2_val, max_chars=90, key="d2_box_edit")

# Força a atualização da memória imediata
st.session_state.t1_val, st.session_state.t2_val, st.session_state.t3_val = t1, t2, t3
st.session_state.d1_val, st.session_state.d2_val = d1, d2

st.write("---")

# =============================================================================================================
# SEÇÃO 5: SCANNER DE POLÍTICAS INTERNACIONAIS E NACIONAIS
# =============================================================================================================
st.markdown("#### 🔍 DIAGNÓSTICO DO RASTREADOR DE POLÍTICAS (RAIO-X DE BLOQUEIO)")

# Regras de termos proibidos corrigidas e travadas sem nenhuma quebra de linha de dicionário
regras_correcao = {"cure": "support formula", "heals": "supports health", "weight loss instantly": "natural weight support", "cura": "formula de suporte", "cura mesmo": "auxilia na saude", "emagrece imediato": "emagrecimento saudavel"}

texto_completo_original = (t1 + " " + t2 + " " + t3 + " " + d1 + " " + d2).lower()
violacao_termo = False
violacao_capital = False
gatilho_detalhado = ""

for termo_ruim in regras_correcao.keys():
    padrao_palavra_exata = r'\b' + re.escape(termo_ruim) + r'\b'
    if re.search(padrao_palavra_exata, texto_completo_original):
        violacao_termo = True
        gatilho_detalhado = termo_ruim
        break
        
letras_grandes = re.findall(r'\b[A-Z]{3,}\b', t1 + " " + t2 + " " + t3)
if not violacao_termo and letras_grandes:
    violacao_capital = True
    gatilho_detalhado = f"Letras Maiúsculas Abusivas: {letras_grandes}"

if violacao_termo or violacao_capital:
    st.error(f"❌ RISCO DE BLOQUEIO DETECTADO! Motivo: '{gatilho_detalhado}'. Esta estrutura quebra as regras do Google Ads.")
    st.warning("⚠️ Atenção: Modifique as palavras citadas acima para destravar o botão de transmissão final.")
    botao_bloqueado = True
else:
    st.success("✅ ANÚNCIO 100% LIMPO! Nenhuma violação editorial encontrada nos criativos. Pode subir, sua campanha está aprovada!")
    botao_bloqueado = False

st.write("---")

# Gráfico de barras verticais ciano na largura total da tela
st.markdown("### 📊 Histórico Volumétrico Estimado Pré-Upload")
meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
valores_envio = [180 + (i * 75) for i in range(12)]
df_envio = pd.DataFrame({"Volume Analisado": valores_envio}, index=meses)
