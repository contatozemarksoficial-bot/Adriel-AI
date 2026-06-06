import streamlit as st
import pandas as pd
import google.generativeai as genai

# 1. Configuração da API (Aqui o motor liga)
try:
    genai.configure(api_key=st.secrets["GEMINI_KEY"])
    model = genai.GenerativeModel("gemini-1.5-flash")
except:
    st.error("Erro: Chave API não configurada nas Secrets.")

st.set_page_config(page_title="Adriel AI - Painel", layout="wide")
st.title("🚀 Adriel AI - Painel de Comando")

# 2. Definição das Abas
tab1, tab2, tab3 = st.tabs(["📊 Radar de Produtos", "🎭 Gerador de Anúncios", "⚙️ Configurações"])

# 3. Lógica do Radar (Tab 1)
with tab1:
    st.subheader("Radar de Produtos Xeque-Mate")
    df = pd.DataFrame({
        "Produto": ["Puravive", "Sugar Defender", "Prod. Gringo X"],
        "Comissão": ["$140", "$125", "$90"],
        "Veredito": ["APROVADO", "APROVADO", "REVISAR"]
    })
    st.table(df)

# 4. Lógica do Gerador de Anúncios (Tab 2)
with tab2:
    st.subheader("Gerador de Anúncios Master")
    produto_alvo = st.text_input("Qual o nome do produto?")
    if st.button("Gerar Anúncios e Roteiro"):
        if produto_alvo:
            with st.spinner("Conectando com o motor de IA..."):
                prompt = f"Crie um roteiro de vendas e 3 títulos para anúncios no Google Ads para o produto {produto_alvo}."
                resultado = model.generate_content(prompt)
                st.markdown(resultado.text)
        else:
            st.warning("Por favor, digite o nome de um produto.")

# 5. Configurações (Tab 3)
with tab3:
    st.subheader("Configurações do Sistema")
    st.write("Status do Motor: Ativo ✅")
    st.write("Chave Gemini: Conectada ✅")
    if st.button("Limpar Cache do Sistema"):
        st.cache_data.clear()
        st.success("Sistema limpo!")
