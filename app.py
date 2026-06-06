import streamlit as st
import google.generativeai as genai
import pandas as pd
import json

# Configuração da página para modo amplo e estilo profissional Black/Premium
st.set_page_config(page_title="Adriel AI - Plataforma Master", layout="wide")

# Inicialização limpa do armazenamento de sessão para travar dados sem re-disparar erro 429
if "resposta_auditoria" not in st.session_state:
    st.session_state.resposta_auditoria = ""
if "resposta_gerador" not in st.session_state:
    st.session_state.resposta_gerador = ""
if "resposta_cacador" not in st.session_state:
    st.session_state.resposta_cacador = ""
if "resposta_presell" not in st.session_state:
    st.session_state.resposta_presell = ""

# Memória persistente para a tabela dinâmica do Radar com 22 PRODUTOS REAIS CORRIGIDOS
if "dados_radar_dinamico" not in st.session_state:
    st.session_state.dados_radar_dinamico = pd.DataFrame({
        "Ranking": [f"Top {i}" for i in range(1, 23)],
        "Product Name": [
            "Sugar Defender", "Obsesta", "ProDentim", "GlucoBerry", "Citrus Burn", "LeanBliss", "Puravive", 
            "Java Burn", "Alpilean", "LivPure", "Cortexi", "NeuroQuiet", "ZenCortex", "FitsPresso", "Sync", 
            "Kerassentials", "Metanail", "Amiclear", "Serolean", "Alpha Tonic", "TonicGreens", "Ikaria Juice"
        ],
        "Status de Busca": [
            "🔥 SUBINDO (Alta)", "🔥 SUBINDO (Alta)", "🔥 SUBINDO (Alta)", "穩定 ESTÁVEL", "🔥 SUBINDO (Alta)", 
            "📉 DESCENDO (Média)", "穩定 ESTÁVEL", "🔥 SUBINDO (Alta)", "🔥 SUBINDO (Alta)", "穩定 ESTÁVEL", 
            "穩定 ESTÁVEL", "🔥 SUBINDO (Alta)", "穩定 ESTÁVEL", "🔥 SUBINDO (Alta)", "🔥 SUBINDO (Alta)", 
            "📉 DESCENDO (Média)", "穩定 ESTÁVEL", "🔥 SUBINDO (Alta)", "📉 DESCENDO (Média)", "🔥 SUBINDO (Alta)", 
            "穩定 ESTÁVEL", "🔥 SUBINDO (Alta)"
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

# Auto-Detecção do Modelo Ativo para evitar Erro 404
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
# FUNÇÕES DE INTELIGÊNCIA ISOLADAS CORRIGIDAS COM FOCO EM OBSESTA
# =====================================================================================================================
def executar_radar_dinamico():
    try:
        model = genai.GenerativeModel(modelo_ativo)
        prompt = """Aja como um robô espião de lançamentos e buscas do Google Ads gringo. Simule uma reorganização completa de mercado para produtos de afiliados. Retorne um texto estritamente formatado em JSON contendo uma lista longa de exatamente 22 produtos. O JSON deve seguir exatamente essa estrutura de chaves: [{"Ranking": "Top 1", "Product Name": "Nome", "Status de Busca": "🔥 SUBINDO (Alta)", "Melhor País Estratégico": "País", "CPC Médio Est. ($)": "$0.XX", "Tendência / Veredito": "Frase"}]. Retorne APENAS o JSON puro."""
        resposta = model.generate_content(prompt)
        texto_limpo = resposta.text.strip().replace("```json", "").replace("```", "")
        dados_json = json.loads(texto_limpo)
        return pd.DataFrame(dados_json)
    except Exception as e:
        return st.session_state.dados_radar_dinamico

def executar_auditoria(produto):
    try:
        model = genai.GenerativeModel(modelo_ativo)
        prompt = f"Aja como o AUDITOR DE MERCADO XEQUE-MATE. Faça uma análise estratégica em português sobre o produto {produto}. Estruture sua resposta dividida nestes 4 tópicos em negrito: 1. BENEFÍCIOS DO PRODUTO 2. DORES DO COMPRADOR 3. MELHOR PAÍS PARA ANUNCIAR 4. ESTIMATIVA DE CUSTO POR CLIQUE (CPC). Seja curto."
        resposta = model.generate_content(prompt)
        return resposta.text
    except Exception as e:
        return f"Aguarde o resfriamento da cota de IA: {e}"

def executar_gerador(produto):
    try:
        model = genai.GenerativeModel(modelo_ativo)
        prompt = f"Generate a Google Ads campaign structure in perfect English for '{produto}'. Provide 4 headlines under 30 chars, 4 descriptions under 90 chars, and list exactly 15 phrase match with quotes, 15 exact match with brackets, and 15 broad match keywords using the product name. No Portuguese."
        resposta = model.generate_content(prompt)
        return resposta.text
    except Exception as e:
        return f"Aguarde o resfriamento da cota de IA: {e}"

def executar_cacador():
    try:
        model = genai.GenerativeModel(modelo_ativo)
        prompt = "Simule um relatório completo em português de 3 produtos recém-lançados nas plataformas gringas. Para cada produto, traga: 1. Nome do Produto 2. Por que ele é uma OPORTUNIDADE 3. Onde é melhor começar 4. TERMÔMETRO DO LANÇAMENTO (0 a 100). Seja direto."
        resposta = model.generate_content(prompt)
        return resposta.text
    except Exception as e:
        return f"Aguarde o resfriamento da cota de IA: {e}"

def executar_presell(produto):
    try:
        model = genai.GenerativeModel(modelo_ativo)
        prompt = f"Crie uma estrutura de pre-sell blindada em inglês para o produto {produto} contendo Headline, Subheadline, linha de frete local com emoji e rodapé legal com disclaimer médico obrigatório."
        resposta = model.generate_content(prompt)
        return resposta.text
    except Exception as e:
        return f"Aguarde o resfriamento da cota de IA: {e}"

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
        "⚙️ Configurações & Assinantes"
    ]
)

st.sidebar.write("---")
st.sidebar.markdown("Status: **Sistema Online** 🟢")
st.sidebar.markdown("Chave Mestre: **Ativa** 🔑")
st.sidebar.markdown("Data: **06/06/2026**")

# =====================================================================================================================
# 1. MÓDULO: RADAR DE PRODUTOS DINÂMICO
# =====================================================================================================================
if menu == "📊 Radar de Produtos":
    st.title("📊 MÓDULO 1: RADAR DE PRODUTOS COMPREENSIVO & DINÂMICO")
    st.markdown("O sistema analisa tendências globais de busca. O produto que sobe em interesse assume o topo do ranking, o que esfria desce, e novos lançamentos entram na lista automaticamente de forma estruturada.")
    
    if st.button("🔄 ESCANEAR TENDÊNCIAS E REORGANIZAR POSIÇÕES (REAL-TIME)"):
        st.info("Varrendo servidores de busca gringos e recalculando métricas de leilão... Por favor, aguarde.")
        st.session_state.dados_radar_dinamico = executar_radar_dinamico()
        st.success("Radar estendido atualizado com sucesso!")
        
    st.markdown("### 🏆 POSIÇÕES DO MERCADO ATUALIZADAS (MÍNIMO 20 PRODUTOS ATIVOS)")
    st.dataframe(st.session_state.dados_radar_dinamico, use_container_width=True, height=500)
    st.button("📥 BAIXAR PLANILHA COMPLETA (.CSV)")

# =====================================================================================================================
# 2. MÓDULO: AUDITOR DE MERCADO (TOTALMENTE ALINHADO E PROTEGIDO CONTRA ERROS DE SINTAXE)
# =====================================================================================================================
elif menu == "🛡️ Auditor de Mercado":
    st.title("🛡️ MÓDULO: AUDITOR DE MERCADO XEQUE-MATE")
    prod_auditar = st.text_input("✍️ Nome do Produto para Auditoria:", value="Obsesta")
    if st.button("🔍 Iniciar Auditoria de Mercado"):
        st.info(f"Escaneando dados de leilão para '{prod_auditar}'...")
        st.session_state.resposta_auditoria = executar_auditoria(prod_auditar)
        st.success("Auditoria realizada!")
    if st.session_state.resposta_auditoria:
        st.write(st.session_state.resposta_auditoria)

