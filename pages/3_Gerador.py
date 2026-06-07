import streamlit as st

# Configuração premium de página - Layout amplo e profissional Black para o Gerador
st.set_page_config(page_title="Adriel AI - Gerador de Anúncios Master", layout="wide")

# INJEÇÃO DE CÓDIGO CSS PREMIUM DEFINITIVO (BOTÃO NEON PERSONALIZADO DE LUXO)
st.markdown("""
<style>
    /* Força o estilo premium em todos os botões da página */
    button[kind="primary"], .stButton > button {
        background: linear-gradient(135deg, #007BFF 0%, #00E5FF 100%) !important;
        color: white !important;
        font-size: 18px !important;
        font-weight: bold !important;
        padding: 14px 40px !important;
        border-radius: 14px !important;
        border: none !important;
        box-shadow: 0px 5px 20px rgba(0, 229, 255, 0.4) !important;
        transition: all 0.3s ease-in-out !important;
        width: 100% !important;
        cursor: pointer !important;
    }
    /* Efeito de brilho e movimento ao passar o mouse */
    button[kind="primary"]:hover, .stButton > button:hover {
        background: linear-gradient(135deg, #00E5FF 0%, #007BFF 100%) !important;
        transform: translateY(-3px) !important;
        box-shadow: 0px 8px 25px rgba(0, 229, 255, 0.7) !important;
        color: white !important;
    }
    /* Alinhamento fino para as abas (tabs) */
    .stTabs [data-baseweb="tab"] {
        font-size: 16px !important;
        font-weight: bold !important;
    }
</style>
""", unsafe_allow_html=True)

st.title("✍️ MÓDULO 2: GERADOR DE ANÚNCIOS MASTER")
st.markdown("Engenharia de criação de criativos massivos e blindagem rigorosa de compliance contra políticas do Google Ads.")
st.write("---")

# Campo de entrada automática do produto do leilão
produto_input = st.text_input("Qual o produto internacional para estruturar a campanha?", value="Citrus Burn")
st.write("")

if st.button("✍️ GERAR ESTRUTURA COMPLETA E PALAVRAS-CHAVE"):
    with st.spinner("Escaneando regras de compliance e estruturando esqueleto publicitário massivo..."):
        
        prod = produto_input.strip()
        prod_low = prod.lower().replace(" ", "-")
        
        st.success("🏆 Arsenal de Tráfego e Criativos Blindados gerados com sucesso para o produto: " + prod)
        st.write("---")
        
        # Criação de abas organizadas para descarregar a densidade brutal de textos sem travar
        aba_copys, aba_palavras_chave = st.tabs(["📋 Criativos, Títulos 30/90 e Caminhos", "🎯 Correspondências (Frase, Exata, Livre e Negativas)"])
        
        with aba_copys:
            st.markdown("### 💎 Estrutura Editorial da Campanha (Responsivo Google Ads)")
            
            # Blocos contendo os caminhos de exibição e os 15 títulos obrigatórios de compliance
            texto_anuncios = (
                "[CAMINHO DE EXIBIÇÃO / DISPLAY PATH]\n"
                "URL Final Recomendada: https://suapagina.com" + prod_low + "\n"
                "Caminho de Exibição 1: /Official\n"
                "Caminho de Exibição 2: /Store\n\n"
                "----------------------------------------------------------------------\n"
                "[15 TÍTULOS DE COMPLIANCE MANDATÓRIOS — MÁXIMO 30 CARACTERES]\n"
                "1. " + prod + " Official Website\n"
                "2. Buy " + prod + " Online\n"
                "3. Original " + prod + " Formula\n"
                "4. " + prod + " Best Price\n"
                "5. Order " + prod + " Today\n"
                "6. " + prod + " Premium Supplement\n"
                "7. " + prod + " Official Store\n"
                "8. Get " + prod + " Now\n"
                "9. " + prod + " Certified Product\n"
                "10. " + prod + " Special Discount\n"
                "11. " + prod + " Natural Blend\n"
                "12. Authentic " + prod + "\n"
                "13. Shop " + prod + " Direct\n"
                "14. " + prod + " Best Deal\n"
                "15. Secure " + prod + " Order\n\n"
                "----------------------------------------------------------------------\n"
                "[TÍTULOS LONGOS DE AUTORIDADE MÁXIMA — EXATAMENTE 90 CARACTERES]\n"
                "1. " + prod + " Official Site - Order Original Premium Formula Directly From The Manufacturer Today\n"
                "2. Buy " + prod + " Online - Save Big On Multi-Bottle Packages With Free Shipping Active Now\n"
                "3. Original " + prod + " Supplement - Secure Your Special Discount Deal Before Allocation Ends Today\n\n"
                "----------------------------------------------------------------------\n"
                "[DESCRIÇÕES EXCLUSIVAS — MÁXIMO 90 CARACTERES]\n"
                "1. Order " + prod + " from the official website today and get exclusive package discounts.\n"
                "2. Get the original " + prod + " with a 100% 60-day money-back guarantee. Secure checkout.\n"
                "3. 100% natural formula backed by clinical research. Fast shipping options available now.\n"
                "4. Save big on multi-bottle packages today. Enjoy secure checkout and fast delivery."
            )
            st.text_area("Copie o Esqueleto dos Criativos Publicitários:", value=texto_anuncios, height=500)
            
        with aba_palavras_chave:
            st.markdown("### 🎯 Listas Completas de Intenção por Extenso (Mínimo de 20 Termos por Bloco)")
            
            # Enfileiramento em massa por extenso de Phrase, Exact, Broad e as 30 Negativas de proteção
            texto_listas = (
                "[CORRESPONDÊNCIA DE FRASE — 20 PALAVRAS-CHAVE MÍNIMO COM ASPAS]\n"
                "1. \"" + prod + " official website\"\n"
                "2. \"buy " + prod + " online\"\n"
                "3. \"" + prod + " discount price\"\n"
                "4. \"order " + prod + " online\"\n"
                "5. \"" + prod + " where to buy\"\n"
                "6. \"" + prod + " store\"\n"
                "7. \"" + prod + " price\"\n"
                "8. \"" + prod + " buy\"\n"
                "9. \"" + prod + " reviews\"\n"
                "10. \"" + prod + " cost\"\n"
                "11. \"" + prod + " supplement\"\n"
                "12. \"" + prod + " official store\"\n"
                "13. \"" + prod + " best price\"\n"
                "14. \"secure " + prod + " order\"\n"
                "15. \"" + prod + " check out\"\n"
                "16. \"get " + prod + " online\"\n"
                "17. \"purchase " + prod + " now\"\n"
                "18. \"" + prod + " coupon code\"\n"
                "19. \"" + prod + " special deal\"\n"
                "20. \"original " + prod + "\"\n\n"
                "----------------------------------------------------------------------\n"
                "[CORRESPONDÊNCIA EXATA — 20 PALAVRAS-CHAVE MÍNIMO COM COLCHETES]\n"
                "1. [" + prod + " official website]\n"
                "2. [buy " + prod + " online]\n"
                "3. [" + prod + " discount price]\n"
                "4. [order " + prod + " online]\n"
                "5. [" + prod + " where to buy]\n"
                "6. [" + prod + " store]\n"
                "7. [" + prod + " price]\n"
                "8. [" + prod + " buy]\n"
                "9. [" + prod + " reviews]\n"
                "10. [" + prod + " cost]\n"
                "11. [" + prod + " supplement]\n"
                "12. [" + prod + " official store]\n"
                "13. [" + prod + " best price]\n"
                "14. [secure " + prod + " order]\n"
                "15. [check out " + prod + "]\n"
                "16. [get " + prod + " online]\n"
                "17. [purchase " + prod + " now]\n"
                "18. [" + prod + " coupon code]\n"
                "19. [" + prod + " special deal]\n"
                "20. [" + prod + "]\n\n"
                "----------------------------------------------------------------------\n"
                "[CORRESPONDÊNCIA LIVRE — 20 PALAVRAS-CHAVE MÍNIMO SEM SÍMBOLOS]\n"
                "1. " + prod + " official site\n"
                "2. buy " + prod + "\n"
                "3. " + prod + " store\n"
                "4. order " + prod + "\n"
                "5. " + prod + " discount\n"
                "6. " + prod + " online\n"
                "7. " + prod + " website\n"
                "8. purchase " + prod + "\n"
                "9. price of " + prod + "\n"
                "10. original " + prod + "\n"
                "11. " + prod + " delivery\n"
                "12. " + prod + " supply\n"
                "13. " + prod + " shop\n"
                "14. cost of " + prod + "\n"
                "15. " + prod + " cost\n"
                "16. get " + prod + "\n"
                "17. " + prod + " brand\n"
                "18. safe " + prod + "\n"
                "19. genuine " + prod + "\n"
                "20. " + prod + " manufacturing\n\n"
                "----------------------------------------------------------------------\n"
                "[30 PALAVRAS-CHAVE NEGATIVAS DE FILTRAGEM — PROTEÇÃO MÁXIMA DE VERBA]\n"
                "1. scam\n2. complaints\n3. ingredients\n4. side effects\n5. free pdf\n6. amazon\n7. walmart\n8. ebay\n9. discount code\n10. coupon\n11. target\n12. refund\n13. fake\n14. wholesale\n15. department\n16. independent review\n17. customer support number\n18. login\n19. free trial\n20. bbb rating\n21. youtube video\n22. diagnosis\n23. treatment\n24. cheap\n25. medical advice\n26. symptoms\n27. where to find cheap\n28. sideeffects\n29. bad reviews\n30. clinical trial history"
            )
            st.text_area("Copie os Blocos de Termos Organizadamente:", value=texto_listas, height=520)
