import streamlit as st
import pandas as pd
import time
import re

# Configuração premium de layout amplo Black para o Simulador Google Ads Completo
st.set_page_config(page_title="Adriel AI - Google Ads Pro", layout="wide")

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

st.title("🛰️ CONFIGURADOR EXECUTIVO: GOOGLE ADS WIZARD")
st.markdown("Interface idêntica à esteira de produção oficial do Google Ads para estruturação, auditoria e envio via API.")
st.write("---")

# Inicialização segura do controle de etapas na memória do servidor para continuidade real
if "ads_passo" not in st.session_state: st.session_state.ads_passo = 1

# Inicialização estável dos dados capturados das caixas para a tela de revisão final
if "v_objetivo" not in st.session_state: st.session_state.v_objetivo = "Vendas"
if "v_tipo" not in st.session_state: st.session_state.v_tipo = "Pesquisar"
if "v_alcance" not in st.session_state: st.session_state.v_alcance = "Visitas ao site"
if "v_nome_campanha" not in st.session_state: st.session_state.v_nome_campanha = "Sales-Search-22"
if "v_metrica" not in st.session_state: st.session_state.v_metrica = "Conversões"
if "v_local" not in st.session_state: st.session_state.v_local = "Todos os países/territórios"
if "v_idioma" not in st.session_state: st.session_state.v_idioma = "Português"
if "v_keywords" not in st.session_state: st.session_state.v_keywords = ""
if "v_budget_tipo" not in st.session_state: st.session_state.v_budget_tipo = "Orçamento diário médio"
if "v_budget_val" not in st.session_state: st.session_state.v_budget_val = 0.0

# Inicialização dos Títulos e Descrições do Anúncio Responsivo (RSA)
for i in range(1, 8):
    if f"v_t{i}" not in st.session_state: st.session_state.f"v_t{i}" = ""
for i in range(1, 3):
    if f"v_d{i}" not in st.session_state: st.session_state.f"v_d{i}" = ""

# Barra de progresso baseada na esteira oficial
st.progress((st.session_state.ads_passo - 1) / 6)
st.markdown(f"**Progresso da Campanha: Etapa {st.session_state.ads_passo} de 6**")
st.write("---")

# =============================================================================================================
# PASSO 1: ESCOLHER SEU OBJETIVO DE CAMPANHA & METAS DE CONVERSÃO
# =============================================================================================================
if st.session_state.ads_passo == 1:
    st.markdown("### 🎯 PASSO 1: ESCOLHER SEU OBJETIVO")
    st.markdown("Escolha um objetivo para personalizar a experiência de acordo com as metas e configurações mais adequadas para sua campanha.")
    
    obj_sel = st.radio(
        "Selecione a meta que ajudaria esta campanha a alcançar o sucesso de acordo com seus critérios:",
        [
            "Vendas (Gerar vendas on-line, no aplicativo, por telefone ou na loja)",
            "Leads (Incentivar clientes a realizar ações para gerar leads e outras conversões)",
            "Tráfego do site (Fazer com que as pessoas certas acessem seu site)",
            "Promoção de app (Gerar mais instalações, engajamentos e pré-registros para seu app)",
            "Alcance, visualizações e engajamentos do YouTube (Antes conhecido como 'Reconhecimento e consideração')",
            "Visitas a lojas locais e promoções (Impulsionar visitas a lojas locais, incluindo restaurantes e concessionárias)",
            "Criar uma campanha sem orientação (Em seguida, escolha um tipo de campanha)"
        ], index=0
    )
    
    st.write("---")
    st.markdown("#### ⚙️ Usar estas metas de conversão para melhorar Vendas")
    st.markdown("Metas de conversão identificadas como padrão da conta usarão dados de todas as suas campanhas para melhorar a estratégia de lances e o desempenho da campanha.")
    
    col1, col2, col3 = st.columns(3)
    with col1: st.info("**Metas de conversão**\n\nCompras (padrão da conta)")
    with col2: st.info("**Origem da conversão**\n\nSite")
    with col3: st.info("**Ações de conversão**\n\n1 ação")
    
    st.write("")
    if st.button("AVANÇAR PROXIO ➔", key="to_p2"):
        st.session_state.v_objetivo = "Vendas" if "Vendas" in obj_sel else "Outros"
        st.session_state.ads_passo = 2
        st.rerun()

# =============================================================================================================
# PASSO 2: SELECIOMAR TIPO DE CAMPANHA & COMO ALCANÇAR A META
# =============================================================================================================
elif st.session_state.ads_passo == 2:
    st.markdown("### 🔎 PASSO 2: SELECIONE UM TIPO DE CAMPANHA")
    
    tipo_sel = st.radio(
        "Escolha o modelo de campanha de leilão comercial:",
        [
            "Performance Max (Aumente as vendas alcançando as pessoas certas com anúncios na Pesquisa Google, YouTube e Display)",
            "Shopping (Promova seus produtos do Merchant Center na Pesquisa Google com anúncios do Shopping)",
            "Geração de demanda (Gere demanda e conversões no YouTube, na Rede de Display do Google com anúncios gráficos e em vídeo)",
            "Pesquisar (Aumente as vendas na Pesquisa Google com os anúncios de texto)",
            "Vídeo (Aumente as vendas no YouTube com seus anúncios em vídeo)",
            "Rede de Display (Alcance clientes em potencial em 3 milhões de sites e apps com seu criativo)"
        ], index=3
    )
    
    st.write("---")
    st.markdown("#### 🗺️ Selecione como você quer alcançar sua meta")
    alcance_sel = st.radio("Selecione os canais de captação:", ["Visitas ao site", "Ligações telefônicas", "Visitas à loja"], index=0)
    
    st.write("---")
    st.markdown("#### 📐 Identificação Base da Campanha")
    st.session_state.v_nome_campanha = st.text_input("Nome da campanha:", value=st.session_state.v_nome_campanha)

    st.write("")
    col_nav2 = st.columns(2)
    with col_nav2:
        if st.button("⬅ Voltar", key="back_to_1"):
            st.session_state.ads_passo = 1
            st.rerun()
    with col_nav2:
        if st.button("PROXIMO PASSO CONTINUA ➔", key="to_p3"):
            st.session_state.v_tipo = "Pesquisa" if "Pesquisar" in tipo_sel else "Outros"
            st.session_state.v_alcance = alcance_sel
            st.session_state.ads_passo = 3
            st.rerun()

# =============================================================================================================
# PASSO 3: LANCES FINANCEIROS & CONFIGURAÇÕES DA CAMPANHA (REDES, LOCAIS, IDIOMAS)
# =============================================================================================================
elif st.session_state.ads_passo == 3:
    st.markdown("### 💰 PASSO 3: LANCES E CONFIGURAÇÕES DA CAMPANHA")
    
    st.markdown("#### 📊 Lances")
    st.session_state.v_metrica = st.selectbox("Em qual métrica você quer focar?", ["Conversões", "Cliques", "Parcela de impressões"], index=0)
    st.checkbox("Definir um custo por ação desejado (opcional)", value=False)
    st.caption("ℹ️ Estratégias de lances alternativas, como portfólios, são disponibilizadas nas configurações depois que você cria sua campanha.")
    
    st.write("---")
    st.markdown("#### 👥 Aquisição do cliente")
    st.checkbox("Ajustar seus lances para conquistar novos clientes", value=True)
    st.caption("Por padrão, os lances da sua campanha são divididos igualmente entre os clientes novos e atuais. Mas você pode direcionar suas configurações de aquisição de clientes apenas para os novos.")
    
    st.write("---")
    st.markdown("#### 🌐 Configurações da campanha (Redes e Geotargeting)")
    st.checkbox("Rede de parceiros de pesquisa do Google (Recomendado)", value=True)
    st.checkbox("Rede de Display do Google (Recomendado)", value=False)
    
    st.write("---")
    st.markdown("#### 📍 Locais")
    st.session_state.v_local = st.radio("Selecione os locais para esta campanha:", ["Todos os países/territórios", "Brasil", "Inserir outro local"], index=0)
    
    st.write("---")
    st.markdown("#### 🗣️ Idiomas")
    st.session_state.v_idioma = st.selectbox("Selecione os idiomas que seus clientes falam:", ["Português", "Inglês", "Todos os idiomas"], index=2)
    
    st.write("---")
    st.markdown("#### 🇪🇺 Anúncios políticos na UE")
    st.radio("Sua campanha tem anúncios políticos na União Europeia? (Obrigatório)", ["Não, esta campanha não tem anúncios políticos na UE", "Sim, esta campanha tem anúncios políticos na UE"], index=0)

    st.write("")
    col_nav3 = st.columns(2)
    with col_nav3:
        if st.button("⬅ Voltar", key="back_to_2"):
            st.session_state.ads_passo = 2
            st.rerun()
    with col_nav3:
        if st.button("VEM AVANÇA ➔", key="to_p4"):
            st.session_state.ads_passo = 4
            st.rerun()

# =============================================================================================================
# PASSO 4: AI MAX PARA CAMPANHAS DE PESQUISA (A LOGÍSTICA INTELIGENTE DO GOOGLE)
# =============================================================================================================
elif st.session_state.ads_passo == 4:
