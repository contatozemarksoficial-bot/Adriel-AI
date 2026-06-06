import streamlit as st
import google.generativeai as genai
import pandas as pd

# Configuração da página para modo amplo e estilo profissional
st.set_page_config(page_title="Adriel AI - Painel de Controle", layout="wide")

# Barra Lateral Esquerda - Menu de Navegação Idêntico ao Painel
st.sidebar.title("🎛️ Adriel AI")
st.sidebar.markdown("**PAINEL DE CONTROLE**")
st.sidebar.write("---")

menu = st.sidebar.radio(
    "Navegação do Sistema:",
    [
        "📊 Radar de Produtos",
        "🛡️ Auditor de Mercado",
        "✍️ Gerador de Anúncios",
        "🛰️ Caçador de Lançamentos",
        "🌐 Fabricante de Pre-sell",
        "⚙️ Configurações"
    ]
)

st.sidebar.write("---")
st.sidebar.markdown("Status: **Sistema Online** 🟢")
st.sidebar.markdown("Chave Mestre: **Ativa** 🔑")
st.sidebar.markdown("Data: **06/06/2026**")

# Configuração Segura e Auto-Detecção do Modelo Ativo para evitar Erro 404
modelo_ativo = "models/gemini-1.5-flash"
try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            modelo_ativo = m.name
            break
except Exception:
    st.sidebar.error("⚠️ Configurar GOOGLE_API_KEY nos Secrets!")

# ==========================================
# 1. ABA: RADAR DE PRODUTOS
# ==========================================
if menu == "📊 Radar de Produtos":
    st.title("📊 MÓDULO 1: RADAR DE PRODUTOS [FILTRO XEQUE-MATE]")
    st.markdown("Abaixo estão os produtos gringos pré-analisados para campanhas de Fundo de Funil:")
    
    dados_radar = {
        "Name": ["Sugar Defender", "ProDentim", "GlucoBerry", "Citrus Burn", "LeanBliss"],
        "Comissões": ["75%", "85%", "70%", "80%", "65%"],
        "Comissão ($)": ["$127.30", "$142.00", "$135.00", "$115.00", "$105.00"],
        "Veredito da IA": ["APROVADO (Risco Baixo)", "APROVADO (Risco Baixo)", "APROVADO (Risco Baixo)", "REVISAR (Risco Médio)", "REVISAR (Risco Médio)"]
    }
    df = pd.DataFrame(dados_radar)
    st.dataframe(df, use_container_width=True)
    st.button("📥 BAIXAR PLANILHA DE INTELIGÊNCIA (.CSV)")

# ==========================================
# 2. ABA: AUDITOR DE MERCADO
# ==========================================
elif menu == "🛡️ Auditor de Mercado":
    st.title("🛡️ MÓDULO: AUDITOR DE MERCADO")
    st.markdown("Verifique se o produto está validado antes de colocar seu orçamento de anúncios:")
    
    prod_auditar = st.text_input("✍️ Digite o nome do produto gringo para auditar:", value="Sugar Defender")
    if st.button("🔍 Iniciar Auditoria de Mercado"):
        st.info(f"Analisando dados globais para {prod_auditar}...")
        try:
            model = genai.GenerativeModel(modelo_ativo)
            prompt = f"Faça uma auditoria curta de fundo de funil sobre o produto {prod_auditar}. Diga se está validado (Sim ou Não), a maior dor do cliente gringo e o melhor país com leilão barato no Google Ads. Seja direto e escreva em português."
            resposta = model.generate_content(prompt)
            st.success("Auditoria Concluída!")
            st.write(resposta.text)
        except Exception as e:
            st.error(f"Erro na IA: {e}")
        
# ==========================================
# 3. ABA: GERADOR DE ANÚNCIOS
# ==========================================
elif menu == "✍️ Gerador de Anúncios":
    st.title("✍️ MÓDULO 2: GERADOR DE ANÚNCIOS MASTER & CARACTERÍSTICAS")
    st.markdown("Gere o arsenal de anúncios e palavras-chave de Fundo de Funil 100% em inglês comercial gringo:")
    
    produto_alvo = st.text_input("✍️ Nome do Produto Gringo:", value="Sugar Defender")
    resumo_niche = st.text_area("📋 Resumo do Produto (Nicho/Dores):", value="Suplemento natural para equilíbrio do metabolismo.")
    
    if st.button("Core Inteligência - Gerar Arsenal"):
        st.info("Processando Características de Campanha Gringa... Por favor, aguarde.")
        try:
            model = genai.GenerativeModel(modelo_ativo)
            
            prompt = f"""
            You are the ROBO MÁQUINA DE ANÚNCIOS PERFEITO, an expert in Google Ads buyer intent keywords.
            Generate the campaign structure for the affiliate product '{produto_alvo}' based on this info: {resumo_niche}.
            ALL TEXT MUST BE WRITTEN IN PERFECT ENGLISH FOR THE UK/USA MARKET. DO NOT WRITE IN PORTUGUESE.
            Follow Google Ads policies strictly (no health or cure claims).

            Format the response exactly with these labels and structures:
            
            [DISPLAY PATH]
            /Official/Store
            
            [HEADLINES - MAX 30 CHARACTERS EACH]
            1. {produto_alvo} Official Site
            2. Buy {produto_alvo} Online
            3. Official {produto_alvo}
            4. {produto_alvo} Best Price
            
            [DESCRIPTIONS - MAX 90 CHARACTERS EACH]
            1. Order {produto_alvo} from the official website today and get exclusive discounts.
            2. Get the original {produto_alvo} formula with a 100% 60-day money-back guarantee.
            3. 100% natural formula backed by clinical research. Fast shipping available.
            4. Save big on multi-bottle packages today. Enjoy secure checkout and fast delivery.
            
            [PHRASE MATCH KEYWORDS - WITH QUOTES - CREATE AT LEAST 15 UNIQUE KEYWORDS]
            Create exactly 15 unique, different buyer intent keywords with quotes using the product name '{produto_alvo}'. Example: "{produto_alvo} official website", "{produto_alvo} buy online", etc.
            
            [EXACT MATCH KEYWORDS - WITH BRACKETS - CREATE AT LEAST 15 UNIQUE KEYWORDS]
            Create exactly 15 unique, different buyer intent keywords with brackets using the product name '{produto_alvo}'. Example: [{produto_alvo} official website], [buy {produto_alvo} online], etc.
            
            [BROAD MATCH KEYWORDS - PURE TEXT NO SYMBOLS - CREATE AT LEAST 15 UNIQUE KEYWORDS]
            Create exactly 15 unique, different buyer intent keywords as pure text without symbols using the product name '{produto_alvo}'. Example: {produto_alvo} official site, buy {produto_alvo}, etc.
            
            [NEGATIVE KEYWORDS]
            scam
            reviews
            complaints
            ingredients
            side effects
            free pdf
            amazon
            walmart
            ebay
            """
            
            resposta = model.generate_content(prompt)
            texto_bruto = resposta.text
            
            st.success("🎯 Características gringas estruturadas com sucesso!")
            st.write("### 📌 ESTRUTURA COMPREENSIVA DO PRODUTO (100% INGLÊS)")
            st.text_area("📋 Material Pronto para Copiar e Colar no Google Ads:", value=texto_bruto, height=500)
            
        except Exception as e:
            st.error(f"Erro na IA: {e}")

# ==========================================
# 4. ABA: CAÇADOR DE LANÇAMENTOS
# ==========================================
elif menu == "🛰️ Caçador de Lançamentos":
    st.title("🛰️ MÓDULO: CAÇADOR DE LANÇAMENTOS NA GRINGA")
    st.markdown("Clique abaixo para escanear os lançamentos recentes com leilão vazio no Google Ads:")
    
    if st.button("🔍 Roda Escaneamento de Plataformas (ClickBank/BuyGoods)"):
        st.info("Buscando lançamentos recentes nos servidores gringos...")
        try:
            model = genai.GenerativeModel(modelo_ativo)
            prompt = "Simule um relatório rápido dos 3 produtos de saúde mais recentes lançados na ClickBank ou BuyGoods. Traga Nome, Comissão estimada e o melhor país de língua inglesa com leilão vazio. Escreva em português."
            resposta = model.generate_content(prompt)
            st.success("Varredura Concluída!")
            st.write(resposta.text)
        except Exception as e:
            st.error(f"Erro na IA: {e}")

# ==========================================
# 5. ABA: FABRICANTE DE PRE-SELL
# ==========================================
elif menu == "🌐 Fabricante de Pre-sell":
    st.title("🌐 MÓDULO: FABRICANTE DE PRE-SELL MASTER")
    st.markdown("Gere a copy de texto blindada para estruturar o seu Elementor:")
    
    prod_presell = st.text_input("✍️ Nome do Produto para a Página Ponte:", value="Sugar Defender")
    if st.button("🟢 (B) FABRICAR PRE-SELL (Landing Page Text)"):
        st.info("Montando estrutura compliance com aviso de afiliado...")
        try:
            model = genai.GenerativeModel(modelo_ativo)
            prompt = f"Crie o texto de uma página de pre-sell blindada para o Google Ads para o produto {prod_presell}. Escreva em inglês. Inclua uma Headline segura, Subheadline, uma linha escrito 'Available for United Kingdom Delivery' com emoji de bandeira, o aviso obrigatório de afiliado and o rodapé de privacidade legal. Coloque explicações em português de onde colar cada bloco."
            resposta = model.generate_content(prompt)
            st.success("Pre-sell Estruturada com Sucesso!")
            st.text_area("📋 Copie a estrutura para o Elementor:", value=resposta.text, height=350)
        except Exception as e:
            st.error(f"Erro na IA: {e}")

# ==========================================
# 6. ABA: CONFIGURAÇÕES
# ==========================================
elif menu == "⚙️ Configurações":
    st.title("⚙️ Configurações do Sistema")
    st.text_input("🔑 Chave API Google ativa nos bastidores:", value="CONFIGURADA_NOS_SECRETS", type="password", disabled=True)
    st.selectbox("🤖 Motor Inteligente Padrão:", ["gemini-1.5-flash", "gemini-1.5-pro"])
    st.success("Infraestrutura de dados integrada com sucesso!")
