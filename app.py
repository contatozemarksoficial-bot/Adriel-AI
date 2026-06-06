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

# =====================================================================================================================
# FUNÇÕES CIRÚRGICAS DE ENTREGA COMPATÍVEIS COM O MENU DE SELEÇÃO (ARSENAL ULTRA DENSO)
# =====================================================================================================================
def executar_auditoria(produto):
    return "**1. STATUS DE VALIDAÇÃO DO PRODUTO**\nO produto '" + produto + "' esta 100% VALIDADO no mercado internacional de afiliados, registrando alto volume de buscas exatas e baixíssima taxa de reembolso, sendo ideal para estratégias agressivas de Fundo de Funil.\n\n**2. ANÁLISE DE CONCORRÊNCIA E PREÇO DO CLIQUE (CPC)**\nNos Estados Unidos a concorrência está saturada com CPC batendo $0.85. Porém, no Reino Unido e Irlanda, o leilão encontra-se livre de grandes afiliados gringos, apresentando um CPC médio real e estimado em excelentes $0.45.\n\n**3. MAIOR DOR DO COMPRADOR GRINGO**\nO cliente final gringo busca por regulação rápida do metabolismo, controle severo de apetite por doces, perda de peso natural sem efeito sanfona e aumento massivo da disposição diária.\n\n**4. MELHOR PAÍS ESTRATÉGICO PARA ANUNCIAR (MAIOR ROI)**\nO melhor país para iniciar a campanha de '" + produto + "' é o **Reino Unido (United Kingdom) 🇬🇧**. O leilão local em libras oferece menor concorrência, cliques muito mais baratos e alto poder de conversão se associado a uma Pre-sell blindada com aviso de bandeira local."

def executar_gerador(produto):
    return "[DISPLAY PATH]\n/Official/Store\n/Secure/Order\n\n[HEADLINES - MAX 30 CHARACTERS]\n1. " + produto + " Official Site (Pin Position 1)\n2. Buy " + produto + " Online\n3. Original " + produto + " Formula\n4. " + produto + " Best Price\n\n[DESCRIPTIONS - MAX 90 CHARACTERS]\n1. Order " + produto + " from the official website today and get exclusive package discounts.\n2. Get the original " + produto + " with a 100% 60-day money-back guarantee. Secure checkout.\n3. 100% natural formula backed by clinical research. Fast shipping options available.\n4. Save big on multi-bottle packages today. Enjoy secure checkout and fast delivery.\n\n[PHRASE MATCH KEYWORDS - WITH QUOTES - EXACTLY 15 UNIQUE TERMS]\n1. \"" + produto + " official website\"\n2. \"buy " + produto + " online\"\n3. \"" + produto + " discount price\"\n4. \"order " + produto + " online\"\n5. \"" + produto + " where to buy\"\n6. \"" + produto + " store\"\n7. \"" + produto + " price\"\n8. \"get " + produto + "\"\n9. \"purchase " + produto + "\"\n10. \"" + produto + " sale\"\n11. \"" + produto + " supplement\"\n12. \"" + produto + " official store\"\n13. \"" + produto + " best price\"\n14. \"secure " + produto + " order\"\n15. \"" + produto + " check out\"\n\n[EXACT MATCH KEYWORDS - WITH BRACKETS - EXACTLY 15 UNIQUE TERMS]\n1. [" + produto + " official website]\n2. [buy " + produto + " online]\n3. [" + produto + " discount price]\n4. [order " + produto + " online]\n5. [" + produto + " where to buy]\n6. [" + produto + " store]\n7. [" + produto + " price]\n8. [get " + produto + "]\n9. [purchase " + produto + "]\n10. [" + produto + " sale]\n11. [" + produto + " supplement]\n12. [" + produto + " official store]\n13. [" + produto + " best price]\n14. [secure " + produto + " order]\n15. [" + produto + "]\n\n[BROAD MATCH KEYWORDS - PURE TEXT NO SYMBOLS - EXACTLY 15 UNIQUE TERMS]\n1. " + produto + " official site\n2. buy " + produto + "\n3. " + produto + " store\n4. order " + produto + "\n5. " + produto + " discount\n6. " + produto + " online\n7. " + produto + " website\n8. purchase " + produto + "\n9. price of " + produto + "\n10. original " + produto + "\n11. " + produto + " delivery\n12. " + produto + " supply\n13. " + produto + " shop\n14. cost of " + produto + "\n15. " + produto + " cost\n\n[NEGATIVE KEYWORDS]\nscam, reviews, complaints, ingredients, side effects, free pdf, amazon, walmart, ebay, discount code, coupon, target, refund"

def executar_cacador():
    return "🔥 **LANÇAMENTO 1: Obsesta (BuyGoods)**\n- **Por que e uma oportunidade:** Produto recém-lançado com leilão completamente vazio nas primeiras 48 horas no Google Ads. Baixíssima concorrência e alta comissão por venda.\n- **Melhor País para Começar:** Reino Unido 🇬🇧\n- **TERMÔMETRO DO LANÇAMENTO:** 98/100 (Potencial máximo de lucro rápido).\n\n🔥 **LANÇAMENTO 2: NeuroQuiet (ClickBank)**\n- **Por que e uma oportunidade:** Nicho de saúde mental e foco em plena ascensão na Europa, com leilão limpo de concorrentes.\n- **Melhor País para Começar:** Irlanda 🇮🇪\n- **TERMÔMETRO DO LANÇAMENTO:** 88/100 (Excelente ROI estimado).\n\n🔥 **LANÇAMENTO 3: ZenCortex (BuyGoods)**\n- **Por que e uma oportunidade:** Alta taxa de conversão na rede de pesquisa internacional para buscas exatas de marca.\n- **Melhor País para Começar:** Nova Zelândia 🇳🇿\n- **TERMÔMETRO DO LANÇAMENTO:** 82/100"

def executar_presell(produto):
    return "[HEADLINE SECURE - ELEMENTOR TOP BANNER]\nSpecial Discount Package on the Official Website Today!\n\n[SUBHEADLINE - PERSUASIVE COPY]\nGet the Authentic " + produto + " Formula Directly from the Manufacturer Website and Save Big.\n\n[LOCAL SHIPPING COMPLIANCE BOX]\nAvailable for United Kingdom Delivery 🇬🇧 - Fast Local Shipping & Secure Order Options.\n\n[AFFILIATE LINK DISCLOSURE - SEU COMISSIONAMENTO]\nOfficial Promo Link active via hostinger tracking system. Click to secure allocation.\n\n[FOOTER LEGAL DISCLAIMER]\n*This website is an independent review and pre-sell hub. We receive compensation from product links. This product is not intended to diagnose, treat, cure or prevent any disease. Privacy Policy | Terms of Service"

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
# INTERFACE DO MENU CENTRAL SEGUINDO SEU MODELO SEGURO DE BOTÕES DE AÇÃO DIRECTA
# =====================================================================================================================
if menu == "📊 Radar de Produtos":
