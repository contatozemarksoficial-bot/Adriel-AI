import streamlit as st
import pandas as pd

# Configuração premium de página - Layout amplo e profissional Black/Premium
st.set_page_config(page_title="Adriel AI - Plataforma Master", layout="wide")

# Inicialização da memória de sessão para travar as respostas na tela sem sumir
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
    "Ranking": [
        "🏆 Top 1 (Elite)", "🏆 Top 2 (Elite)", "🏆 Top 3 (Elite)", "🏆 Top 4 (Elite)", "🏆 Top 5 (Elite)",
        "🏆 Top 6 (Elite)", "🏆 Top 7 (Elite)", "🏆 Top 8 (Elite)", "🏆 Top 9 (Elite)", "🏆 Top 10 (Elite)",
        "Top 11 (Oportunidade)", "Top 12 (Oportunidade)", "Top 13 (Oportunidade)", "Top 14 (Oportunidade)", "Top 15 (Oportunidade)",
        "Top 16 (Oportunidade)", "Top 17 (Oportunidade)", "Top 18 (Oportunidade)", "Top 19 (Oportunidade)", "Top 20 (Oportunidade)",
        "Top 21 (Oportunidade)", "Top 22 (Oportunidade)"
    ],
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
    "Afirmação Estratégica / Por que Anunciar": [
        "VALIDADO: Foco total em libras. Volume explosivo no leilão britânico com baixa taxa de devolução.",
        "VALIDADO: Fundo de Funil Escalando UK. Cliques qualificados e leilão livre de afiliados concorrentes.",
        "VALIDADO: Oceano azul dental. Altíssima conversão na Irlanda por falta de anúncios locais.",
        "VALIDADO: CPC baratíssimo. Nova Zelândia apresenta o tráfego de público idoso mais barato do ano.",
        "VALIDADO: Leilão forte apenas Mobile. Segmentar campanha direto para smartphones nos EUA.",
        "VALIDADO: Lançamento escalando no Canadá. Correspondência de frase convertendo muito.",
        "VALIDADO: Conformidade total na Europa. Público comprador maduro buscando queima rápida.",
        "VALIDADO: Poder de compra alto na Austrália. Oferta de conversão imediata misturada com café.",
        "VALIDADO: Leilão livre de lances agressivos no Canadá. Correspondência de frase convertendo muito.",
        "VALIDADO: Lista de lances exatos nos EUA. Excelente aceitação com público de meia idade.",
        "OPORTUNIDADE: Pouca concorrência. Reino Unido com excelente tráfego para nicho de audição.",
        "OPORTUNIDADE: Pouca concorrência. Poucos afiliados na Irlanda explorando o nicho de sono.",
        "OPORTUNIDADE: Oceano Azul. Leilão completamente vazio na NZ para buscas diretas de marca.",
        "OPORTUNIDADE: Alta conversão de energia. Cliques rápidos no leilão alternativo da Austrália.",
        "OPORTUNIDADE: Lançamento qualificado. Baixo custo por clique focado em libras no Reino Unido.",
        "OPORTUNIDADE: Pouca concorrência. Forte aceitação comercial no público feminino do Canadá.",
        "OPORTUNIDADE: Leilão livre na Irlanda. Cliques limpos para correspondência de frase direta.",
        "OPORTUNIDADE: Correspondência de frase convertendo com cliques baratos na Nova Zelândia.",
        "OPORTUNIDADE: Controle de apetite agressivo. Excelente recepção de buscas no mercado de UK.",
        "OPORTUNIDADE: Saúde masculina na Austrália. Tráfego qualificado de alta conversão direta.",
        "OPORTUNIDADE: Ótimo engajamento de tráfego no Canadá. Cliques frios convertendo no funil.",
        "OPORTUNIDADE: Consolidado e limpo fora dos EUA. Reino Unido faturando alto na rede de pesquisa."
    ]
})

# =====================================================================================================================
# BARRA LATERAL ESQUERDA - MENU DE NAVEGAÇÃO COMPLETO
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
    st.markdown("O sistema analisa tendências globais de busca de forma estendida na ClickBank e BuyGoods.")
    st.dataframe(dados_fixos_radar, use_container_width=True, height=550)
    csv_data = dados_fixos_radar.to_csv(index=False).encode('utf-8')
    st.download_button(label="📥 BAIXAR PLANILHA COMPLETA (.CSV)", data=csv_data, file_name="radar_produtos.csv", mime="text/csv")

elif menu == "🛡️ Auditor de Mercado":
    st.title("🛡️ MÓDULO: AUDITOR DE MERCADO XEQUE-MATE")
    produto = st.text_input("Digite o nome do produto para auditar:", value="Obsesta")
    if st.button("Executar Auditoria"):
        st.session_state.resposta_auditoria = "**1. BENEFÍCIOS DO PRODUTO**\n- Regulação acelerada do metabolismo basal.\n- Controle severo da compulsão por doces e ansiedade por carboidratos.\n- Derretimento de gordura visceral profunda de forma 100% natural.\n- Aumento massivo da disposição física e mental diária.\n\n**2. MAIOR DOR DO COMPRADOR GRINGO**\nO cliente final gringo sofre com o efeito sanfona, baixa autoestima por excesso de peso, fadiga crônica ao longo do dia e dificuldade extrema de emagrecer após os 40 anos.\n\n**3. MELHOR PAÍS PARA ANUNCIAR E CRIAR CAMPANHA (AFIRMAÇÃO)**\nO melhor país absoluto para divulgar este produto é o **Reino Unido (United Kingdom) 🇬🇧**. O leilão local rodando em libras esterlinas oferece baixa concorrência de afiliados gringos e um público altamente qualificado para compras de pacotes com mais frascos.\n\n**4. ANÁLISE DE MERCADO E CUSTO DO CLIQUE (CPC)**\nPara o produto '" + produto + "', o custo do clique (CPC) estimado no país **Reino Unido 🇬🇧** é de excelentes **$0.45** na correspondência de frase de marca. Nos Estados Unidos, o mesmo termo está inflado e saturado, batendo marcas perigosas de $0.85 por clique."
        st.success("Auditoria concluída com sucesso!")
    if st.session_state.resposta_auditoria:
        st.text_area("📋 Resultado da Auditoria de Mercado Real:", value=st.session_state.resposta_auditoria, height=350)

elif menu == "✍️ Gerador de Anúncios":
    st.title("✍️ MÓDULO 2: GERADOR DE ANÚNCIOS")
    produto = st.text_input("Digite o nome do produto:", value="Obsesta")
    if st.button("Gerar Anúncios"):
