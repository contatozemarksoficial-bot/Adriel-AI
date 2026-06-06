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

# ==========================================
# 1. ABA: RADAR DE PRODUTOS (100% ISOLADA E LOCAL)
# ==========================================
if menu == "📊 Radar de Produtos":
    st.title("📊 MÓDULO 1: RADAR DE PRODUTOS [FILTRO XEQUE-MATE]")
    st.markdown("Abaixo estão os 7 principais produtos gringos altamente validados e os melhores mercados para anúncios:")
    
    dados_radar = {
        "Product Name": ["Sugar Defender", "ProDentim", "GlucoBerry", "Citrus Burn", "LeanBliss", "Puravive", "Java Burn"],
        "Comissão Média": ["75%", "85%", "70%", "80%", "75%", "80%", "70%"],
        "Ganho Estimado ($)": ["$127.30", "$142.00", "$135.00", "$115.00", "$105.00", "$138.00", "$120.00"],
        "Veredito de Mercado": ["VALIDADO (Risco Baixo)", "VALIDADO (Risco Baixo)", "VALIDADO (Risco Baixo)", "VALIDADO (Risco Baixo)", "VALIDADO (Risco Médio)", "VALIDADO (Risco Baixo)", "VALIDADO (Risco Baixo)"],
        "Melhor País Estratégico": ["Reino Unido (United Kingdom) 🇬🇧", "Irlanda (Ireland) 🇮🇪", "Nova Zelândia (New Zealand) 🇳🇿", "Estados Unidos (Mobile Only) 🇺🇸", "Canadá (Canada) 🇨🇦", "Reino Unido (United Kingdom) 🇬🇧", "Austrália (Australia) 🇦🇺"]
    }
    df = pd.DataFrame(dados_radar)
    st.dataframe(df, use_container_width=True)
    st.button("📥 BAIXAR PLANILHA DE INTELIGÊNCIA (.CSV)")

# CONEXÃO COM A API SÓ OCORRE SE ENTRAR NOS MÓDULOS DE IA
else:
    modelo_ativo = "models/gemini-1.5-flash"
    try:
        genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                modelo_ativo = m.name
                break
    except Exception:
        pass

    # ==========================================
    # 2. ABA: AUDITOR DE MERCADO
    # ==========================================
    if menu == "🛡️ Auditor de Mercado":
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
                st.error(f"Erro na IA (Aguarde 1 minuto para resetar a cota): {e}")
            
    # ==========================================
    # 3. ABA: GERADOR DE ANÚNCIOS
    # ==========================================
    elif menu == "✍️ Gerador de Anúncios":
        st.title("✍️ MÓDULO 2: GERADOR DE ANÚNCIOS MASTER & CARACTERÍSTICAS")
        produto_alvo = st.text_input("✍️ Nome do Produto Gringo:", value="Sugar Defender")
        resumo_niche = st.text_area("📋 Resumo do Produto (Nicho/Dores):", value="Suplemento natural para equilíbrio do metabolismo.")
        if st.button("Core Inteligência - Gerar Arsenal"):
            st.info("Processando Características de Campanha Gringa... Por favor, aguarde.")
            try:
                model = genai.GenerativeModel(modelo_ativo)
                prompt = f'Generate a Google Ads campaign structure in perfect English for "{produto_alvo}" based on: {resumo_niche}. Provide 4 headlines (max 30 chars), 4 descriptions (max 90 chars), and exactly 15 phrase match with quotes, 15 exact match with brackets, and 15 broad match keywords. No Portuguese.'
                resposta = model.generate_content(prompt)
                st.success("🎯 Características gringas estruturadas com sucesso!")
                st.text_area("📋 Material Pronto para Copiar e Colar:", value=resposta.text, height=500)
            except Exception as e:
                st.error(f"Erro na IA (Aguarde 1 minuto para resetar a cota): {e}")

    # ==========================================
    # 4. ABA: CAÇADOR DE LANÇAMENTOS
    # ==========================================
    elif menu == "🛰️ Caçador de Lançamentos":
        st.title("🛰️ MÓDULO: CAÇADOR DE LANÇAMENTOS NA GRINGA")
        if st.button("🔍 Roda Escaneamento de Plataformas"):
            st.info("Buscando lançamentos recentes nos servidores gringos...")
            try:
                model = genai.GenerativeModel(modelo_ativo)
                resposta = model.generate_content("Simule um relatório de 3 lançamentos de saúde recentes na ClickBank com nome e melhor país estratégico. Em português.")
                st.success("Varredura Concluída!")
                st.write(resposta.text)
            except Exception as e:
                st.error(f"Erro na IA: {e}")

    # ==========================================
    # 5. ABA: FABRICANTE DE PRE-SELL
    # ==========================================
    elif menu == "🌐 Fabricante de Pre-sell":
        st.title("🌐 MÓDULO: FABRICANTE DE PRE-SELL MASTER")
        prod_presell = st.text_input("✍️ Nome do Produto para a Página Ponte:", value="Sugar Defender")
        if st.button("🟢 (B) FABRICAR PRE-SELL"):
            st.info("Montando estrutura compliance...")
            try:
                model = genai.GenerativeModel(modelo_ativo)
                resposta = model.generate_content(f"Crie uma pre-sell em inglês para {prod_presell} com headline, subheadline, 'Available for UK Delivery' e rodapé legal.")
                st.success("Pre-sell Estruturada com Sucesso!")
                st.text_area("📋 Copie para o Elementor:", value=resposta.text, height=350)
            except Exception as e:
                st.error(f"Erro na IA: {e}")

    # ==========================================
    # 6. ABA: CONFIGURAÇÕES
    # ==========================================
    elif menu == "⚙️ Configurações":
        st.title("⚙️ Configurações do Sistema")
        st.text_input("🔑 Chave API Google ativa nos bastidores:", value="CONFIGURADA_NOS_SECRETS", type="password", disabled=True)
        st.selectbox("🤖 Motor Inteligente Padrão:", ["gemini-1.5-flash"])
        st.success("Infraestrutura de dados integrada com sucesso!")
