import streamlit as st
import google.generativeai as genai

# Configuração
genai.configure(api_key=st.secrets["GEMINI_KEY"])
model = genai.GenerativeModel('gemini-pro')

st.set_page_config(page_title="Super Cérebro V3 - Atração e Vendas", layout="wide")

st.title("🚀 Super Cérebro Supremo Unificado V3")

tab1, tab2, tab3 = st.tabs(["🔎 Filtro de Oportunidades", "🎯 Avatar de Engajamento", "📢 Máquina de Vendas/Atração"])

# --- ABA 1: FILTRO ---
with tab1:
    st.header("Filtragem de Produtos (Xeque-Mate)")
    produto_analise = st.text_input("Cole o nome ou link do produto para analisar:")
    if st.button("Analisar Potencial de Venda"):
        prompt = f"Analise o produto {produto_analise}. Por que ele é um bom produto para vender agora? Identifique a 'dor' principal que podemos usar para atrair pessoas para um grupo de estudos."
        res = model.generate_content(prompt)
        st.write(res.text)

# --- ABA 2: AVATAR ---
with tab2:
    st.header("Avatar do Estudante")
    st.write("Quem queremos atrair para o grupo?")
    dor_publico = st.text_input("Qual a maior dificuldade desse público?")
    if st.button("Criar Perfil do Estudante"):
        st.session_state['avatar_info'] = dor_publico
        st.success(f"Estudante focado em: {dor_publico}")

# --- ABA 3: MÁQUINA DE ADS ---
with tab3:
    st.header("Máquina de Ads - Atração para o Grupo")
    if 'avatar_info' in st.session_state:
        if st.button("Gerar Anúncio de Alta Pressão"):
            prompt = f"""
            Crie um anúncio persuasivo para atrair pessoas para o nosso grupo de estudos de vendas.
            O foco é ajudar quem tem a seguinte dificuldade: {st.session_state['avatar_info']}.
            Use uma copy de alta pressão, mostrando que o tempo está acabando e que o conhecimento está no nosso grupo.
            Ao final, coloque uma chamada forte para o nosso link de convite.
            """
            res = model.generate_content(prompt)
            st.write(res.text)
    else:
        st.warning("Defina o Avatar na aba 2 primeiro!")
