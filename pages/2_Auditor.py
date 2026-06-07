import streamlit as st

# Configuração premium de página - Layout amplo e profissional Black para a Pre-sell
st.set_page_config(page_title="Adriel AI - Fabricante de Pre-sell", layout="wide")

# INJEÇÃO DE CÓDIGO CSS PREMIUM DEFINITIVO (PARA BOTÃO NEON REAL)
st.markdown("""
<style>
    button[kind="primary"], .stButton > button {
        background: linear-gradient(135deg, #007BFF 0%, #00E5FF 100%) !important;
        color: white !important;
        font-size: 18px !important;
        font-weight: bold !important;
        padding: 12px 35px !important;
        border-radius: 12px !important;
        border: none !important;
        box-shadow: 0px 4px 15px rgba(0, 229, 255, 0.4) !important;
        transition: all 0.3s ease-in-out !important;
        width: 100% !important;
    }
    button[kind="primary"]:hover, .stButton > button:hover {
        background: linear-gradient(135deg, #00E5FF 0%, #007BFF 100%) !important;
        transform: translateY(-2px) !important;
        box-shadow: 0px 6px 20px rgba(0, 229, 255, 0.6) !important;
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

st.title("🌐 MÓDULO: FABRICANTE DE PRE-SELL BLINDADA")
st.markdown("Estruturação automatizada de páginas de destino (Páginas Ponte) focadas em alta conversão e conformidade com o Google Ads.")
st.write("---")

# Campos de entrada de dados para moldar a Pre-sell
produto = st.text_input("Digite o nome do produto gringo para a Pre-sell:", value="Citrus Burn")
st.write("")

if st.button("🌐 GERAR ESTRUTURA DE PRÉ-VENDA COMPLETA"):
    with st.spinner("Compilando blocos de copy e gerando links de infraestrutura..."):
        st.success("Estrutura e textos prontos para o Elementor do produto: " + produto)
        st.write("---")
        
        # Módulos informativos e link de indicação direta no topo do relatório
        st.markdown("### 🛠️ 1. INFRAESTRUTURA DE HOSPEDAGEM PROFISSIONAL (OBRIGATÓRIO)")
        st.markdown(
            "Para rodar suas páginas ponte internacionais com velocidade recorde e evitar bloqueios de leilão, "
            "é fundamental utilizar servidores de alta performance. Clique no link oficial abaixo para garantir "
            "sua hospedagem profissional com desconto exclusivo da nossa plataforma:"
        )
        
        # O seu link oficial comissionado destacado em um botão nativo clicável
        st.markdown(
            '<a href="https://hostinger.com" target="_blank" style="text-decoration: none;">'
            '<div style="background-color: #2ECC71; color: white; text-align: center; padding: 12px; font-weight: bold; border-radius: 8px; box-shadow: 0px 4px 10px rgba(46, 204, 113, 0.3);">'
            "👉 CLIQUE AQUI PARA ADQUIRIR SUA HOSPEDAGEM HOSTINGER COM DESCONTO EXCLUSIVO"
            "</div>"
            "</a>", 
            unsafe_allow_html=True
        )
        st.write("")
        st.write("---")
        
        st.markdown("### 📐 2. ARQUITETURA DE TEXTOS E COPY PARA O ELEMENTOR")
        st.markdown("Copie as seções abaixo por extenso e cole dentro dos blocos de texto correspondentes do seu Elementor:")
        
        # Estrutura textual densa por extenso com as variáveis limpas do produto
        prod_nome = produto.strip()
        texto_presell = (
            "[BLOCO 1 — TOP BANNER DE CONFORMIDADE — ELEMENTOR SEÇÃO SUPERIOR]\n"
            "Texto: Special Discount Active on the Official Website Today!\n"
            "Ação: Use fundo cinza escuro ou preto com letras brancas pequenas para passar autoridade limpa.\n\n"
            "[BLOCO 2 — HEADLINE SECURE — PERSUASIVE COPY]\n"
            "Texto Principal: Get the Authentic " + prod_nome + " Formula Directly from the Manufacturer Website and Save Big Today.\n"
            "Sub-texto: 100% original product backed by a 60-day money-back guarantee. Secure check-out infrastructure enabled.\n\n"
            "[BLOCO 3 — LOCAL SHIPPING COMPLIANCE BOX — CAIXA DE BANDEIRA LOCAL]\n"
            "Texto: Available for United Kingdom Delivery 🇬🇧 — Fast Local Shipping & Secure Order Allocation Options Active.\n"
            "Dica: Altere a bandeira e o país de acordo com a geolocalização vencedora que você localizou no Radar ou no Auditor.\n\n"
            "[BLOCO 4 — BOTÃO DE CHAMADA PARA AÇÃO (CTA) — SEU LINK DE AFILIADO]\n"
            "Texto do Botão: CLAIM YOUR EXCLUSIVE OFFICIAL DISCOUNT PACKAGE NOW\n"
            "Destino: Cole o seu link de afiliado direto da ClickBank ou BuyGoods que redireciona para a página oficial do produtor.\n\n"
            "[BLOCO 5 — FOOTER LEGAL & DISCLAIMERS — RODAPÉ COMPREENSIVO ANTI-BLOQUEIO]\n"
            "Texto de Proteção: *This website is an independent review and pre-sell hub. We receive financial compensation from product links. This product is not intended to diagnose, treat, cure or prevent any disease. Privacy Policy | Terms of Service | Contact Us"
        )
        
        st.text_area("Estrutura Pronta da Pre-sell (Copie abaixo):", value=texto_presell, height=450)
