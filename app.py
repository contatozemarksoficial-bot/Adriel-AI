import streamlit as st
import google.generativeai as genai

# Configuração da Página
st.set_page_config(page_title="Super Cérebro V3", layout="wide")

# Configuração da API
genai.configure(api_key=st.secrets["GEMINI_KEY"])
model = genai.GenerativeModel('gemini-pro')

# --- SIDEBAR: Painel de Controle ---
st.sidebar.title("⚙️ Painel de Controle")
st.sidebar.info("Use este painel para configurar sua estratégia de vendas.")
if 'avatar' not in st.session_state:
    st.session_state['avatar'] = "Pessoas buscando renda extra"

# --- Título Principal ---
st.title("👑 Super Cérebro Supremo Unificado V3")

# --- Estrutura de Abas ---
tab1, tab2, tab3 = st.tabs(["📊 Filtro Xeque-Mate", "🎭 Configuração de Avatar", "🤖 Máquina de Ads"])

with tab1:
    st.header("Filtro Xeque-Mate: Produtos Validados")
    # Tabela de visualização rápida
    col_a, col_b = st.columns([2, 1])
    with col_a:
        st.table({
            "Produto": ["Puravive", "Sugar Defender", "Lançamento X"],
            "Plataforma": ["ClickBank", "BuyGoods", "Hotmart"],
            "Comissão": ["$142.10", "$127.30", "R$ 350.00"]
        })
    with col_b:
        st.success("Produtos prontos para análise de pressão!")

with tab2:
    st.header("Configuração do Avatar")
    st.session_state['avatar'] = st.text_input("Defina o perfil do cliente:", st.session_state['avatar'])
    st.write(f"Você está focando em: **{st.session_state['avatar']}**")

with tab3:
    st.header("Máquina de Ads")
    produto_sel = st.selectbox("Escolha o Produto para criar o Ad:", ["Puravive", "Sugar Defender", "Lançamento X"])
    
    if st.button("Gerar Estratégia de Pressão"):
        prompt = f"Crie um anúncio de alta conversão para o produto {produto_sel} focado em {st.session_state['avatar']}. Use gatilhos mentais, escassez e uma chamada irresistível para o nosso grupo de estudos."
        with st.spinner("O Cérebro Supremo está criando..."):
            resposta = model.generate_content(prompt)
            st.markdown("---")
            st.write(resposta.text)
            st.markdown("---")
            st.success("Copy gerada com sucesso!")
