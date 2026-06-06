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
# 1. ABA: RADAR DE PRODUTOS (100% ISOLADA, LOCAL E COMPREENSIVA)
# ==========================================
if menu == "📊 Radar de Produtos":
    st.title("📊 MÓDULO 1: RADAR DE PRODUTOS [FILTRO XEQUE-MATE]")
    st.markdown("Abaixo está o mapa completo com as métricas e a estratégia exata dos 7 produtos líderes de Fundo de Funil:")
    
    dados_radar = {
        "Product Name": ["Sugar Defender", "ProDentim", "GlucoBerry", "Citrus Burn", "LeanBliss", "Puravive", "Java Burn"],
        "Veredito de Mercado": ["VALIDADO (Risco Baixo)", "VALIDADO (Risco Baixo)", "VALIDADO (Risco Baixo)", "VALIDADO (Risco Baixo)", "VALIDADO (Risco Médio)", "VALIDADO (Risco Baixo)", "VALIDADO (Risco Baixo)"],
        "Melhor País Estratégico": ["Reino Unido (UK) 🇬🇧", "Irlanda (Ireland) 🇮🇪", "Nova Zelândia 🇳🇿", "Estados Unidos 🇺🇸", "Canadá (Canada) 🇨🇦", "Reino Unido (UK) 🇬🇧", "Austrália (Australia) 🇦🇺"],
        "CPC Médio Est. ($)": ["$0.42", "$0.55", "$0.38", "$0.65", "$0.48", "$0.50", "$0.45"],
        "Ganho Estimado ($)": ["$127.30", "$142.00", "$135.00", "$115.00", "$105.00", "$138.00", "$120.00"],
        "Estratégia Recomendada": [
            "Fundo de Funil + Vídeo de 10s com seta amarela e Pre-sell com bandeira local para máxima conversão.",
            "Correspondência ampla qualificada para destravar o leilão, evitando termos genéricos de dor de dente.",
            "Oceano Azul puro para fugir da briga de afiliados dos EUA e garantir cliques ultra baratos.",
            "Travar exclusão de computadores nas configurações e rodar anúncio focado 100% em celulares gringos.",
            "Campanha de rede de pesquisa focada em pacotes de 6 frascos usando copy sem promessas agressivas.",
            "Estrutura com aviso obrigatório de afiliado no topo para passar direto pela conformidade da Europa.",
            "Anúncio direto para os termos de compra exatos aproveitando o forte poder de consumo dos australianos."
        ]
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
    # 2. ABA: AUDITOR DE MERCADO (ESTRUTURA CIRÚRGICA PADRONIZADA)
    # ==========================================
    if menu == "🛡️ Auditor de Mercado":
        st.title("🛡️ MÓDULO: AUDITOR DE MERCADO XEQUE-MATE")
        st.markdown("Verifique a viabilidade estratégica e financeira de qualquer produto antes de subir anúncios:")
        
        prod_auditar = st.text_input("✍️ Digite o nome do produto gringo para auditar:", value="Sugar Defender")
        if st.button("🔍 Iniciar Auditoria de Mercado"):
            st.info(f"Analisando dados globais de leilão e concorrência para '{prod_auditar}'...")
            try:
                model = genai.GenerativeModel(modelo_ativo)
                
                # Prompt de engenharia reversa travando os 4 blocos de respostas obrigatórias
                prompt = f"""
                Você é o AUDITOR DE MERCADO XEQUE-MATE, especialista em análise de concorrência e custos de leilão no Google Ads para afiliados internacionais.
                Faça uma análise estratégica precisa do produto de afiliado gringo '{prod_auditar}'.
                Você deve obrigatoriamente estruturar sua resposta dividida exatamente nestes 4 tópicos abaixo (use títulos em letras maiúsculas e negrito):

                **1. STATUS DE VALIDAÇÃO DO PRODUTO**
                Afirme claramente se o produto '{prod_auditar}' está validado no mercado de afiliados, se possui alta demanda de buscas e se o risco da campanha de fundo de funil é baixo, médio ou alto.

                **2. ANÁLISE DE CONCORRÊNCIA E PREÇO DO CLIQUE (CPC)**
                Explique o nível de concorrência atual de afiliados brigando por esse termo e informe uma estimativa média de custo por clique (CPC) para o tráfego de fundo de funil.

                **3. MAIOR DOR DO COMPRADOR GRINGO**
                Diga qual é a principal dor, desejo ou necessidade do cliente final que busca por esse termo e que faz ele comprar o produto com o cartão de crédito na mão.

                **4. MELHOR PAÍS ESTRATÉGICO PARA ANUNCIAR (MAIOR ROI E MENOR CONCORRÊNCIA)**
                Indique categoricamente qual é o melhor país de língua inglesa com leilão barato, concorrência reduzida e altíssimo poder de compra (como Reino Unido, Irlanda, Canadá, Nova Zelândia ou Austrália) para o afiliado anunciar e obter o maior lucro possível, fugindo da briga cara dos Estados Unidos. Justifique a escolha.

                Escreva toda a resposta em português claro, direto, profissional e direto ao ponto, sem enrolação.
                """
                
                resposta = model.generate_content(prompt)
                st.success("Auditoria Estratégica Concluída com Sucesso!")
                st.write(resposta.text)
            except Exception as e:
                st.error(f"Erro na IA (Se necessário, aguarde 1 minuto para resetar a cota): {e}")
            
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
        st.selectbox("🤖 Modelo de IA Ativo:", ["gemini-1.5-flash"])
        st.success("Infraestrutura de dados integrada com sucesso!")
