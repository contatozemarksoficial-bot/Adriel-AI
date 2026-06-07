import streamlit as st

# Configuração premium de página - Layout amplo e profissional Black para a Pre-sell
st.set_page_config(page_title="Adriel AI - Fabricante de Pre-sell Master", layout="wide")

# INJEÇÃO DE CÓDIGO CSS PREMIUM DEFINITIVO (BOTÕES NEON PERSONALIZADOS DE LUXO)
st.markdown("""
<style>
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
    button[kind="primary"]:hover, .stButton > button:hover {
        background: linear-gradient(135deg, #00E5FF 0%, #007BFF 100%) !important;
        transform: translateY(-2px) !important;
        box-shadow: 0px 8px 25px rgba(0, 229, 255, 0.7) !important;
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

st.title("🌐 MÓDULO: FABRICANTE DE PRE-SELL ANTIBLOQUEIO")
st.markdown("Estruturação automatizada de páginas ponte com super blindagem de rodapé legal exigida pelas políticas do Google Ads.")
st.write("---")

# Campos de entrada de dados para moldar a Pre-sell dinamicamente
produto = st.text_input("Qual o produto gringo para estruturar a Pre-sell?", value="Sugar Defender")
st.write("")

if st.button("🌐 GERAR ESTRUTURA BLINDADA PARA O ELEMENTOR"):
    with st.spinner("Compilando blocos de copy e injetando textos de conformidade legal do Google..."):
        
        prod_nome = produto.strip()
        prod_low = prod_nome.lower().replace(" ", "-")
        
        st.success("🎯 Pre-sell de Alta Conversão, Proteção Legal e Link de Parceria gerados para: " + prod_nome)
        st.write("---")
        
        # =============================================================================================================
        # SEU LINK DE INDICAÇÃO OFICIAL FIXADO E DESTACADO COM DADOS DE PLANOS REAIS NO TOPO
        # =============================================================================================================
        st.markdown("### 🛠️ 1. INFRAESTRUTURA DE HOSPEDAGEM DO AFILIADO (SUA INDICAÇÃO OFICIAL)")
        st.markdown(
            "Para que sua página ponte carregue de forma instantânea sem lentidão e evite reprovações de leilão, configure seu domínio "
            "na hospedagem profissional líder de mercado internacional. Garanta o desconto ativado de planos a partir de **R$ 5,99/mês (Single)**, "
            "**R$ 10,99/mês (Premium)** ou **R$ 13,99/mês (Business recomendado com NVMe rápido e CDN grátis)** clicando no nosso link oficial comissionado:"
        )
        
        st.markdown(
            '<a href="https://hostinger.com" target="_blank" style="text-decoration: none;">'
            '<div style="background-color: #2ECC71; color: white; text-align: center; padding: 15px; font-weight: bold; border-radius: 14px; box-shadow: 0px 5px 15px rgba(46, 204, 113, 0.4); font-size: 18px; transition: all 0.2s;">'
            "👉 CLIQUE AQUI PARA COMPRAR SUA HOSPEDAGEM HOSTINGER COM DESCONTO EXCLUSIVO (INDICAÇÃO ADRIEL AI)"
            '</div>'
            '</a>', 
            unsafe_allow_html=True
        )
        st.write("")
        st.write("---")
        
        # Estrutura de caixas expansíveis para separar o topo da blindagem do rodapé de forma clara
        st.markdown("### 📐 2. ARQUITETURA DE BLOCOS DO ELEMENTOR")
        
        with st.expander("🔝 SEÇÕES SUPERIORES E ESTRUTURA VISUAL (CÓPIA)", expanded=True):
            texto_topo = (
                "[BLOCO 1 — BANNER ANTES DA HEADLINE — SEÇÃO SUPREMA VERMELHA/PRETA]\n"
                "Texto: Discover The Natural Method To Support Metabolic Balance\n\n"
                "[BLOCO 2 — SUB-HEADLINE DE ALTA CONVERSÃO]\n"
                "Texto: Try the original 10-second morning ritual backed by clinical research. Claim up to 80% OFF today!\n"
                "Aviso de Afiliado Superior: Notice: This is an affiliate website. We may receive a small commission on sales made through the links on this page at no extra cost to you.\n\n"
                "[BLOCO 3 — BOTÃO DE CHAMADA PARA AÇÃO PRINCIPAL (CTA)]\n"
                "Texto do Botão: ➔ CLICK HERE TO VISIT THE OFFICIAL WEBSITE & ORDER NOW [*]\n"
                "Link de Destino: Seu link de afiliado direto da ClickBank/BuyGoods."
            )
            st.text_area("Criativos do Topo e Botão:", value=texto_topo, height=280)
            
        with st.expander("🛡️ RODAPÉ BLINDADO ANTI-BLOQUEIO (OBRIGATÓRIO COPIAR COMPLETO)", expanded=True):
            st.markdown(
                "**⚠️ ATENÇÃO EXTREMA:** Este bloco abaixo contém a linha mestre exata exigida pelo Google Ads juntando links e avisos de saúde. "
                "Cole tudo na caixa de texto do rodapé da sua página ponte para blindar a conta contra suspensões:"
            )
            
            # Injeção cirúrgica da linha exata solicitada com a variável dinâmica do produto
            texto_rodape = (
                "[RODAPÉ LEGAL COMPLETO — FONTE PEQUENA E FUNDO ESCURO]\n\n"
                "About " + prod_nome + ": • 100% Natural Formula with carefully selected ingredients. • Easy-to-take liquid dropper format for daily use. • Non-GMO, gluten-free, and manufactured in a secure facility.\n\n"
                "------------------------------------------------------------------------------------------------------\n"
                "FTC DISCLOSURE & AFFILIATE NOTICE:\n"
                "The links contained on this website page may result in a small financial compensation if you opt to purchase the product advised at no additional cost to you. This helps support our independent research team so we can continue to review high-quality premium products.\n\n"
                "------------------------------------------------------------------------------------------------------\n"
                "LINE-BLINDAGE MANDATORY GOOGLE ADS POLICY:\n"
                "Privacy Policy | Terms of Service | Disclaimer The content of this site is for informational purposes only and is not intended to replace professional medical advice, diagnosis, or treatment. " + prod_nome + " is a registered trademark of its respective owners.\n\n"
                "------------------------------------------------------------------------------------------------------\n"
                "[REQUISITO DE INFRAESTRUTURA INTEGRADO — ONDE HOSPEDAR]\n"
                "Hospedagem Recomendada para esta Pre-sell: Hostinger (https://hostinger.com)"
            )
            st.text_area("Massa Bruta do Rodapé de Proteção:", value=texto_rodape, height=380)
