import streamlit as st
import google.generativeai as genai

# Configuração da Página
st.set_page_config(page_title="Super Cérebro V3", layout="wide")

# Configuração da API
genai.configure(api_key=st.secrets["GEMINI_KEY"])
model = genai.GenerativeModel('gemini-pro')

# --- CABEÇALHO DE IMPACTO (O que o afiliado vê de cara) ---
st.title("👑 Super Cérebro Supremo Unificado V3")
st.markdown("---")
st.success("🚀 Bem-vindo, Afiliado. Você está no painel de alta conversão. Siga os passos abaixo para gerar sua máquina de vendas.")

# --- SIDEBAR: O painel de controle fixo ---
st.sidebar.header("🎯 Painel de Ação")
if 'avatar' not in st.session_state:
    st.session_state['avatar'] = "Pessoas buscando renda extra"

# --- ESTRUTURA DE ABAS (O fluxo de trabalho) ---
tab1, tab2, tab3 = st.tabs(["🔎 1. Filtro de Oportunidades", "🎭 2. Definição de Avatar", "📢 3. Máquina de Ads"])

with tab1:
    st.subheader("Produtos Validados (Xeque-Mate)")
    st.write("Abaixo estão os produtos que convertem hoje:")
    st.table({
        "Produto": ["Puravive", "Sugar Defender", "Lançamento Exclusivo"],
        "Potencial": ["⭐⭐⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"],
        "Ação": ["Analisar", "Analisar", "Analisar"]
    })

with tab2:
    st.subheader("Quem vamos atrair?")
    st.session_state['avatar'] = st.text_area("Descreva o seu público-alvo para o grupo de estudos:", st.session_state['avatar'])
    st.info("Dica: Quanto mais específica a dor desse público, maior a pressão do seu anúncio.")

with tab3:
    st.subheader("Gere sua Copy de Alta Pressão")
    produto_escolhido = st.selectbox("Selecione o produto alvo:", ["Puravive", "Sugar Defender", "Lançamento Exclusivo"])
    
    if st.button("GERAR ANÚNCIO DE CONVERSÃO"):
        prompt = f"""
        Você é um estrategista de marketing de afiliados. Crie um anúncio agressivo e persuasivo 
        para atrair pessoas para o nosso grupo de estudos exclusivo.
        
        - Produto: {produto_escolhido}
        - Público-Alvo: {st.session_state['avatar']}
        - Objetivo: Fazer a pessoa sentir que está perdendo uma grande oportunidade se não entrar no grupo agora.
        
        Estruture com: Título chamativo, Dor do público, Promessa de solução no grupo e Link de convite.
        """
        with st.spinner("Estamos criando sua estratégia de vendas..."):
            resultado = model.generate_content(prompt)
            st.markdown("### 📣 Copy Gerada para seu Anúncio:")
            st.write(resultado.text)
            st.warning("Copie e cole este texto no seu Gerenciador de Anúncios!")
