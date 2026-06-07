import streamlit st as
import pandas as pd

# Configuração premium de página - Layout amplo e profissional Black
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
# INTERFACE DO MENU CENTRAL SEGUINDO SEU MODELO SEGURO DE BOTÕES DE AÇÃO DIRETA
# =====================================================================================================================
if menu == "📊 Radar de Produtos":
    st.title("📊 MÓDULO 1: RADAR DE PRODUTOS COMPREENSIVO & DINÂMICO")
    st.markdown("O sistema analisa tendências globais de busca de forma estendida na ClickBank e BuyGoods.")
    st.dataframe(dados_fixos_radar, use_container_width=True, height=550)
    csv_data = dados_fixos_radar.to_csv(index=False).encode('utf-8')
    st.download_button(label="📥 BAIXAR PLANILHA COMPLETA (.CSV)", data=csv_data, file_name="radar_produtos.csv", mime="text/csv")

if menu == "🛡️ Auditor de Mercado":
    st.title("🛡️ MÓDULO: AUDITOR DE MERCADO XEQUE-MATE")
    produto = st.text_input("Digite o nome do produto para auditar:", value="Obsesta")
    if st.button("Executar Auditoria"):
        st.session_state.resposta_auditoria = "**1. STATUS DE VALIDAÇÃO DO PRODUTO**\nO produto '" + produto + "' está 100% VALIDADO no mercado internacional de afiliados, registrando alto volume de buscas exatas de marca na ClickBank e BuyGoods. Apresenta baixa taxa de reembolso, sendo ideal para estratégias agressivas de Fundo de Funil.\n\n**2. ANÁLISE DE CONCORRÊNCIA E PREÇO DO CLIQUE (CPC)**\nNos Estados Unidos a concorrência está saturada com CPC batendo $0.85. Porém, no Reino Unido e Irlanda, o leilão encontra-se livre de grandes afiliados gringos, apresentando um CPC médio real e estimado em excelentes $0.45 por clique qualificado.\n\n**3. MAIOR DOR DO COMPRADOR GRINGO**\nO cliente final gringo busca por regulação rápida do metabolismo, controle severo de apetite por doces, perda de peso natural sem efeito sanfona e aumento massivo da disposição diária.\n\n**4. MELHOR PAÍS ESTRATÉGICO PARA ANUNCIAR (MAIOR ROI)**\nO melhor país para iniciar a campanha é o Reino Unido (United Kingdom) 🇬🇧. O leilão local em libras oferece menor concorrência, cliques muito mais baratos e alto poder de conversão se associado a uma Pre-sell blindada com aviso de bandeira local."
        st.success("Auditoria concluída com sucesso!")
    if st.session_state.resposta_auditoria:
        st.text_area("📋 Resultado da Auditoria de Mercado Real:", value=st.session_state.resposta_auditoria, height=350)

if menu == "✍️ Gerador de Anúncios":
    st.title("✍️ MÓDULO 2: GERADOR DE ANÚNCIOS")
    produto = st.text_input("Digite o nome do produto:", value="Obsesta")
    if st.button("Gerar Anúncios"):
        st.session_state.resposta_gerador = (
            "[DISPLAY PATH]\n"
            "/Official/Store\n"
            "/Secure/Order\n\n"
            "[HEADLINES - MAX 30 CHARACTERS]\n"
            "1. " + produto + " Official Site (Pin 1)\n"
            "2. Buy " + produto + " Online\n"
            "3. Original " + produto + " Formula\n"
            "4. " + produto + " Best Price\n\n"
            "[DESCRIPTIONS - MAX 90 CHARACTERS]\n"
            "1. Order " + produto + " from the official website today and get exclusive package discounts.\n"
            "2. Get the original " + produto + " with a 100% 60-day money-back guarantee. Secure checkout.\n"
            "3. 100% natural formula backed by clinical research. Fast shipping options available now.\n"
            "4. Save big on multi-bottle packages today. Enjoy secure checkout and fast delivery.\n\n"
            "[PHRASE MATCH KEYWORDS - WITH QUOTES - 15 UNIQUE TERMS]\n"
            "1. \"" + produto + " official website\"\n"
            "2. \"buy " + produto + " online\"\n"
            "3. \"" + produto + " discount price\"\n"
            "4. \"order " + produto + " online\"\n"
            "5. \"" + produto + " where to buy\"\n"
            "6. \"" + produto + " store\"\n"
            "7. \"" + produto + " price\"\n'
            '8. \"get " + produto + "\"\n'
            '9. \"purchase " + produto + "\"\n'
            '10. \"" + produto + " sale\"\n'
            '11. \"" + produto + " supplement\"\n'
            '12. \"" + produto + " official store\"\n'
            '13. \"" + produto + " best price\"\n'
            '14. \"secure " + produto + " order\"\n'
            '15. \"" + produto + " check out\"\n\n'
            '[EXACT MATCH KEYWORDS - WITH BRACKETS - 15 UNIQUE TERMS]\n'
            '1. [' + produto + ' official website]\n'
            '2. [buy ' + produto + ' online]\n'
            '3. [' + produto + ' discount price]\n'
            '4. [order ' + produto + ' online]\n'
            '5. [' + produto + ' where to buy]\n'
            '6. [' + produto + ' store]\n'
            '7. [' + produto + ' price]\n'
            '8. [get ' + produto + ']\n'
            '9. [purchase ' + produto + ']\n'
            '10. [' + produto + ' sale]\n'
            '11. [' + produto + ' supplement]\n'
            '12. [' + produto + ' official store]\n'
            '13. [' + produto + ' best price]\n'
            '14. [secure ' + produto + ' order]\n'
            '15. [' + produto + ']\n\n'
            '[NEGATIVE KEYWORDS - LISTA PROFISSIONAL LINHA POR LINHA]\n'
            '1. scam\n'
            '2. reviews\n'
            '3. complaints\n'
            '4. ingredients\n'
            '5. side effects\n'
            '6. free pdf\n'
            '7. amazon\n'
            '8. walmart\n'
            '9. ebay\n'
            '10. discount code\n'
            '11. coupon\n'
            '12. target\n'
            '13. refund\n'
            '14. fake\n'
            '15. wholesale'
        )
        st.success("Anuncio completo gerado com sucesso!")
    if st.session_state.resposta_gerador:
        st.text_area("📋 Resultado dos Anúncios e Palavras-Chave Ordenadas:", value=st.session_state.resposta_gerador, height=550)

if menu == "🛰️ Caçador de Lançamentos":
    st.title("🛰️ MÓDULO: CAÇADOR DE LANÇAMENTOS")
    if st.button("Simular Lançamentos"):
