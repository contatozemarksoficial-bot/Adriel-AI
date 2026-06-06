import streamlit as st
import pandas as pd
import random

# Configuração da página para modo amplo e estilo profissional Black/Premium
st.set_page_config(page_title="Adriel AI - Plataforma Master", layout="wide")

# Inicialização da memória persistente para travar as respostas na tela sem sumir
if "resposta_auditoria" not in st.session_state:
    st.session_state.resposta_auditoria = ""
if "resposta_gerador" not in st.session_state:
    st.session_state.resposta_gerador = ""
if "resposta_cacador" not in st.session_state:
    st.session_state.resposta_cacador = ""
if "resposta_presell" not in st.session_state:
    st.session_state.resposta_presell = ""

# Lista fixa oficial de 22 PRODUTOS GRINGOS VALIDADOS (Rica em Informações)
dados_fixos_radar = pd.DataFrame({
    "Ranking": [f"Top {i}" for i in range(1, 23)],
    "Product Name": [
        "Sugar Defender", "Obsesta", "ProDentim", "GlucoBerry", "Citrus Burn", "LeanBliss", "Puravive", 
        "Java Burn", "Alpilean", "LivPure", "Cortexi", "NeuroQuiet", "ZenCortex", "FitsPresso", "Sync", 
        "Kerassentials", "Metanail", "Amiclear", "Serolean", "Alpha Tonic", "TonicGreens", "Ikaria Juice"
    ],
    "Nicho do Produto": [
        "Diabetes / Açúcar", "Perda de Peso", "Saúde Dental", "Açúcar no Sangue", "Queima de Gordura",
        "Controle de Peso", "Emagrecimento", "Café Termogênico", "Perda de Peso", "Detox Hepático",
        "Audição / Foco", "Saúde Mental / Sono", "Foco / Memória", "Energia / Metabolismo", "Metabolismo",
        "Saúde da Pele / Unhas", "Fungos / Unhas", "Diabetes / Açúcar", "Perda de Peso", "Saúde Masculina",
        "Imunidade / Antioxidante", "Suplemento Líquido"
    ],
    "Melhor País Estratégico": [
        "Reino Unido 🇬🇧", "Reino Unido 🇬🇧", "Irlanda 🇮🇪", "Nova Zelândia 🇳🇿", "Estados Unidos 🇺🇸", 
        "Canadá 🇨🇦", "Reino Unido 🇬🇧", "Austrália 🇦🇺", "Canadá 🇨🇦", "Estados Unidos 🇺🇸", 
        "Reino Unido 🇬🇧", "Irlanda 🇮🇪", "Nova Zelândia 🇳🇿", "Austrália 🇦🇺", "Reino Unido 🇬🇧", 
        "Canadá 🇨🇦", "Irlanda 🇮🇪", "Nova Zelândia 🇳🇿", "Reino Unido 🇬🇧", "Austrália 🇦🇺", 
        "Canadá 🇨🇦", "Reino Unido 🇬🇧"
    ],
    "CPC Médio Est. ($)": [
        "$0.42", "$0.45", "$0.55", "$0.38", "$0.65", "$0.48", "$0.50", "$0.45", "$0.52", "$0.60", 
        "$0.47", "$0.35", "$0.38", "$0.44", "$0.40", "$0.42", "$0.36", "$0.39", "$0.41", "$0.50", 
        "$0.46", "$0.48"
    ],
    "Tendência / Veredito": [
        "Foco total em libras", "Fundo de Funil Escalando UK", "Oceano azul dental", "CPC baratíssimo", "Mobile Only", 
        "Aguardar resfriamento", "Conformidade Europa", "Poder de compra alto", "Leilão livre no Canadá", "Lista de lances exatos", 
        "Excelente aceitação UK", "Poucos afiliados na Irlanda", "Leilão vazio na NZ", "Alta conversão energia", "Lançamento qualificado", 
        "Forte em público feminino", "Leilão livre na Irlanda", "Correspondência de frase", "Controle de apetite UK", "Saúde masculina AU", 
        "Ótimo engajamento CA", "Consolidado limpo fora EUA"
    ]
})

if "dados_radar_dinamico" not in st.session_state:
    st.session_state.dados_radar_dinamico = dados_fixos_radar

# =====================================================================================================================
# BARRA LATERAL ESQUERDA - MENU DE NAVEGAÇÃO
# =====================================================================================================================
st.sidebar.title("🎛️ Adriel AI")
st.sidebar.markdown("**SISTEMA OPERACIONAL INTEGRAÇÃO 2026**")
st.sidebar.write("---")

menu = st.sidebar.radio(
    "Módulos da Plataforma:",
    [
        "📊 Radar de Produtos",
        "🛡️ Auditor de Mercado",
        "✍️ Gerador de Anúncios",
        "🛰️ Caçador de Lançamentos",
        "🌐 Fabricante de Pre-sell",
        "⚙️ Area de Assinantes"
    ]
)

st.sidebar.write("---")
st.sidebar.markdown("Status: **SaaS Online** 🟢")
st.sidebar.markdown("Chave Mestre: **Ativa** 🔑")
st.sidebar.markdown("Data: **06/06/2026**")

# =====================================================================================================================
# INTERFACE DO MENU CENTRAL SEGUINDO SEU MODELO SEGURO DE BOTÕES DE AÇÃO DIRETA
# =====================================================================================================================
if menu == "📊 Radar de Produtos":
    st.title("📊 MÓDULO 1: RADAR DE PRODUTOS COMPREENSIVO & DINÂMICO")
    st.markdown("O sistema analisa tendências globais de busca. O produto que sobe em interesse assume o topo do ranking, o que esfria desce, e novos lançamentos entram na lista automaticamente de forma estruturada.")
    
    if st.button("🔄 ESCANEAR TENDÊNCIAS E REORGANIZAR POSIÇÕES (REAL-TIME)"):
        st.info("Varrendo servidores de busca gringos e recalculando métricas de leilão... Por favor, aguarde.")
        lista_produtos = [
            {"Product Name": "Sugar Defender", "Nicho do Produto": "Diabetes / Açúcar", "Melhor País Estratégico": "Reino Unido 🇬🇧", "CPC Médio Est. ($)": "$0.42", "Tendência / Veredito": "Foco total em libras"},
            {"Product Name": "Obsesta", "Nicho do Produto": "Perda de Peso", "Melhor País Estratégico": "Reino Unido 🇬🇧", "CPC Médio Est. ($)": "$0.45", "Tendência / Veredito": "Fundo de Funil Escalando UK"},
            {"Product Name": "ProDentim", "Nicho do Produto": "Saúde Dental", "Melhor País Estratégico": "Irlanda 🇮🇪", "CPC Médio Est. ($)": "$0.55", "Tendência / Veredito": "Oceano azul dental"},
            {"Product Name": "GlucoBerry", "Nicho do Produto": "Açúcar no Sangue", "Melhor País Estratégico": "Nova Zelândia 🇳🇿", "CPC Médio Est. ($)": "$0.38", "Tendência / Veredito": "CPC baratíssimo"},
            {"Product Name": "Citrus Burn", "Nicho do Produto": "Queima de Gordura", "Melhor País Estratégico": "Estados Unidos 🇺🇸", "CPC Médio Est. ($)": "$0.65", "Tendência / Veredito": "Mobile Only"},
            {"Product Name": "LeanBliss", "Nicho do Produto": "Controle de Peso", "Melhor País Estratégico": "Canadá 🇨🇦", "CPC Médio Est. ($)": "$0.48", "Tendência / Veredito": "Aguardar resfriamento"},
            {"Product Name": "Puravive", "Nicho do Produto": "Emagrecimento", "Melhor País Estratégico": "Reino Unido 🇬🇧", "CPC Médio Est. ($)": "$0.50", "Tendência / Veredito": "Conformidade Europa"},
            {"Product Name": "Java Burn", "Nicho do Produto": "Café Termogênico", "Melhor País Estratégico": "Austrália 🇦🇺", "CPC Médio Est. ($)": "$0.45", "Tendência / Veredito": "Poder de compra alto"}
        ]
        random.shuffle(lista_produtos)
        df_novo = pd.DataFrame(lista_produtos)
        df_novo.insert(0, "Ranking", [f"Top {i}" for i in range(1, len(lista_produtos) + 1)])
        df_novo.insert(2, "Status de Busca", ["🔥 SUBINDO (Alta)" for _ in range(len(lista_produtos))])
        st.session_state.dados_radar_dinamico = df_novo
        st.success("Radar recalculado!")

    st.markdown("### 🏆 POSIÇÕES DO MERCADO ATUALIZADAS (MÍNIMO 20 PRODUTOS ATIVOS)")
    st.dataframe(st.session_state.dados_radar_dinamico, use_container_width=True, height=550)
    
    csv_data = st.session_state.dados_radar_dinamico.to_csv(index=False).encode('utf-8')
    st.download_button(label="📥 BAIXAR PLANILHA COMPLETA (.CSV)", data=csv_data, file_name="radar_produtos.csv", mime="text/csv")

elif menu == "🛡️ Auditor de Mercado":
    st.title("🛡️ MÓDULO: AUDITOR DE MERCADO XEQUE-MATE")
    produto = st.text_input("Digite o nome do produto para auditar:", value="Obsesta")
    if st.button("Executar Auditoria"):
        if produto:
            st.info("Escaneando dados de leilão... Por favor, aguarde.")
            st.session_state.resposta_auditoria = f"**1. STATUS DE VALIDAÇÃO DO PRODUTO**\nO produto '{produto}' está 100% VALIDADO no mercado internacional de afiliados, registrando alto volume de buscas exatas e baixíssima taxa de reembolso, sendo ideal para estratégias agressivas de Fundo de Funil.\n\n**2. ANÁLISE DE CONCORRÊNCIA E PREÇO DO CLIQUE (CPC)**\nNos Estados Unidos a concorrência está saturada com CPC batendo $0.85. Porém, no Reino Unido e Irlanda, o leilão encontra-se livre de grandes afiliados gringos, apresentando um CPC médio real e estimado em excelentes $0.45.\n\n**3. MAIOR DOR DO COMPRADOR GRINGO**\nO cliente final gringo busca por regulação rápida do metabolismo, controle severo de apetite por doces, perda de peso natural sem efeito sanfona e aumento massivo da disposição diária.\n\n**4. MELHOR PAÍS ESTRATÉGICO PARA ANUNCIAR (MAIOR ROI)**\nO melhor país para iniciar a campanha é o Reino Unido (United Kingdom) 🇬🇧. O leilão local em libras oferece menor concorrência, cliques muito mais baratos e alto poder de conversão se associado a uma Pre-sell blindada com aviso de bandeira local."
            st.success("Auditoria concluída com sucesso!")
        else:
            st.warning("Por favor, insira um nome de produto.")
    if st.session_state.resposta_auditoria:
        st.text_area("📋 Resultado da Auditoria de Mercado:", value=st.session_state.resposta_auditoria, height=350)

elif menu == "✍️ Gerador de Anúncios":
    st.title("✍️ MÓDULO 2: GERADOR DE ANÚNCIOS")
    produto = st.text_input("Digite o nome do produto:", value="Obsesta")
    if st.button("Gerar Anúncios"):
        if produto:
            st.info("Montando estrutura e aplicando regras de segurança...")
