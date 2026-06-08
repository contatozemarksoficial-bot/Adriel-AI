import streamlit as st

# =============================================================================================================
# CONSTANTES DE CONFIGURAÇÃO
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

# Configuração da página
st.set_page_config(page_title="Adriel AI - Google Ads Pro Suite", layout="wide")

# Estilo CSS
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

st.title("🚀 MÓDULO 6: CENTRAL DE CRIAÇÃO E ATIVAÇÃO (GOOGLE ADS API)")
st.markdown("Chassi sequencial de alta performance blindado com validações de dados e conformidade anti-bloqueios.")
st.write("---")

# =============================================================================================================
# GERENCIAMENTO DE ESTADO DE FLUXO
# =============================================================================================================
if "ads_passo" not in st.session_state:
    st.session_state.ads_passo = 1
if "v_objetivo" not in st.session_state:
    st.session_state.v_objetivo = "Vendas"
if "v_tipo" not in st.session_state:
    st.session_state.v_tipo = "Pesquisa"
if "v_alcance" not in st.session_state:
    st.session_state.v_alcance = "Visitas ao site"
if "v_nome_campanha" not in st.session_state:
    st.session_state.v_nome_campanha = "Sales-Search-22"
if "v_metrica" not in st.session_state:
    st.session_state.v_metrica = "Conversões"
if "v_local" not in st.session_state:
    st.session_state.v_local = "Todos os países/territórios"
if "v_idioma" not in st.session_state:
    st.session_state.v_idioma = "Português"
if "v_keywords" not in st.session_state:
    st.session_state.v_keywords = ""
if "v_budget_tipo" not in st.session_state:
    st.session_state.v_budget_tipo = "Orçamento diário médio"
if "v_budget_val" not in st.session_state:
    st.session_state.v_budget_val = 0.0

# Inicialização segura
for i in range(1, 8):
    chave_t =
