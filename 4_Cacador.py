import streamlit as st
import google.generativeai as genai

# Configuração da API
try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
except:
    st.error("Erro: API Key não configurada nos Secrets.")

st.title("🔍 4. Caçador de Oportunidades")
st.write("Identifique sub-nichos lucrativos e inexplorados.")

# Entrada do usuário
termo_busca = st.text_input("Qual nicho deseja explorar?")

if st.button("Buscar Oportunidades"):
    if termo_busca:
        with st.spinner("O Gemini está caçando oportunidades..."):
            model = genai.GenerativeModel("gemini-1.5-flash")
            prompt = f"Analise o nicho '{termo_busca}' e me dê 5 sub-nichos específicos, com alta demanda e pouca concorrência, focados em venda de produtos digitais."
            resposta = model.generate_content(prompt)
            st.markdown(resposta.text)
    else:
        st.warning("Por favor, insira um nicho.")
