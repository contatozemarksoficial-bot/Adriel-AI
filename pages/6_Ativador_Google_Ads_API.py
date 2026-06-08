import streamlit as st

# Definições de constantes
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

# Configuração da página
st.set_page_config(page_title="Adriel AI - Google Ads Pro Suite", layout="wide")

# Inicialização do estado
if "ads_passo" not in st.session_state:
    st.session_state.ads_passo = 1
if "v_objetivo" not in st.session_state:
    st.session_state.v_objetivo = None

# Barra de progresso
st.progress((st.session_state.ads_passo - 1) / 6)
st.markdown(f"**Progresso: Passo {st.session_state.ads_passo} de 6**")
st.write("---")

# Passo 1: Escolher objetivo
if st.session_state.ads_passo == 1:
    st.markdown("### 🎯 PASSO 1: ESCOLHER SEU OBJETIVO")
    obj_sel = st.radio("Selecione a meta:", OBJETIVOS_CAMPANHA)
    if st.button("PRÓXIMO PASSO ➔"):
        st.session_state.v_objetivo = obj_sel
        st.session_state.ads_passo = 2
        st.experimental_rerun()  # Força a atualização da página

# Passo 2: Selecionar tipo de campanha
elif st.session_state.ads_passo == 2:
    st.markdown("### 🔎 PASSO 2: SELECIONE UM TIPO DE CAMPANHA")

    if st.session_state.v_objetivo is None:
        st.error("⚠️ Por favor, selecione um objetivo primeiro.")
    else:
        tipo_sel = st.radio("Escolha o formato:", TIPOS_CAMPANHA)
        if st.button("PRÓXIMO PASSO ➔"):
            st.session_state.ads_passo = 3
            st.experimental_rerun()  # Força a atualização

# Passo 3: Estratégia de lances
elif st.session_state.ads_passo == 3:
    st.markdown("### 💰 PASSO 3: ESTRATÉGIA DE LANCES")
    # Aqui você pode adicionar suas opções de estratégia de lances
    if st.button("PRÓXIMO PASSO ➔"):
        st.session_state.ads_passo = 4
        st.experimental_rerun()

# Passo 4: Orçamento diário
elif st.session_state.ads_passo == 4:
    st.markdown("### 💵 PASSO 4: ORÇAMENTO DA CAMPANHA")
    st
