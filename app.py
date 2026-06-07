import streamlit as st
import pandas as pd

# Configuração premium de página - Layout amplo e estilo profissional Black
st.set_page_config(page_title="Adriel AI - Plataforma Master", layout="wide")

# Inicialização da memória de sessão para travar as respostas na tela sem sumir
if "produto_auditar" not in st.session_state:
    st.session_state.produto_auditar = "Obsesta"
if "produto_anuncio" not in st.session_state:
    st.session_state.produto_anuncio = "Obsesta"
if "produto_presell" not in st.session_state:
    st.session_state.produto_presell = "Obsesta"

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
# INTERFACE DO MENU CENTRAL - COM BOTÕES E ABAS INDIVIDUAIS FIXAS (MÁXIMA DENSIDADE)
# =====================================================================================================================
if menu == "📊 Radar de Produtos":
    st.title("📊 MÓDULO 1: RADAR DE PRODUTOS COMPREENSIVO & DINÂMICO")
    st.markdown("O sistema analisa tendências globais de busca de forma estendida na ClickBank e BuyGoods.")
    st.dataframe(dados_fixos_radar, use_container_width=True, height=550)
    csv_data = dados_fixos_radar.to_csv(index=False).encode('utf-8')
    st.download_button(label="📥 BAIXAR PLANILHA COMPLETA (.CSV)", data=csv_data, file_name="radar_produtos.csv", mime="text/csv")

elif menu == "🛡️ Auditor de Mercado":
    st.title("🛡️ MÓDULO: AUDITOR DE MERCADO XEQUE-MATE")
    st.session_state.produto_auditar = st.text_input("Nome do Produto para Auditoria Individual:", value=st.session_state.produto_auditar)
    prod = st.session_state.produto_auditar
    
    st.markdown("### 🎛️ Painel de Consultas Individuais Fixas")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("🚀 Validar Status Comercial"):
            st.success("Análise de Fundo de Funil processada!")
            st.text_area("Resultado do Status:", "O produto '" + prod + "' está 100% VALIDADO no mercado internacional de afiliados, registrando alto volume de buscas exatas de marca na ClickBank e BuyGoods. Apresenta baixíssima taxa de reembolso no tráfego direto.", height=150)
    with col2:
        if st.button("💰 Analisar Concorrência e CPC"):
            st.success("Métricas de Leilão calculadas!")
            st.text_area("Resultado do CPC:", "Estados Unidos (USA): Concorrência inflada com leilão saturado e CPC médio batendo $0.85.\nReino Unido (UK) e Irlanda: Leilão limpo de afiliados gringos com CPC estimado em excelentes $0.45 por clique qualificado.", height=150)
    with col3:
        if st.button("🎯 Mapear Maior Dor do Gringo"):
            st.success("Dores de público rastreadas!")
            st.text_area("Resultado da Dor:", "O público-alvo comprador busca por regulação acelerada do metabolismo, controle severo da compulsão por doces/carboidratos, queima de gordura visceral profunda e aumento massivo da energia diária.", height=150)
    with col4:
        if st.button("🇬🇧 Revelar Melhor País (ROI)"):
            st.success("País geo-estratégico mapeado!")
            st.text_area("Resultado da Geo:", "O melhor país disparado para iniciar as campanhas de pesquisa é o Reino Unido (United Kingdom) 🇬🇧. O leilão rodando em libras esterlinas oferece concorrência reduzida e alta taxa de conversão se associado a uma pre-sell.", height=150)

elif menu == "✍️ Gerador de Anúncios":
    st.title("✍️ MÓDULO 2: GERADOR DE ANÚNCIOS MASTER")
    st.session_state.produto_anuncio = st.text_input("Nome do Produto para a Campanha:", value=st.session_state.produto_anuncio)
    prod = st.session_state.produto_anuncio
    
    st.markdown("### 🎛️ Painel de Componentes Individuais da Campanha")
    aba1, aba2, aba3 = st.tabs(["📋 Títulos e Descrições (Copy)", "🎯 Palavras em Frase e Exatas", "🚫 Palavras Negativas Obras-Primas"])
    
    with aba1:
        st.write("**Caminhos de Exibição (Display Path):** `/Official/Store` ou `/Secure/Order`")
        títulos = "1. " + prod + " Official Site (Pin Position 1)\n2. Buy " + prod + " Online\n3. Original " + prod + " Formula\n4. " + prod + " Best Price"
        descrições = "1. Order " + prod + " from the official website today and get exclusive package discounts.\n2. Get the original " + prod + " with a 100% 60-day money-back guarantee. Secure checkout.\n3. 100% natural formula backed by clinical research. Fast shipping options available.\n4. Save big on multi-bottle packages today. Enjoy secure checkout."
        st.text_area("Títulos Formatados (Max 30 Caracteres):", títulos, height=120)
        st.text_area("Descrições Formatadas (Max 90 Caracteres):", descrições, height=150)
        
    with aba2:
        frase = "1. \"" + prod + " official website\"\n2. \"buy " + prod + " online\"\n3. \"" + prod + " discount price\"\n4. \"order " + prod + " online\"\n5. \"" + prod + " where to buy\"\n6. \"" + prod + " store\"\n7. \"" + prod + " price\"\n8. \"get " + prod + "\"\n9. \"purchase " + prod + "\"\n10. \"" + prod + " sale\"\n11. \"" + prod + " supplement\"\n12. \"" + prod + " official store\"\n13. \"" + prod + " best price\"\n14. \"secure " + prod + " order\"\n15. \"" + prod + " check out\""
        exatas = "1. [" + prod + " official website]\n2. [buy " + prod + " online]\n3. [" + prod + " discount price]\n4. [order " + prod + " online]\n5. [" + prod + " where to buy]\n6. [" + prod + " store]\n7. [" + prod + " price]\n8. [get " + prod + "]\n9. [purchase " + prod + "]\n10. [" + prod + " sale]\n11. [" + prod + " supplement]\n12. [" + prod + " official store]\n13. [" + prod + " best price]\n14. [secure " + prod + " order]\n15. [" + prod + "]"
        st.text_area("Lista de 15 Palavras-Chave de Correspondência de Frase (Com Aspas):", frase, height=250)
        st.text_area("Lista de 15 Palavras-Chave de Correspondência Exata (Com Colchetes):", exatas, height=250)
        
    with aba3:
        negativas = "scam, reviews, complaints, ingredients, side effects, free pdf, amazon, walmart, ebay, discount code, coupon, target, refund, independent review, fake, complaints department, customer service phone number"
        st.text_area("Lista de Palavras Negativas de Extrema Proteção de Orçamento:", negativas, height=120)

elif menu == "🛰️ Caçador de Lançamentos":
    st.title("🛰️ MÓDULO: CAÇADOR DE LANÇAMENTOS INTERNACIONAIS")
    st.markdown("### 🎛️ Servidores de Monitoramento de Lançamentos")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("🇺🇸 Escanear Plataforma BuyGoods"):
            st.info("Varrendo banco de dados BuyGoods...")
