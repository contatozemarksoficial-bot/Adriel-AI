import streamlit as st
import pandas as pd
import google.generativeai as genai

# Configuração da Página
st.set_page_config(page_title="Adriel AI", layout="wide")
st.title("🚀 Adriel AI - Painel de Comando")

# Tentar carregar a chave
try:
    api_key = st.secrets["GEMINI_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    status_api = "Conectado ✅"
except:
    status_api = "Chave API não configurada ou inválida ❌"

tab1, tab2, tab3 = st.tabs(["📊 Radar de Produtos", "🎭 Gerador de Anúncios", "⚙️ Configurações"])

with tab1:
    st.subheader("Radar de Oportunidades")
    st.table(pd.DataFrame({"Produto": ["Puravive", "Sugar Defender"], "Comissão": ["$142", "$127"]}))

with tab2:
    st.subheader("Gerador de Anúncios Master")
    produto = st.text_input("Qual o produto gringo?")
    if st.button("Gerar Estratégia de Vendas"):
        if 'model' in globals():
            with st.spinner("IA criando seu criativo de alta conversão..."):
                try:
                    response = model.generate_content(f"Crie um roteiro de vendas para o produto {produto}")
                    st.markdown(response.text)
                except Exception as e:
                    st.error(f"Erro ao gerar conteúdo: {e}")
        else:
            st.error("O motor de IA não está conectado. Verifique as configurações.")

with tab3:
    st.subheader("Configurações")
    st.write(f"Status da API: {status_api}")
