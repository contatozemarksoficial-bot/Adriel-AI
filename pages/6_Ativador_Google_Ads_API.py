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

# Configuração do layout
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
st.markdown("Chassi sequencial de alta performance blindado com validações de dados.")
st.write("---")

# Gerenciamento de estado
if "ads_passo" not in st.session_state: st.session_state.ads_passo = 1
if "v_objetivo" not in st.session_state: st.session_state.v_objetivo = "Vendas"
if "v_tipo" not in st.session_state: st.session_state.v_tipo = "Pesquisa"
if "v_alcance" not in st.session_state: st.session_state.v_alcance = "Visitas ao site"
if "v_nome_campanha" not in st.session_state: st.session_state.v_nome_campanha = "Sales-Search-22"
if "v_metrica" not in st.session_state: st.session_state.v_metrica = "Conversões"
if "v_local" not in st.session_state: st.session_state.v_local = "Todos os países/territórios"
if "v_idioma" not in st.session_state: st.session_state.v_idioma = "Português"
if "v_budget_val" not in st.session_state: st.session_state.v_budget_val = 0.0

# Barra de progresso
st.progress((st.session_state.ads_passo - 1) / 6)
st.markdown(f"**Progresso do Setup Google Ads: Passo {st.session_state.ads_passo} de 6**")
st.write("---")

# Passo 1: Escolher objetivo
if st.session_state.ads_passo == 1:
    st.markdown("### 🎯 PASSO 1: ESCOLHER SEU OBJETIVO")
    obj_sel = st.radio("Selecione a meta:", OBJETIVOS_CAMPANHA)
    if st.button("PRÓXIMO PASSO ➔", key="to_p2"):
        st.session_state.v_objetivo = "Vendas" if "Vendas" in obj_sel else "Outros"
        st.session_state.ads_passo = 2
        st.rerun()

# Passo 2: Selecionar tipo de campanha
elif st.session_state.ads_passo == 2:
    st.markdown("### 🔎 PASSO 2: SELECIONE UM TIPO DE CAMPANHA")
    tipo_sel = st.radio("Escolha o formato:", TIPOS_CAMPANHA)
    st.session_state.v_nome_campanha = st.text_input("Nome da campanha:")
    if st.button("PRÓXIMO PASSO ➔", key="to_p3"):
        if st.session_state.v_nome_campanha.strip() == "":
            st.error("⚠️ Erro de Validação: Insira um nome válido.")
        else:
            st.session_state.v_tipo = "Pesquisa" if "Pesquisar" in tipo_sel else "Outros"
            st.session_state.ads_passo = 3
            st.rerun()

# Passo 3: Estratégia de lances
elif st.session_state.ads_passo == 3:
    st.markdown("### 💰 PASSO 3: ESTRATÉGIA DE LANCES DA CAMPANHA")
    st.session_state.v_metrica = st.selectbox("Métrica:", ["Conversões", "Cliques", "Parcela de impressões"])
    st.session_state.v_local = st.radio("Locais:", ["Todos os países", "Brasil", "Inserir outro local"])
    st.session_state.v_idioma = st.selectbox("Idiomas:", ["Português", "Inglês", "Todos os idiomas"])
    if st.button("PRÓXIMO PASSO ➔", key="to_p4"):
        st.session_state.ads_passo = 4
        st.rerun()

# Passo 4: Orçamento
elif st.session_state.ads_passo == 4:
    st.markdown("### 💵 PASSO 4: ORÇAMENTO DA CAMPANHA")
    st.session_state.v_budget_val = st.number_input("Orçamento diário:", min_value=0.0, step=0.01)
    if st.button("PRÓXIMO PASSO ➔", key="to_p5"):
        if st.session_state.v_budget_val <= 0:
            st.error("⚠️ Erro de Validação: O orçamento diário deve ser um valor positivo.")
        else:
            st.session_state.ads_passo = 5
            st.success("✅ Orçamento validado com sucesso!")
            st.rerun()

# Passo 5: Resumo da campanha
elif st.session_state.ads_passo == 5:
    st.markdown("### 📋 PASSO 5: RESUMO DA CAMPANHA")
    st.write(f"**Objetivo:** {st.session_state.v_objetivo}")
    st.write(f"**Tipo de Campanha:** {st.session_state.v_tipo}")
    st.write(f"**Alcance:** {st.session_state.v_alcance}")
    st.write(f"**Nome da Campanha:** {st.session_state.v_nome_campanha}")
    st.write(f"**Métrica de Foco:** {st.session_state.v_metrica}")
    st.write(f"**Local:** {st.session_state.v_local}")
    st.write(f"**Idioma:** {st.session_state.v_idioma}")
    st.write(f"**Orçamento Diário:** R$ {st.session_state.v_budget_val:.2f}")
    
    if st.button("CONFIRMAR CAMPANHA", key="confirm_campaign"):
        st.success("✅ Campanha criada com sucesso!")
        # Aqui você pode adicionar a lógica para enviar os dados para a API do Google Ads.

# Passo 6: Finalização
elif st.session_state.ads_passo == 6:
    st.markdown("### 🎉 CAMPANHA FINALIZADA!")
    st.markdown("Obrigado por usar o Ativador Inteligente do Google Ads.")
