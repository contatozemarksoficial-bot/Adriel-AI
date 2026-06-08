import streamlit as st

# =============================================================================================================
# CONSTANTES DE CONFIGURAÇÃO
# =============================================================================================================
OBJETIVOS_CAMPANHA = [
    "Vendas",
    "Leads",
    "Tráfego do site",
    "Promoção de app",
    "Alcance do YouTube",
    "Visitas a lojas",
    "Criar uma campanha sem orientação"
]

TIPOS_CAMPANHA = [
    "Performance Max",
    "Shopping",
    "Geração de demanda",
    "Pesquisar",
    "Vídeo",
    "Rede de Display"
]

# Configuração do layout
st.set_page_config(page_title="Adriel AI - Google Ads Pro Suite", layout="wide")

# Gerenciamento de estado
if "ads_passo" not in st.session_state:
    st.session_state.ads_passo = 1
if "v_objetivo" not in st.session_state:
    st.session_state.v_objetivo = None  # Inicializar como None para evitar erros

# Barra de progresso
st.progress((st.session_state.ads_passo - 1) / 6)
st.markdown(f"**Progresso: Passo {st.session_state.ads_passo} de 6**")
st.write("---")

# Passo 1: Escolher objetivo
if st.session_state.ads_passo == 1:
    st.markdown("### 🎯 PASSO 1: ESCOLHER SEU OBJETIVO")
    obj_sel = st.radio("Selecione a meta:", OBJETIVOS_CAMPANHA)
    st.write("Objetivo selecionado:", obj_sel)  # Debug
    if st.button("PRÓXIMO PASSO ➔"):
        st.session_state.v_objetivo = obj_sel
        st.session_state.ads_passo = 2
        st.experimental_rerun()  # Usar experimental_rerun para forçar a atualização

# Passo 2: Selecionar tipo de campanha
elif st.session_state.ads_passo == 2:
    st.markdown("### 🔎 PASSO 2: SELECIONE UM TIPO DE CAMPANHA")
    
    if st.session_state.v_objetivo is None:
        st.error("⚠️ Por favor, selecione um objetivo primeiro.")  # Validação
    else:
        tipo_sel = st.radio("Escolha o formato:", TIPOS_CAMPANHA)
        st.write("Tipo de campanha selecionado:", tipo_sel)  # Debug
        
        if st.button("PRÓXIMO PASSO ➔"):
            st.session_state.ads_passo = 3
            st.experimental_rerun()

# Continue adicionando passos conforme necessário...
