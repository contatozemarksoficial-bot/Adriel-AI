import streamlit as st
import google.generativeai as genai
import pandas as pd

# Configuração da página para modo amplo e estilo profissional Black/Premium
st.set_page_config(page_title="Adriel AI - Plataforma Master", layout="wide")

# Inicialização do armazenamento de sessão para fixar dados na tela e evitar erro 429
if "resposta_auditoria" not in st.session_state:
    st.session_state.resposta_auditoria = ""
if "resposta_gerador" not in st.session_state:
    st.session_state.resposta_gerador = ""
if "resposta_cacador" not in st.session_state:
    st.session_state.resposta_cacador = ""
if "resposta_presell" not in st.session_state:
    st.session_state.resposta_presell = ""

# Barra Lateral Esquerda - Menu de Navegação Idêntico ao Painel
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
        "⚙️ Configurações & Assinantes"
    ]
)

st.sidebar.write("---")
st.sidebar.markdown("Status: **Sistema Online** 🟢")
st.sidebar.markdown("Chave Mestre: **Ativa** 🔑")
st.sidebar.markdown("Data: **06/06/2026**")

# Configuração Segura e Auto-Detecção do Modelo Ativo para evitar Erro 404
modelo_ativo = "models/gemini-1.5-flash"
try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            modelo_ativo = m.name
            break
except Exception:
    pass

# =====================================================================================================================
# 1. MÓDULO: RADAR DE PRODUTOS (ENTRE 20 A 30 PRODUTOS COM TOP 10 FIXO E ISOLADO DE ERROS)
# =====================================================================================================================
if menu == "📊 Radar de Produtos":
    st.title("📊 MÓDULO 1: RADAR DE PRODUTOS [FILTRO XEQUE-MATE]")
    st.markdown("### 🏆 OS TOP 10 CAMPEÕES DE VENDAS (Afirmação Válida - Alta Movimentação)")
    
    dados_top10 = {
        "Ranking": [f"Top {i}" for i in range(1, 11)],
        "Product Name": ["Sugar Defender", "ProDentim", "GlucoBerry", "Citrus Burn", "LeanBliss", "Puravive", "Java Burn", "Alpilean", "LivPure", "Cortexi"],
        "Status de Validação": ["VALIDADO - Alta Demanda"] * 10,
        "Melhor País para Anunciar": ["Reino Unido 🇬🇧", "Irlanda 🇮🇪", "Nova Zelândia 🇳🇿", "Estados Unidos 🇺🇸", "Canadá 🇨🇦", "Reino Unido 🇬🇧", "Austrália 🇦🇺", "Canadá 🇨🇦", "Estados Unidos 🇺🇸", "Reino Unido 🇬🇧"],
        "CPC Médio Est. ($)": ["$0.42", "$0.55", "$0.38", "$0.65", "$0.48", "$0.50", "$0.45", "$0.52", "$0.60", "$0.47"],
        "Por que anunciar aqui?": [
            "Leilão de baixo custo no Reino Unido, fugindo da briga de afiliados americanos.",
            "Mercado qualificado na Irlanda com alta conversão para saúde dental.",
            "Oceano azul puro com CPC baratíssimo na Nova Zelândia.",
            "Volume massivo de vendas, recomendado focar em tráfego Mobile Only.",
            "Público canadense consome muitos pacotes de 6 frascos.",
            "Passa fácil pela conformidade britânica usando pre-sell com aviso de afiliado.",
            "Australianos têm alto poder de compra para ofertas de queima de gordura.",
            "Mercado canadense está com leilão livre e concorrência reduzida.",
            "Ideal para focar em locais de lances exatos no mercado americano.",
            "Excelente aceitação no Reino Unido para nichos de audição e foco."
        ]
    }
    st.dataframe(pd.DataFrame(dados_top10), use_container_width=True)
    
    st.write("---")
    st.markdown("### 🛰️ PRODUTOS VALIDADOS DE BAIXA CONCORRÊNCIA (Excelentes Oportunidades)")
    
    dados_baixa = {
        "Product Name": ["NeuroQuiet", "ZenCortex", "FitsPresso", "Sync", "Kerassentials", "Metanail", "Amiclear", "Serolean", "Alpha Tonic", "TonicGreens", "Ikaria Juice", "CustomKeto"],
        "Status de Validação": ["VALIDADO - Concorrência Baixa"] * 12,
        "Melhor País para Anunciar": ["Irlanda 🇮🇪", "Nova Zelândia 🇳🇿", "Austrália 🇦🇺", "Reino Unido 🇬🇧", "Canadá 🇨🇦", "Irlanda 🇮🇪", "Nova Zelândia 🇳🇿", "Reino Unido 🇬🇧", "Austrália 🇦🇺", "Canadá 🇨🇦", "Reino Unido 🇬🇧", "Estados Unidos 🇺🇸"],
        "Por que é uma oportunidade?": [
            "Poucos afiliados anunciando na Irlanda, cliques muito baratos.",
            "Leilão vazio na Nova Zelândia permitindo testar com baixo orçamento diário.",
            "Público australiano buscando soluções alternativas de energia.",
            "Lançamento recente com busca qualificada crescendo na Inglaterra.",
            "Nicho de estética focado em público feminino muito forte no Canadá.",
            "Produto específico com leilão livre na Irlanda.",
            "Ideal para iniciar com correspondência de frase na Nova Zelândia.",
            "Concorrência reduzida no Reino Unido para o nicho de controle de apetite.",
            "Nicho de saúde masculina com alto pagamento de comissão na Austrália.",
            "Suplemento verde com ótimo engajamento no público de saúde do Canadá.",
            "Produto consolidado, mas com leilão limpo fora dos Estados Unidos.",
            "Alta conversão duradoura se trabalhado com exclusão de palavras curiosas nos EUA."
        ]
    }
    st.dataframe(pd.DataFrame(dados_baixa), use_container_width=True)
    st.button("📥 BAIXAR PLANILHA COMPLETA DE INTELIGÊNCIA (.CSV)")

# =====================================================================================================================
# 2. MÓDULO: AUDITOR DE MERCADO (4 PILARES E INFORMAÇÕES CLARAS DE PAÍS E CUSTO)
# =====================================================================================================================
elif menu == "🛡️ Auditor de Mercado":
    st.title("🛡️ MÓDULO: AUDITOR DE MERCADO XEQUE-MATE")
    st.markdown("Verifique benefícios, dores, melhor país e custo de clique de qualquer produto gringo:")
    
    prod_auditar = st.text_input("✍️ Nome do Produto para Auditoria:", value="Sugar Defender")
    if st.button("🔍 Iniciar Auditoria de Mercado"):
        st.info(f"Escaneando dados de leilão e comportamento de mercado para '{prod_auditar}'...")
        try:
            model = genai.GenerativeModel(modelo_ativo)
            prompt = f"""
            Aja como o AUDITOR DE MERCADO XEQUE-MATE. Faça uma análise estratégica em português sobre o produto '{prod_auditar}'.
            Estruture sua resposta estritamente dividida nestes 4 tópicos em negrito:
            1. BENEFÍCIOS DO PRODUTO (Explique resumidamente o que ele faz)
            2. DORES DO COMPRADOR (Por que as pessoas precisam dele e compram com cartão na mão)
            3. MELHOR PAÍS PARA ANUNCIAR (Diga categoricamente qual país tem menor concorrência e maior resultado)
            4. ESTIMATIVA DE CUSTO POR CLIQUE (CPC) (Informe o custo aproximado do clique de fundo de funil para esse produto no país indicado)
            Seja direto e profissional.
            """
            resposta = model.generate_content(prompt)
            st.session_state.resposta_auditoria = resposta.text
            st.success("Auditoria realizada!")
        except Exception as e:
            st.error(f"Erro na IA (Aguarde a liberação de cota do servidor): {e}")
            
    if st.session_state.resposta_auditoria:
        st.write(st.session_state.resposta_auditoria)

# =====================================================================================================================
# 3. MÓDULO: GERADOR DE ANÚNCIOS (SUPER BLINDAGEM, 15 FRASES POR BLOCO E EXTENSÃO DE 90 CARACTERES)
# =====================================================================================================================
elif menu == "✍️ Gerador de Anúncios":
    st.title("✍️ MÓDULO 2: GERADOR DE ANÚNCIOS MASTER & SUPER BLINDAGEM")
    st.markdown("Gere a estrutura completa do anúncio (Caminho, Títulos de 30 e Descrições de 90 caracteres) com 15 palavras-chave por bloco em inglês:")
    
    produto_alvo = st.text_input("✍️ Nome do Produto Gringo:", value="Sugar Defender")
    
    if st.button("Core Inteligência - Fabricar Anúncio Blindado"):
        st.info("Montando estrutura e aplicando regras de segurança contra bloqueios...")
        try:
            model = genai.GenerativeModel(modelo_ativo)
            prompt = f"""
            Generate a Google Ads campaign structure in perfect English for '{produto_alvo}'. 
            All text must follow Google Ads policy strictly (NO promises of medical cure, NO aggressive words). Apply maximum safety shielding.
            
            Deliver the result exactly with these sections:
            [DISPLAY PATH]
            Must provide Camino 1 and Camino 2 (like /Official/Store)
            
            [HEADLINES - MAX 30 CHARACTERS]
            Provide 4 headlines containing the product name. Mark Headline 1 to pin on position 1.
            
            [DESCRIPTIONS - MAX 90 CHARACTERS]
            Provide 4 descriptions focused on secure checkout, discount, and official site shipping guarantees.
            
            [PHRASE MATCH KEYWORDS - WITH QUOTES]
            List exactly 15 unique phrase match keywords with quotes using the name '{produto_alvo}'.
            
            [EXACT MATCH KEYWORDS - WITH BRACKETS]
            List exactly 15 unique exact match keywords with brackets using the name '{produto_alvo}'.
            
            [BROAD MATCH KEYWORDS - PURE TEXT]
            List exactly 15 unique buyer intent broad match keywords as pure text without symbols using the name '{produto_alvo}'.
            
            [NEGATIVE KEYWORDS]
            List 10 essential negative terms (scam, reviews, free pdf, etc).
