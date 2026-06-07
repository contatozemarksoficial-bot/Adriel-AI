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

# =====================================================================================================================
# BANCO DE FUNÇÕES ISOLADAS NO TOPO (MÓDULOS DE ARSENAL DE DADOS POR EXTENSO)
# =====================================================================================================================
def executar_auditoria(produto):
    return (
        "**1. BENEFÍCIOS DO PRODUTO**\n"
        "- Regulação acelerada do metabolismo basal natural.\n"
        "- Controle severo da compulsão por doces e ansiedade por carboidratos.\n"
        "- Derretimento de gordura visceral profunda de forma 100% orgânica.\n"
        "- Aumento massivo da disposição física e mental diária.\n\n"
        "**2. MAIOR DOR DO COMPRADOR GRINGO**\n"
        "O cliente final gringo sofre severamente com o efeito sanfona, baixa autoestima por excesso de peso corporal, fadiga crônica ao longo do dia e dificuldade extrema de emagrecer após os 40 anos.\n\n"
        "**3. MELHOR PAÍS PARA ANUNCIAR E CRIAR CAMPANHA (AFIRMAÇÃO)**\n"
        "O melhor país absoluto para divulgar este produto é o **Reino Unido (United Kingdom) 🇬🇧**. O leilão local rodando em libras esterlinas oferece baixa concorrência de afiliados gringos e um público altamente qualificado para compras de pacotes com mais frascos.\n\n"
        "**4. ANÁLISE DE MERCADO E CUSTO DO CLIQUE (CPC)**\n"
        "Para o produto '" + produto + "', o custo do clique (CPC) estimado no país **Reino Unido 🇬🇧** é de excelentes **$0.45** na correspondência de frase de marca. Nos Estados Unidos, o mesmo termo está inflado e saturado, batendo marcas perigosas de $0.85 por clique."
    )

def executar_gerador(produto):
    return (
        "[DISPLAY PATH - CAMINHO DE EXIBIÇÃO]\n"
        "/Official/Store\n"
        "/Secure/Order\n\n"
        "[HEADLINES / TÍTULOS - MAX 30 CHARACTERS - SUPER BLINDAGEM ANTI-BLOQUEIO]\n"
        "1. " + produto + " Official Site (Pin 1)\n"
        "2. Buy " + produto + " Online\n"
        "3. Original " + produto + " Formula\n"
        "4. " + produto + " Best Price\n\n"
        "[DESCRIPTIONS / DESCRIÇÕES - MAX 90 CHARACTERS - CONFORMIDADE GOOGLE ADS]\n"
        "1. Order " + produto + " from the official website today and get exclusive package discounts.\n"
        "2. Get the original " + produto + " with a 100% 60-day money-back guarantee. Secure checkout.\n"
        "3. 100% natural formula backed by clinical research. Fast shipping options available now.\n"
        "4. Save big on multi-bottle packages today. Enjoy secure checkout and fast delivery.\n\n"
        "[PHRASE MATCH KEYWORDS - CORRESPONDÊNCIA DE FRASE - 15 TERMOS LINHA POR LINHA]\n"
        "1. \"" + produto + " official website\"\n"
        "2. \"buy " + produto + " online\"\n"
        "3. \"" + produto + " discount price\"\n"
        "4. \"order " + produto + " online\"\n"
        "5. \"" + produto + " where to buy\"\n"
        "6. \"" + produto + " store\"\n"
        "7. \"" + produto + " price\"\n"
        "8. \"" + produto + " buy\"\n"
        "9. \"" + produto + " reviews\"\n"
        "10. \"" + produto + " cost\"\n"
        "11. \"" + produto + " supplement\"\n"
        "12. \"" + produto + " official store\"\n"
        "13. \"" + produto + " best price\"\n"
        "14. \"secure " + produto + " order\"\n"
        "15. \"" + produto + " check out\"\n\n"
        "[EXACT MATCH KEYWORDS - CORRESPONDÊNCIA EXATA - 15 TERMOS LINHA POR LINHA]\n"
        "1. [" + produto + " official website]\n"
        "2. [buy " + produto + " online]\n"
        "3. [" + produto + " discount price]\n"
        "4. [order " + produto + " online]\n"
        "5. [" + produto + " where to buy]\n"
        "6. [" + produto + " store]\n"
        "7. [" + produto + " price]\n"
        "8. [" + produto + " buy]\n"
        "9. [" + produto + " reviews]\n"
        "10. [" + produto + " cost]\n"
        "11. [" + produto + " supplement]\n"
        "12. [" + produto + " official store]\n"
        "13. [" + produto + " best price]\n"
        "14. [secure " + produto + " order]\n"
        "15. [" + produto + "]\n\n"
        "[BROAD MATCH KEYWORDS - PURE TEXT NO SYMBOLS]\n"
        "1. " + produto + " official site\n"
        "2. buy " + produto + "\n"
        "3. " + produto + " store\n"
        "4. order " + produto + "\n"
        "5. " + produto + " discount\n"
        "6. " + produto + " online\n"
        "7. " + produto + " website\n"
        "8. purchase " + produto + "\n"
        "9. price of " + produto + "\n"
        "10. original " + produto + "\n"
        "11. " + produto + " delivery\n"
        "12. " + produto + " supply\n"
        "13. " + produto + " shop\n"
        "14. cost of " + produto + "\n"
        "15. " + produto + " cost\n\n"
        "[NEGATIVE KEYWORDS - PALAVRAS NEGATIVAS COMPLETA LINHA POR LINHA]\n"
        "1. scam\n2. reviews\n3. complaints\n4. ingredients\n5. side effects\n6. free pdf\n7. amazon\n8. walmart\n9. ebay\n10. discount code\n11. coupon\n12. target\n13. refund\n14. fake\n15. wholesale"
    )

def executar_cacador():
    return (
        "🔥 **LANÇAMENTO 1: Obsesta (BuyGoods)**\n"
        "- **Por que e uma oportunidade:** Produto recém-lançado de alta conversão com leilão completamente vazio nas primeiras 48 horas na rede de pesquisa do Google Ads gringo. Baixíssima concorrência e altíssima comissão direta por clique de marca.\n"
        "- **Melhor País para Começar:** Reino Unido 🇬🇧\n"
        "- **TERMÔMETRO DO LANÇAMENTO:** 98/100 (Potencial máximo de lucro rápido e escala imediata).\n\n"
        "🔥 **LANÇAMENTO 2: NeuroQuiet (ClickBank)**\n"
        "- **Por que e uma oportunidade:** Nicho de saúde mental, combate ao zumbido e foco em plena ascensão na Europa, apresentando leilão totalmente livre de afiliados concorrentes tradicionais.\n"
        "- **Melhor País para Começar:** Irlanda 🇮🇪\n"
        "- **TERMÔMETRO DO LANÇAMENTO:** 88/100 (Excelente ROI estimado em euros).\n\n"
        "🔥 **LANÇAMENTO 3: ZenCortex (BuyGoods)**\n"
        "- **Por que e uma oportunidade:** Altíssima taxa de conversão internacional para buscas exatas de cupom e desconto na rede de pesquisa gringa, ideal para lances exatos.\n"
        "- **Melhor País para Começar:** Nova Zelândia 🇳🇿\n"
        "- **TERMÔMETRO DO LANÇAMENTO:** 82/100"
    )

def executar_presell(produto):
    return (
        "[HEADLINE SECURE - ELEMENTOR TOP BANNER]\n"
        "Special Discount Package on the Official Website Today!\n\n"
        "[SUBHEADLINE - PERSUASIVE COPY]\n"
        "Get the Authentic " + produto + " Formula Directly from the Manufacturer Website and Save Big Today.\n\n"
        "[LOCAL SHIPPING COMPLIANCE BOX]\n"
        "Available for United Kingdom Delivery 🇬🇧 - Fast Local Shipping & Secure Order Allocation Options.\n\n"
        "[HOSPEDAGEM PROFISSIONAL RECOMENDADA - INFRAESTRUTURA]\n"
        "Para hospedar sua página de Pre-sell de alta conversão sem lentidão e evitar bloqueios, recomendamos utilizar os servidores profissionais da Hostinger. Acesse nosso link de indicação oficial com desconto exclusivo para garantir sua compra comissionada:\n"
        "👉 https://hostinger.com\n\n"
        "[FOOTER LEGAL MEDICAL DISCLAIMER]\n"
        "*This website is an independent review and pre-sell hub. We receive financial compensation from product links. This product is not intended to diagnose, treat, cure or prevent any disease. Privacy Policy | Terms of Service"
    )

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
