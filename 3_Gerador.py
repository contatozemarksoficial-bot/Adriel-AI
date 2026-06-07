import streamlit as st
import google.generativeai as genai

# Configuração da API
try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
except:
    st.error("Configuração de API necessária.")

st.title("✍️ Gerador de Anúncios Master")
st.write("Crie headlines e estruturas de campanha de alta conversão.")

# Memória para não perder os dados ao trocar de aba
if "resposta_gerador" not in st.session_state:
    st.session_state.resposta_gerador = ""

produto = st.text_input("Nome do Produto:")

if st.button("Gerar Anúncios"):
    with st.spinner("Gerando estrutura..."):
        try:
            model = genai.GenerativeModel("gemini-1.5-flash")
            prompt = f"Gere uma estrutura de Google Ads para o produto {produto} contendo Headlines (max 30 chars), Descrições (max 90 chars), Keywords (Phrase, Exact, Broad) e Negative Keywords."
            resposta = model.generate_content(prompt)
            st.session_state.resposta_gerador = resposta.text
        except:
            st.session_state.resposta_gerador = "Erro ao conectar. Tente novamente."

if st.session_state.resposta_gerador:
    st.code(st.session_state.resposta_gerador)
