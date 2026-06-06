import streamlit as st
import google.generativeai as genai

# Configuração da sua Chave
genai.configure(api_key="SUA_CHAVE_AQUI")
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("🚀 Adriel-AI: Painel de Controle de Afiliados")

tab1, tab2, tab3 = st.tabs(["📊 Consultoria & Estratégia", "🎭 Criativos (Avatar)", "💰 Máquina de Ads"])

with tab1:
    st.subheader("Consultoria Estratégica")
    pergunta = st.text_area("O que você quer perguntar para o Robô 3?")
    if st.button("Consultar"):
        # Lógica do Robô 3 aqui
        st.write("Analisando estratégias...")

with tab2:
    st.subheader("Criador de Anúncios Avatar")
    produto = st.selectbox("Selecione o produto:", ["Puravive", "Sugar Defender", "Java Burn"])
    if st.button("Gerar Roteiro e Prompt"):
        # Lógica do Avatar Real aqui
        st.success("Criativo pronto!")

with tab3:
    st.subheader("Máquina de Ads (Download)")
    prod_ads = st.text_input("Nome do Produto para a Campanha")
    if st.button("Criar Campanha"):
        # Lógica de geração de campanha e st.download_button aqui
        st.download_button("Baixar Campanha", "Conteúdo do arquivo", file_name="campanha.txt")
