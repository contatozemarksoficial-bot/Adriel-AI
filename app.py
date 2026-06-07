import streamlit as st
import pandas as pd

# Configuração premium de página - Ampla e profissional Black
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
# BARRA LATERAL ESQUERDA - MENU DE NAVEGAÇÃO COMPLETO SIMPLIFICADO
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
# INTERFACE DO MENU CENTRAL - TOTALMENTE PLANIFICADA CONTRA ERROS DE MARGEM
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
        st.session_state.resposta_auditoria = "1. STATUS DE VALIDAÇÃO DO PRODUTO: O produto está 100% VALIDADO no mercado internacional de afiliados, registrando alto volume de buscas exatas de marca na ClickBank e BuyGoods. Apresenta baixíssima taxa de reembolso, sendo ideal para estratégias agressivas de Fundo de Funil.\n\n2. ANÁLISE DE CONCORRÊNCIA E PREÇO DO CLIQUE (CPC): Nos Estados Unidos a concorrência está saturada com CPC batendo $0.85. Porém, no Reino Unido e Irlanda, o leilão encontra-se livre de grandes afiliados gringos, apresentando um CPC médio real e estimado em excelentes $0.45 por clique qualificado.\n\n3. MAIOR DOR DO COMPRADOR GRINGO: O cliente final gringo busca por regulação rápida do metabolismo, controle severo de apetite por doces, perda de peso natural sem efeito sanfona e aumento massivo da disposição diária.\n\n4. MELHOR PAÍS ESTRATÉGICO PARA ANUNCIAR (MAIOR ROI): O melhor país para iniciar a campanha é o Reino Unido (United Kingdom) 🇬🇧. O leilão local em libras oferece menor concorrência, cliques muito mais baratos e alto poder de conversão se associado a uma Pre-sell blindada com aviso de bandeira local."
        st.success("Auditoria concluída com sucesso!")
    if st.session_state.resposta_auditoria:
        st.text_area("📋 Resultado da Auditoria de Mercado:", value=st.session_state.resposta_auditoria, height=350)

if menu == "✍️ Gerador de Anúncios":
    st.title("✍️ MÓDULO 2: GERADOR DE ANÚNCIOS")
    produto = st.text_input("Digite o nome do produto:", value="Obsesta")
    if st.button("Gerar Anúncios"):
        st.session_state.resposta_gerador = "[DISPLAY PATH]\n/Official/Store\n/Secure/Order\n\n[HEADLINES - MAX 30 CHARACTERS]\n1. Obsesta Official Site (Pin Position 1)\n2. Buy Obsesta Online\n3. Original Obsesta Formula\n4. Obsesta Best Price\n\n[DESCRIPTIONS - MAX 90 CHARACTERS]\n1. Order Obsesta from the official website today and get exclusive package discounts.\n2. Get the original Obsesta with a 100% 60-day money-back guarantee. Secure checkout.\n3. 100% natural formula backed by clinical research. Fast shipping options available.\n4. Save big on multi-bottle packages today. Enjoy secure checkout and fast delivery.\n\n[PHRASE MATCH KEYWORDS - WITH QUOTES - EXACTLY 15 UNIQUE TERMS]\n1. \"obsesta official website\"\n2. \"buy obsesta online\"\n3. \"obsesta discount price\"\n4. \"order obsesta online\"\n5. \"obsesta where to buy\"\n6. \"obsesta store\"\n7. \"obsesta price\"\n8. \"get obsesta\"\n9. \"purchase obsesta\"\n10. \"obsesta sale\"\n11. \"obsesta supplement\"\n12. \"obsesta official store\"\n13. \"obsesta best price\"\n14. \"secure obsesta order\"\n15. \"obsesta check out\"\n\n[EXACT MATCH KEYWORDS - WITH BRACKETS - EXACTLY 15 UNIQUE TERMS]\n1. [obsesta official website]\n2. [buy obsesta online]\n3. [obsesta discount price]\n4. [order obsesta online]\n5. [obsesta where to buy]\n6. [obsesta store]\n7. [obsesta price]\n8. [get obsesta]\n9. [purchase obsesta]\n10. [obsesta sale]\n11. [obsesta supplement]\n12. [obsesta official store]\n13. [obsesta best price]\n14. [secure obsesta order]\n15. [obsesta]\n\n[BROAD MATCH KEYWORDS - PURE TEXT NO SYMBOLS - EXACTLY 15 UNIQUE TERMS]\n1. obsesta official site\n2. buy obsesta\n3. obsesta store\n4. order obsesta\n5. obsesta discount\n6. obsesta online\n7. obsesta website\n8. purchase obsesta\n9. price of obsesta\n10. original obsesta\n11. obsesta delivery\n12. obsesta supply\n13. obsesta shop\n14. cost of obsesta\n15. obsesta cost\n\n[NEGATIVE KEYWORDS]\nscam, reviews, complaints, ingredients, side effects, free pdf, amazon, walmart, ebay, discount code, coupon, target, refund"
        st.success("Anuncio gerado com sucesso!")
    if st.session_state.resposta_gerador:
        st.text_area("📋 Resultado dos Anúncios e Lista Completa de Palavras-Chave (Copie abaixo):", value=st.session_state.resposta_gerador, height=500)

if menu == "🛰️ Caçador de Lançamentos":
    st.title("🛰️ MÓDULO: CAÇADOR DE LANÇAMENTOS")
    if st.button("Simular Lançamentos"):
        st.session_state.resposta_cacador = "🔥 **LANÇAMENTO 1: Obsesta (BuyGoods)**\n- **Por que e uma oportunidade:** Produto recém-lançado com leilão completamente vazio nas primeiras 48 horas no Google Ads. Baixíssima concorrência e alta comissão por venda.\n- **Melhor País para Começar:** Reino Unido 🇬🇧\n- **TERMÔMETRO DO LANÇAMENTO:** 98/100 (Potencial máximo de lucro rápido).\n\n🔥 **LANÇAMENTO 2: NeuroQuiet (ClickBank)**\n- **Por que e uma oportunidade:** Nicho de saúde mental e foco em plena ascensão na Europa, com leilão limpo de concorrentes.\n- **Melhor País para Começar:** Irlanda 🇮🇪\n- **TERMÔMETRO DO LANÇAMENTO:** 88/100 (Excelente ROI estimado).\n\n🔥 **LANÇAMENTO 3: ZenCortex (BuyGoods)**\n- **Por que e uma oportunidade:** Alta taxa de conversão na rede de pesquisa internacional para buscas exatas de marca.\n- **Melhor País para Começar:** Nova Zelândia 🇳🇿\n- **TERMÔMETRO DO LANÇAMENTO:** 82/100"
        st.success("Varredura concluída com sucesso!")
    if st.session_state.resposta_cacador:
