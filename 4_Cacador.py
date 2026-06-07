import streamlit as st
import google.generativeai as genai

# Configuração Padrão
try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
except:
    st.error("Configuração de API pendente.")

st.title("🔍 Caçador de Oportunidades")
st.write("Varredura inteligente de tendências e lançamentos.")

nicho_busca = st.text_input("Qual nicho deseja caçar?")

if st.button("Iniciar Varredura"):
    with st.spinner("Varrendo o mercado em busca de brechas..."):
        model = genai.GenerativeModel("gemini-1.5-flash")
        prompt = f"Liste 5 oportunidades de produtos ou nichos inexplorados no mercado de afiliados para o tema {nicho_busca}."
        resultado = model.generate_content(prompt)
        st.markdown(resultado.text)
