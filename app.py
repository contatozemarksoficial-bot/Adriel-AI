import streamlit as st
import google.generativeai as genai

# Configuração da Página
st.set_page_config(page_title="Super Cérebro V3", layout="wide")

# Tenta carregar a API Key de forma segura
try:
    api_key = st.secrets["GEMINI_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')
except Exception as e:
    st.error("Erro de configuração: Verifique a chave GEMINI_KEY nas Secrets.")
    st.stop()

# --- INTERFACE ---
st.title("👑 Super Cérebro Supremo Unificado V3")
tab1, tab2, tab3 = st.tabs(["🔎 1. Filtro", "🎭 2. Avatar", "📢 3. Máquina de Ads"])

# Inicializa estado se não existir
if 'avatar' not in st.session_state:
    st.session_state['avatar'] = "Pessoas buscando renda extra"

with tab1:
    st.subheader("Produtos Validados")
    st.table({"Produto": ["Puravive", "Sugar Defender"], "Status": ["Validado", "Validado"]})

with tab2:
    st.subheader("Definição de Avatar")
    st.session_state['avatar'] = st.text_area("Descreva seu público:", st.session_state['avatar'])

with tab3:
    st.subheader("Máquina de Ads")
    produto_sel = st.selectbox("Selecione o produto:", ["Puravive", "Sugar Defender"])
    
    # Botão com tratamento de erro
    if st.button("GERAR ANÚNCIO"):
        try:
            with st.spinner("Gerando copy de alta pressão..."):
                prompt = f"Crie um anúncio de vendas persuasivo para {produto_sel} focado em {st.session_state['avatar']}. Use gatilhos de urgência."
                response = model.generate_content(prompt)
                st.markdown("---")
                st.write(response.text)
                st.markdown("---")
        except Exception as e:
            st.error(f"Erro ao gerar conteúdo: {e}")
            st.warning("Verifique se a sua chave API está correta e com saldo no Google AI Studio.")
