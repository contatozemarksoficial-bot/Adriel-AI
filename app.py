import streamlit as st
import pandas as pd

# Configuração de Layout
st.set_page_config(page_title="Leonardo AI - Painel de Controle", layout="wide")

# Título do Painel
st.title("👑 Painel de Comando Leonardo AI")
st.markdown("---")

# Abas do Sistema
tab1, tab2, tab3 = st.tabs(["📊 Radar de Produtos", "🎭 Gerador de Anúncios", "⚙️ Configurações"])

with tab1:
    st.subheader("Radar de Oportunidades")
    # Tabela de exemplo
    dados = {"Produto": ["Puravive", "Sugar Defender"], "Comissão": ["$142", "$127"]}
    st.table(pd.DataFrame(dados))

with tab2:
    st.subheader("Gerador de Anúncios Master")
    produto = st.text_input("Qual o produto gringo?")
    if st.button("Gerar Estratégia de Vendas"):
        st.success(f"A IA está processando o criativo para: {produto}")
        st.text_area("Resultado:", "Aqui aparecerá o copy e o roteiro do seu anúncio após a integração com a API.")

with tab3:
    st.subheader("Configurações do Sistema")
    st.info("Chave API do Gemini: Ativa ✅")
    st.write("Versão do Sistema: 2026.06.06")
