import streamlit as st
import google.generativeai as genai
import pandas as pd

# Configuração da página e estilo escuro profissional
st.set_page_config(page_title="Adriel AI - Painel", layout="wide")

st.title("🚀 Adriel AI - Painel de Comando")
st.markdown("Status: **Sistema Online** | Dados atualizados em tempo real")
st.write("---")

# Criando as abas de navegação do seu painel
aba1, aba2, aba3 = st.tabs(["📊 Radar de Produtos", "✍️ Gerador de Anúncios", "⚙️ Configurações"])

with aba1:
    st.subheader("MÓDULO 1: RADAR DE PRODUTOS [FILTRO XEQUE-MATE]")
    st.markdown("Abaixo estão os produtos gringos pré-analisados para campanhas de Fundo de Funil:")
    
    dados_radar = {
        "Name": ["Produto Gringo 1", "Produto Gringo 2", "Produto Gringo 3", "Produto Gringo 4"],
        "Comissões": ["75%", "80%", "65%", "70%"],
        "Comissão ($)": ["$135.00", "$150.00", "$110.00", "$125.00"],
        "Veredito da IA": ["APROVADO (Risco Baixo)", "APROVADO (Risco Baixo)", "REVISAR (Risco Médio)", "APROVADO (Risco Baixo)"]
    }
    df = pd.DataFrame(dados_radar)
    st.dataframe(df, use_container_width=True)
    
    st.button("📥 BAIXAR PLANILHA DE INTELIGÊNCIA (.CSV)")

with aba2:
    st.subheader("MÓDULO 2: GERADOR DE ANÚNCIOS MASTER & PRE-SELL")
    
    produto_alvo = st.text_input("✍️ Digite o Nome do Produto Gringo:", value="Sugar Defender")
    resumo_niche = st.text_area("📋 Resumo do Produto (Nicho/Dores):", value="Suplemento natural para equilíbrio do metabolismo.")
    
    col1, col2 = st.columns(2)
    with col1:
        btn_anuncio = st.button("🟢 (A) GERAR ANÚNCIOS ADSMASTER")
    with col2:
        btn_presell = st.button("🟢 (B) FABRICAR PRE-SELL (Landing Page Text)")
        
    if btn_anuncio:
        st.info(f"Processando IA para {produto_alvo}...")
        
        # 🛡️ PUXANDO A CHAVE PROTEGIDA DO SERVIDOR DO STREAMLIT
        try:
            genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
        except Exception:
            st.error("Chave de API não configurada no painel do Streamlit.")
        
        modelo_ativo = "gemini-1.5-flash"
        try:
            for m in genai.list_models():
                if 'generateContent' in m.supported_generation_methods:
                    modelo_ativo = m.name
                    break
        except Exception:
            pass
            
        model = genai.GenerativeModel(modelo_ativo)
        prompt = f"Crie 3 títulos de até 30 caracteres e 2 descrições de até 90 caracteres para o produto de afiliado gringo {produto_alvo} baseado em: {resumo_niche}. Siga as políticas do Google Ads. Seja direto."
        
        try:
            resposta = model.generate_content(prompt)
            st.success("🎯 Arsenal de Anúncios gerado com sucesso!")
            st.text_area("📋 Copie os textos abaixo:", value=resposta.text, height=250)
        except Exception as e:
            st.error(f"Erro de conexão com o robô: {e}")

with aba3:
    st.subheader("⚙️ Painel de Configurações")
    st.text_input("🔑 Chave Mestre API do Google:", value="OCULTA_NO_SERVIDOR", type="password")
    st.selectbox("🤖 Modelo de IA Ativo:", ["gemini-1.5-flash", "gemini-1.5-pro"])
    st.success("Configurações de infraestrutura integradas com o repositório.")
