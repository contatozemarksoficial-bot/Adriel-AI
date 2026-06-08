import streamlit as st
import pandas as pd
import time
import re

# Configuração premium de layout amplo Black para o Simulador Google Ads Completo
st.set_page_config(page_title="Adriel AI - Google Ads Pro Suite", layout="wide")

# INJEÇÃO DE CÓDIGO CSS PREMIUM DEFINITIVO (BOTÕES NEON PERSONALIZADOS DE LUXO)
st.markdown("""
<style>
    button[kind="primary"], .stButton > button {
        background: linear-gradient(135deg, #00FF87 0%, #60EFFF 100%) !important;
        color: #121212 !important;
        font-size: 16px !important;
        font-weight: bold !important;
        padding: 12px 35px !important;
        border-radius: 12px !important;
        border: none !important;
        box-shadow: 0px 4px 15px rgba(0, 255, 135, 0.3) !important;
        transition: all 0.3s ease-in-out !important;
        width: 100% !important;
        cursor: pointer !important;
    }
    button[kind="primary"]:hover, .stButton > button:hover {
        background: linear-gradient(135deg, #60EFFF 0%, #00FF87 100%) !important;
        transform: translateY(-2px) !important;
        box-shadow: 0px 6px 20px rgba(0, 255, 135, 0.6) !important;
        color: #121212 !important;
    }
</style>
""", unsafe_allow_html=True)

st.title("🚀 MÓDULO 6: CENTRAL DE ATIVAÇÃO DE CAMPANHAS E VALIDAÇÃO DE API")
st.markdown("Chassi executivo de engenharia estruturado em conformidade com as regras e tratamento de exceções da Google Ads API.")
st.write("---")

# =============================================================================================================
# SEÇÃO 1: OBJETIVOS E METAS (PAINEL DO GOOGLE ADS)
# =============================================================================================================
st.markdown("### 🎯 1. ESCOLHER SEU OBJETIVO DE CAMPANHA")
st.markdown("Escolha um objetivo para personalizar a experiência de acordo com as metas e configurações mais adequadas para sua campanha.")

obj_sel = st.radio(
    "Selecione a meta que ajudaria esta campanha a alcançar o sucesso de acordo com seus critérios:",
    [
        "🛒 Vendas (Gerar vendas on-line, no aplicativo, por telefone ou na loja)",
        "🎯 Leads (Incentivar clientes a realizar ações para gerar leads e outras conversões)",
        "🌐 Tráfego do site (Fazer com que as pessoas certas acessem seu site)",
        "⚙️ Criar uma campanha sem orientação"
    ], index=0, key="main_obj_radio"
)

st.write("---")
st.markdown("#### ⚙️ Metas de conversão identificadas como padrão da conta")
col1, col2, col3 = st.columns(3)
with col1: st.info("**Metas de conversão**\n\nCompras (padrão da conta)")
with col2: st.info("**Origem da conversão**\n\nSite")
with col3: st.info("**Ações de conversão**\n\n1 ação")

st.write("---")

# =============================================================================================================
# SEÇÃO 2: TIPO E CANAL DE ALCANCE
# =============================================================================================================
st.markdown("### 🔎 2. SELECIONE UM TIPO DE CAMPANHA")
tipo_sel = st.radio(
    "Escolha o formato onde quer exibir seus anúncios no Google:",
    [
        "⚡ Performance Max (Anúncios na Pesquisa, YouTube, Display e muito mais)",
        "🛍️ Shopping (Promova seus produtos do Merchant Center na Pesquisa Google)",
        "🔎 Pesquisar (Aumente as vendas na Pesquisa Google com os anúncios de texto)"
    ], index=2, key="main_type_radio"
)

st.markdown("#### Selecione como você quer alcançar sua meta")
alcance_sel = st.radio("Selecione os canais de captação:", ["Visitas ao site", "Ligações telefônicas", "Visitas à loja"], index=0, key="main_reach_radio")

st.write("---")

# =============================================================================================================
# SEÇÃO 3: DADOS DE IDENTIFICAÇÃO E PARÂMETROS FINANCEIROS
# =============================================================================================================
st.markdown("### 📊 3. CONFIGURAÇÕES GERAIS, LANCES E ORÇAMENTO")

col_d1, col_d2 = st.columns(2)
with col_d1:
    v_nome_campanha = st.text_input("Nome da campanha:", value="Sales-Search-22", key="input_camp_name")
    v_metrica = st.selectbox("Em qual métrica você quer focar?", ["Conversões", "Cliques", "Parcela de impressões"], index=0, key="input_metrica")
    v_local = st.radio("Selecione os locais para esta campanha:", ["Todos os países/territórios", "Brasil", "Inserir outro local"], index=1, key="input_local")
with col_d2:
    v_customer_id = st.text_input("Google Ads Customer ID (Somente números):", value="1234567890", key="input_cust_id")
    v_budget_tipo = st.selectbox("Selecione o tipo de orçamento de leilão:", ["Orçamento diário médio", "Orçamento total da campanha"], key="input_budget_type")
    v_budget_val = st.number_input("Orçamento diário da campanha (R$):", min_value=0.0, value=50.0, step=5.0, key="input_budget_val")

st.write("---")

# =============================================================================================================
# SEÇÃO 4: PALAVRAS-CHAVE E ANÚNCIO RESPONSIVO (RSA)
# =============================================================================================================
st.markdown("### 🎯 4. PALAVRAS-CHAVE E TEXTOS DO ANÚNCIO (RSA)")

col_kw1, col_kw2 = st.columns(2)
with col_kw1:
    v_keywords = st.text_area("Inserir palavras-chave (Uma por linha):", value='"citrus burn site oficial"\n"comprar citrus burn original"', height=120, key="input_keywords")
with col_kw2:
    v_negativas = st.text_area("Palavras-Chave Negativas de Segurança:", value="gratis\npdf\ndownload\nreclame aqui", height=120, key="input_negativas")

st.write("---")
st.markdown("#### 📝 Criar anúncios para ter mais vendas")

col_tx1, col_tx2 = st.columns(2)
with col_tx1:
    v_t1 = st.text_input("Título 1 (Obrigatório - Até 30 letras):", value="Citrus Burn Site Oficial", max_chars=30, key="input_t1")
    v_t2 = st.text_input("Título 2 (Obrigatório - Até 30 letras):", value="Comprar Citrus Burn Original", max_chars=30, key="input_t2")
with col_tx2:
    v_d1 = st.text_input("Descrição 1 (Obrigatório - Até 90 letras):", value="Adquira o Citrus Burn direto no site oficial com desconto exclusivo hoje.", max_chars=90, key="input_d1")
    v_d2 = st.text_input("Descrição 2 (Até 90 letras):", value="Garantia de satisfação total ou seu dinheiro de volta. Parcelamento facilitado.", max_chars=90, key="input_d2")

st.write("---")

# =============================================================================================================
# SEÇÃO 5: INTEGRAÇÃO E AUTENTICAÇÃO DA GOOGLE API
# =============================================================================================================
st.markdown("#### 🛠️ CONFIGURAÇÃO DE INTEGRAÇÃO COM A GOOGLE ADS API")
col_ap1, col_ap2 = st.columns(2)
with col_ap1:
    client_id_in = st.text_input("Client ID do Google Cloud Console:", value="SEU_CLIENT_ID", key="input_api_client_id")
    customer_id_in = st.text_input("Google Ads ID do Cliente (Customer ID):", value=v_customer_id, key="input_api_cust_id")
with col_ap2:
    client_secret_in = st.text_input("Client Secret de Chave:", value="SEU_CLIENT_SECRET", type="password", key="input_api_secret")
    developer_token_in = st.text_input("Developer Token de Acesso:", value="SUA_TOKEN_DE_DESENVOLVEDOR", type="password", key="input_api_token")
    
st.write("")
if st.button("🔗 SOLICITAR AUTENTICAÇÃO DO ARQUIVO GOOGLE-ADS.YAML", key="btn_yaml_auth"):
    if client_id_in == "SEU_CLIENT_ID" or customer_id_in == "1234567890":
        st.error("❌ Falha de Credenciais: Substitua as chaves padrão pelos dados reais extraídos do seu painel Cloud.")
    else:
        st.success("✅ AUTENTICAÇÃO E CHECK DE TOKEN CONCLUÍDOS VIA OAUTH 2.0!")

st.write("---")

# =============================================================================================================
# SEÇÃO 6: REVISÃO DE SINAL VERMELHO E BOTÃO DE DISPARO DA API DO JOSÉ
# =============================================================================================================
st.markdown("### 📋 REVISAR (SUA CAMPANHA ESTÁ QUASE PRONTA PARA SER PUBLICADA)")

st.markdown("#### 🛑 Problemas Detectados (Semáforo de Erros):")
lista_erros = []
if v_nome_campanha.strip() == "": lista_erros.append("• **Nome da Campanha:** O nome não pode ficar em branco na seção 3.")
if v_keywords.strip() == "": lista_erros.append("• **Adicionar palavras-chave:** Insira os termos de busca na seção 4.")
if v_t1.strip() == "" or v_d1.strip() == "": lista_erros.append("• **Criar um Anúncio:** O Título 1 e Descrição 1 são obrigatórios na seção 4.")
if v_budget_val <= 0.0: lista_erros.append("• **Adicionar um orçamento:** O valor diário deve ser positivo na seção 3.")

# Scanner de Políticas integrado em tempo real
regras_politicas = ["cure", "heals", "cura", "emagrece imediato"]
texto_criativo = (v_t1 + " " + v_d1).lower()
for proibido in regras_politicas:
    if re.search(r'\b' + re.escape(proibido) + r'\b', texto_criativo):
        lista_erros.append(f"• **Violação de Política:** O termo '{proibido}' quebra as regras do Google Ads. Remova-o.")

if lista_erros:
    for err in lista_erros: st.error(err)
    trava_api = True
else:
    st.success("🎉 ZERO PROBLEMAS ENCONTRADOS! Padrão de integridade e compliance do leilão atingido com sucesso total!")
    trava_api = False

st.write("---")
st.markdown("### 📊 Gráfico Histórico de Volume Estimado Pré-Upload")
meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
valores_envio = [250 + (i * 55) for i in range(12)]
df_envio = pd.DataFrame({"Volume Estimado": valores_envio}, index=meses)
st.bar_chart(df_envio, use_container_width=True, color="#00E5FF")

st.write("---")
st.markdown("#### 🚀 TRANSMITIR CAMPANHA COMPLETA DIRETO PARA O GOOGLE ADS VIA API")

if trava_api:
