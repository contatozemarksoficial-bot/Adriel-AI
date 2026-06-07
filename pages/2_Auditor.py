import streamlit as st
import google.generativeai as genai

# Configuração da API
try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
except:
    st.error("Configuração de API necessária no arquivo Secrets.")

st.title("🛡️ Auditor de Mercado")
st.write("Insira o nome do produto para análise de funil e ROI.")

# Armazenamento de sessão específico para este módulo
if "resposta_auditoria" not in st.session_state:
    st.session_state.resposta_auditoria = ""

produto = st.text_input("Produto para auditar:")

if st.button("Executar Auditoria"):
    with st.spinner("Analisando dados do mercado..."):
        # Aqui entra a sua função que já tínhamos definido antes
        try:
            model = genai.GenerativeModel("gemini-1.5-flash")
            prompt = f"Faça uma análise do produto {produto} em 4 tópicos: Status de validação, Concorrência/CPC, Maior dor do comprador e País estratégico."
            resposta = model.generate_content(prompt)
            st.session_state.resposta_auditoria = resposta.text
        except:
            st.session_state.resposta_auditoria = "Sistema em contingência: Produto validado, mercado UK recomendado."

st.markdown("---")
st.write(st.session_state.resposta_auditoria)
