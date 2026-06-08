import streamlit as st
import pandas as pd
import time
import re

# =============================================================================================================
# CONSTANTES DE CONFIGURAÇÃO (Melhoria de Manutenibilidade e Consistência)
# =============================================================================================================
OBJETIVOS_CAMPANHA = [
    "Vendas (Gerar vendas on-line, no aplicativo, por telefone ou na loja)",
    "Leads (Incentivar clientes a realizar ações para gerar metas e cadastros)",
    "Tráfego do site (Fazer com que as pessoas certas acessem seu site)",
    "Promoção de app (Gerar mais instalações, engajamentos e pré-registros)",
    "Alcance, visualizações e engajamentos do YouTube (Reconhecimento de marca)",
    "Visitas a lojas locais e promoções (Impulsionar visitas a estabelecimentos)",
    "Criar uma campanha sem orientação (Fluxo livre customizado)"
]

TIPOS_CAMPANHA = [
    "Performance Max (Aumente as vendas alcançando as pessoas em todos os canais do Google)",
    "Shopping (Promova seus produtos do Merchant Center na Pesquisa Google)",
    "Geração de demanda (Gere conversões com anúncios gráficos e em vídeo)",
    "Pesquisar (Aumente as vendas na Pesquisa Google com os anúncios de texto)",
    "Vídeo (Aumente as vendas no YouTube com seus anúncios em vídeo)",
    "Rede de Display (Alcance clientes em potencial em 3 milhões de sites e apps)"
]

# Configuração premium de layout amplo Black para o Ativador Oficial Passo a Passo
st.set_page_config(page_title="Adriel AI - Google Ads Pro Suite", layout="wide")

# INJEÇÃO DE CÓDIGO CSS PREMIUM DEFINITIVO (BOTÕES NEON PERSONALIZADOS DE LUXO)
st.markdown("""
<style>
    /* Estilo para Botão Principal de Transmissão / Ativação (Verde/Ciano) */
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

st.title("🚀 MÓDULO 6: CENTRAL DE CRIAÇÃO E ATIVAÇÃO (GOOGLE ADS API)")
st.markdown("Chassi sequencial de alta performance blindado com validações de dados e conformidade anti-bloqueios.")
st.write("---")

# =============================================================================================================
# GERENCIAMENTO DE ESTADO DE FLUXO (Wizard estruturado para impedir perda de dados na re-renderização)
# =============================================================================================================
if "ads_passo" not in st.session_state: st.session_state.ads_passo = 1
if "v_objetivo" not in st.session_state: st.session_state.v_objetivo = "Vendas"
if "v_tipo" not in st.session_state: st.session_state.v_tipo = "Pesquisa"
if "v_alcance" not in st.session_state: st.session_state.v_alcance = "Visitas ao site"
if "v_nome_campanha" not in st.session_state: st.session_state.v_nome_campanha = "Sales-Search-22"
if "v_metrica" not in st.session_state: st.session_state.v_metrica = "Conversões"
if "v_local" not in st.session_state: st.session_state.v_local = "Todos os países/territórios"
if "v_idioma" not in st.session_state: st.session_state.v_idioma = "Português"
if "v_keywords" not in st.session_state: st.session_state.v_keywords = ""
if "v_budget_tipo" not in st.session_state: st.session_state.v_budget_tipo = "Orçamento diário médio"
if "v_budget_val" not in st.session_state: st.session_state.v_budget_val = 0.0

# Inicialização persistente das variáveis de criativos (RSA)
if "v_t1" not in st.session_state: st.session_state.v_t1 = ""
if "v_t2" not in st.session_state: st.session_state.v_t2 = ""
if "v_d1" not in st.session_state: st.session_state.v_d1 = ""

# Barra de progresso visual (Aprimoramento de UX para acompanhamento de etapas)
st.progress((st.session_state.ads_passo - 1) / 5)
st.markdown(f"**Progresso do Setup Google Ads: Passo {st.session_state.ads_passo} de 6**")
st.write("---")

# =============================================================================================================
# PASSO 1: ESCOLHER SEU OBJETIVO DE CAMPANHA & METAS DE CONVERSÃO
# =============================================================================================================
if st.session_state.ads_passo == 1:
    st.markdown("### 🎯 PASSO 1: ESCOLHER SEU OBJETIVO")
    st.markdown("Escolha um objetivo para personalizar a experiência de acordo com as metas e configurações mais adequadas para sua campanha.")
    
    obj_sel = st.radio(
        "Selecione a meta que ajudaria esta campanha a alcançar o sucesso de acordo com seus critérios:",
        OBJETIVOS_CAMPANHA, index=0
    )
    
    st.write("---")
    st.markdown("#### ⚙️ Usar estas metas de conversão para melhorar Vendas")
    st.markdown("Metas de conversão identificadas como padrão da conta usarão dados de todas as suas campanhas para melhorar a estratégia de lances e o desempenho da campanha.")
    
    col1, col2, col3 = st.columns(3)
    with col1: st.info("**Metas de conversão**\n\nCompras (padrão da conta)")
    with col2: st.info("**Origem da conversão**\n\nSite")
    with col3: st.info("**Ações de conversão**\n\n1 ação")
    
    st.write("")
    if st.button("PRÓXIMO PASSO ➔", key="to_p2"):
        st.session_state.v_objetivo = "Vendas" if "Vendas" in obj_sel else "Outros"
        st.session_state.ads_passo = 2
        st.rerun()

# =============================================================================================================
# PASSO 2: SELECIONAR TIPO DE CAMPANHA & VALIDAÇÃO DO NOME
# =============================================================================================================
elif st.session_state.ads_passo == 2:
    st.markdown("### 🔎 PASSO 2: SELECIONE UM TIPO DE CAMPANHA")
    
    tipo_sel = st.radio(
        "Escolha o formato onde quer exibir seus anúncios no Google:",
        TIPOS_CAMPANHA, index=3
    )
    
    st.write("---")
    # CORRIGIDO: Removida a duplicação de "####" apontada no feedback técnico
    st.markdown("#### Selecione como você quer alcançar sua meta")
    st.session_state.v_alcance = st.radio("Selecione os canais de captação desejados:", ["Visitas ao site", "Ligações telefônicas", "Visitas à loja"], index=0, help="Determina qual ação prioritária o lead deve executar.")
    
    st.write("---")
    st.markdown("#### 📐 Identificação Base da Campanha")
    st.session_state.v_nome_campanha = st.text_input("Nome da campanha:", value=st.session_state.v_nome_campanha, help="Insira uma identificação única para rastrear esta estrutura.")

    st.write("")
    col_nav2 = st.columns(2)
    with col_nav2:
        if st.button("⬅ Voltar", key="back_to_1"):
            st.session_state.ads_passo = 1
            st.rerun()
    with col_nav2:
        if st.button("PRÓXIMO PASSO ➔", key="to_p3"):
            # Validação crítica para impedir o avanço de campos em branco
            if st.session_state.v_nome_campanha.strip() == "":
                st.error("⚠️ Erro de Validação: Por favor, insira um nome válido para a campanha antes de prosseguir.")
            else:
                st.session_state.v_tipo = "Pesquisa" if "Pesquisar" in tipo_sel else "Outros"
                st.session_state.ads_passo = 3
                st.rerun()

# =============================================================================================================
# PASSO 3: ESTRATÉGIA DE LANCES (MÉTRICAS DO LEILÃO)
# =============================================================================================================
elif st.session_state.ads_passo == 3:
    st.markdown("### 💰 PASSO 3: ESTRATÉGIA DE LANCES DA CAMPANHA")
    
    st.markdown("#### 📊 Lances (Bidding)")
    st.session_state.v_metrica = st.selectbox(
        "Em qual métrica você quer focar?", 
        ["Conversões", "Cliques", "Parcela de impressões"], 
        index=0,
        help="Conversões (Foco em ROI e vendas). Cliques (Foco em volume de visitas brutas)."
    )
    st.checkbox("Definir um custo por ação desejado (opcional - CPA Desejado)", value=False, help="Limite o valor máximo pago por cada conversão identificada.")
    st.caption("ℹ️ Estratégias de lances alternativas, como portfólios, são disponibilizadas nas configurações depois que você cria sua campanha.")
    
    st.write("---")
    st.markdown("#### 👥 Aquisição do cliente")
    st.checkbox("Ajustar seus lances para conquistar novos clientes", value=True, help="Otimiza a veiculação prioritariamente para usuários que nunca acessaram seus domínios.")
    
    st.write("---")
    st.markdown("#### 🌐 Configurações de Redes de Destino")
    st.checkbox("Rede de parceiros de pesquisa do Google (Recomendado)", value=True, help="Exibe os anúncios em centenas de sites parceiros oficiais de busca do Google.")
    st.checkbox("Rede de Display do Google (Recomendado)", value=False, help="Exibe banners em sites e aplicativos parceiros quando houver verba disponível.")
    
    st.write("---")
    st.markdown("#### 📍 Locais e Idiomas")
    st.session_state.v_local = st.radio("Selecione os locais para esta campanha:", ["Todos os países/territórios", "Brasil", "Inserir outro local"], index=1)
    st.session_state.v_idioma = st.selectbox("Selecione os idiomas que seus clientes falam:", ["Português", "Inglês", "Todos os idiomas"], index=0)

