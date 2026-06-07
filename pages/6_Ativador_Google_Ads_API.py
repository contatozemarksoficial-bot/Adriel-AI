import streamlit as st
import pandas as pd
import time

# Configuração de layout amplo e profissional Black para o Simulador Google Ads Inteligente
st.set_page_config(page_title="Adriel AI - Google Ads Pro", layout="wide")

# INJEÇÃO DE CÓDIGO CSS PREMIUM DEFINITIVO (BOTÃO DE DISPARO REAL EM GRADIENTE VERDE)
st.markdown("""
<style>
    button[kind="primary"], .stButton > button {
        background: linear-gradient(135deg, #00FF87 0%, #60EFFF 100%) !important;
        color: #121212 !important;
        font-size: 18px !important;
        font-weight: bold !important;
        padding: 15px 45px !important;
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
    .stTabs [data-baseweb="tab"] {
        font-size: 16px !important;
        font-weight: bold !important;
    }
</style>
""", unsafe_allow_html=True)

st.title("🌐 PAINEL DE CONTROLE: GOOGLE ADS EXPRESS")
st.markdown("Crie, edite e publique sua campanha gringa através de uma interface simplificada interligada diretamente à API Oficial.")
st.write("---")

# =============================================================================================================
# CHASSI GERAL DE CREDENCIAIS (O PORTÃO DE ENTRADA DO CLIENTE)
# =============================================================================================================
st.markdown("### 🔑 CREDENCIAIS DO ANUNCIANTE")
col_cr1, col_cr2 = st.columns(2)
with col_cr1:
    customer_id = st.text_input("Google Ads Customer ID (Apenas números da conta):", value="1234567890")
with col_cr2:
    developer_token = st.text_input("Developer Token da API (Protegido):", value="API_DEVELOPER_TOKEN_SECURE", type="password")

st.write("---")
st.markdown("### 🛠️ CONFIGURAÇÃO DE CAMPANHA (ESTILO GOOGLE ADS FACILITADO)")

# SEPARAÇÃO DO FLUXO COMPLETO POR ABAS EXATAS DO PAINEL DO GOOGLE
aba_campanha, aba_keywords, aba_anuncio = st.tabs([
    "⚙️ 1. Configurações da Campanha", 
    "🎯 2. Grupos & Palavras-Chave", 
    "📝 3. Criação do Anúncio (RSA)"
])

# -------------------------------------------------------------------------------------------------------------
# ABA 1: CONFIGURAÇÕES DA CAMPANHA
# -------------------------------------------------------------------------------------------------------------
with aba_campanha:
    st.markdown("#### 📊 Parâmetros de Nível de Campanha")
    col_c1, col_c2 = st.columns(2)
    
    with col_c1:
        nome_campanha = st.text_input("Nome da Campanha no Google Ads:", value="Campanha Gringa - Fundo de Funil Search")
        objetivo_meta = st.selectbox("Meta de Conversão da Campanha (Objective):", ["🛒 Vendas (Sales - Altamente Recomendado)", "🎯 Leads (Cadastros)", "🌐 Tráfego do Site"])
        tipo_rede = st.selectbox("Rede de Exibição (Networks):", ["🔎 Rede de Pesquisa do Google (Apenas Busca Oficial)", "📺 Rede de Display (Parceiros)", "🚀 Performance Max (PMax)"])
    
    with col_c2:
        produto_input = st.text_input("Produto Selecionado do Leilão:", value="Citrus Burn")
        pais_alvo = st.selectbox("Localização Geográfica Alvo (GEO):", ["Estados Unidos 🇺🇸", "Reino Unido 🇬🇧", "Irlanda 🇮🇪", "Canadá 🇨🇦", "Austrália 🇦🇺"])
        
        col_f1, col_f2 = st.columns(2)
        with col_f1:
            orcamento_diario = st.number_input("Orçamento Diário da Campanha ($):", value=20.0, step=5.0)
        with col_f2:
            cpc_maximo = st.number_input("Limite de Lance Máximo (CPC Max $):", value=0.65, step=0.05)

prod = produto_input.strip()

# -------------------------------------------------------------------------------------------------------------
# ABA 2: GRUPOS & PALAVRAS-CHAVE
# -------------------------------------------------------------------------------------------------------------
with aba_keywords:
    st.markdown("#### 🎯 Configuração do Grupo de Anúncios e Palavras-Chave de Intenção")
    nome_grupo = st.text_input("Nome do Grupo de Anúncios (Ad Group Name):", value="Ad Group 1 - Brand Keywords")
    
    st.write("---")
    st.markdown("💡 **Edite e personalize as caixas de termos abaixo antes do envio direto:**")
    
    col_kw1, col_kw2 = st.columns(2)
    with col_kw1:
        # Correspondência de Frase com no mínimo 20 sugestões dinâmicas editáveis
        lista_frase = (
            f'"{prod} official website"\n"buy {prod} online"\n"{prod} discount price"\n'
            f'"order {prod} online"\n"{prod} where to buy"\n"{prod} store"\n'
            f'"{prod} price"\n"{prod} buy"\n"{prod} reviews"\n"{prod} cost"\n'
            f'"{prod} supplement"\n"{prod} official store"\n"{prod} best price"\n'
            f'"secure {prod} order"\n"{prod} check out"\n"get {prod} online"\n'
            f'"purchase {prod} now"\n"{prod} coupon code"\n"{prod} special deal"\n"original {prod}"'
        )
        kw_frase = st.text_area("✏️ Palavras-Chave de Frase (Use aspas):", value=lista_frase, height=250)
        
        # Correspondência Exata com no mínimo 20 sugestões dinâmicas editáveis
        lista_exata = (
            f'[{prod} official website]\n[buy {prod} online]\n[{prod} discount price]\n'
            f'[order {prod} online]\n[{prod} where to buy]\n[{prod} store]\n'
            f'[{prod} price]\n[{prod} buy]\n[original {prod}]\n[{prod} cost]\n'
            f'[{prod} supplement]\n[{prod} official store]\n[{prod} best price]\n'
            f'[secure {prod} order]\n[{prod} check out]\n[get {prod} online]\n'
            f'[purchase {prod} now]\n[{prod} coupon code]\n[{prod} special deal]\n[{prod}]'
        )
        kw_exata = st.text_area("✏️ Palavras-Chave Exatas (Use colchetes):", value=lista_exata, height=250)
        
    with col_kw2:
        # Correspondência Ampla Livre com no mínimo 20 sugestões dinâmicas editáveis
        lista_ampla = (
            f'{prod} official site\nbuy {prod}\n{prod} store\norder {prod}\n{prod} discount\n'
            f'{prod} online\n{prod} website\npurchase {prod}\nprice of {prod}\noriginal {prod}\n'
            f'{prod} delivery\n{prod} supply\n{prod} shop\ncost of {prod}\n{prod} cost\n'
            f'get {prod}\n{prod} brand\nsafe {prod}\ngenuine {prod}\n{prod} manufacturing'
        )
        kw_ampla = st.text_area("✏️ Palavras-Chave Livres (Sem símbolos):", value=lista_ampla, height=250)
        
        # 30 Negativas de proteção cirúrgica de caixa editáveis
        lista_negativas = "scam\ncomplaints\ningredients\nside effects\nfree pdf\namazon\nwalmart\nebay\ndiscount code\ncoupon\ntarget\nrefund\nfake\nwholesale\ndepartment\nindependent review\ncustomer support number\nlogin\nfree trial\nbbb rating\nyoutube video\ndiagnosis\ntreatment\ncheap\nmedical advice\nsymptoms\nwhere to find cheap\nsideeffects\nbad reviews\nclinical trial history"
        kw_negativa = st.text_area("✏️ Palavras-Chave Negativas de Proteção (30 Termos):", value=lista_negativas, height=250)

# -------------------------------------------------------------------------------------------------------------
# ABA 3: CRIAÇÃO DO ANÚNCIO (RSA)
# -------------------------------------------------------------------------------------------------------------
with aba_anuncio:
    st.markdown("#### 📝 Criação do Anúncio Responsivo de Rede de Pesquisa (Responsive Search Ad)")
    
    caminho_1 = st.text_input("Caminho de Exibição 1 (Display Path - Até 15 letras):", value="Official")
    caminho_2 = st.text_input("Caminho de Exibição 2 (Display Path - Até 15 letras):", value="Store")
    
    st.write("---")
    st.markdown("**✏️ Edite os 15 Títulos Obrigatórios de Compliance (Máximo 30 caracteres por linha):**")
    
    col_t1, col_t2, col_t3 = st.columns(3)
    with col_t1:
        t1 = st.text_input("Headline 1 (Pin 1):", value=f"{prod} Official Website")
        t2 = st.text_input("Headline 2 (Pin 2):", value=f"Buy {prod} Online")
        t3 = st.text_input("Headline 3 (Pin 3):", value=f"Original {prod} Formula")
        t4 = st.text_input("Headline 4:", value=f"{prod} Best Price")
        t5 = st.text_input("Headline 5:", value=f"Order {prod} Today")
    with col_t2:
        t6 = st.text_input("Headline 6:", value=f"{prod} Premium Supplement")
        t7 = st.text_input("Headline 7:", value=f"{prod} Official Store")
        t8 = st.text_input("Headline 8:", value=f"Get {prod} Now")
        t9 = st.text_input("Headline 9:", value=f"{prod} Certified Product")
        t10 = st.text_input("Headline 10:", value=f"{prod} Special Discount")
    with col_t3:
        t11 = st.text_input("Headline 11:", value=f"{prod} Natural Blend")
        t12 = st.text_input("Headline 12:", value=f"Authentic {prod}")
        t13 = st.text_input("Headline 13:", value=f"Shop {prod} Direct")
        t14 = st.text_input("Headline 14:", value=f"{prod} Best Deal")
        t15 = st.text_input("Headline 15:", value=f"Secure {prod} Order")

    st.write("---")
    st.markdown("**✏️ Edite as Descrições Customizadas (Máximo 90 caracteres por linha):**")
    d1 = st.text_input("Description 1:", value=f"Order {prod} from the official website today and get exclusive package discounts.", max_chars=90)
    d2 = st.text_input("Description 2:", value=f"Get the original {prod} with a 100% 60-day money-back guarantee. Secure checkout.", max_chars=90)
    d3 = st.text_input("Description 3:", value=f"100% natural formula backed by clinical research. Fast shipping options available now.", max_chars=90)
    d4 = st.text_input("Description 4:", value=f"Save big on multi-bottle packages today. Enjoy secure checkout and fast delivery.", max_chars=90)

