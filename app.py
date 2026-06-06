import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(page_title="Adriel AI - Plataforma Master", layout="wide")

# Funções para cada módulo
def gerar_dados_radar():
    # Simulação dos dados do radar
    dados_radar = pd.DataFrame({
        "Ranking": [f"Top {i}" for i in range(1, 11)] + [f"Produto {i}" for i in range(11, 31)],
        "Nome do Produto": [
            "Produto A", "Produto B", "Produto C", "Produto D", "Produto E",
            "Produto F", "Produto G", "Produto H", "Produto I", "Produto J",
            "Produto K", "Produto L", "Produto M", "Produto N", "Produto O",
            "Produto P", "Produto Q", "Produto R", "Produto S", "Produto T",
            "Produto U"
        ],
        "Status de Busca": ["🔥 SUBINDO"] * 10 + ["ESTÁVEL"] * 20,
        "Melhor País Estratégico": ["Reino Unido 🇬🇧", "EUA 🇺🇸", "Canadá 🇨🇦", "Austrália 🇦🇺"] * 7 + ["Brasil 🇧🇷"],
        "CPC Médio Estimado": ["$0.45", "$0.50", "$0.55", "$0.40", "$0.65"] * 6,
        "Oportunidade": ["Alta validação com baixa concorrência."] * 10 + ["Oportunidade válida."] * 20
    })
    return dados_radar

def auditoria_produto(produto):
    # Simulação de dados de auditoria
    return {
        "Produto": produto,
        "Status de Validação": "Validado com alta demanda.",
        "Benefícios": "Melhora a saúde, aumenta energia.",
        "Dores": "Falta de energia, dificuldade em emagrecer.",
        "Melhor País": "Reino Unido 🇬🇧",
        "CPC Estimado": "$0.55"
    }

def gerar_anuncio(produto):
    return {
        "Títulos": [
            f"Compre {produto} Agora!",
            f"Descontos em {produto}!",
            f"Produto Oficial {produto}",
            f"Melhor Preço para {produto}"
        ],
        "Descrições": [
            "Obtenha descontos exclusivos ao comprar hoje.",
            "Garantia de 60 dias na compra do produto."
        ],
        "Palavras-Chave": [
            f'"{produto} oficial"', f'"comprar {produto}"', f'"{produto} desconto"',
            f'"{produto} online"', f'"{produto} reviews"'
        ],
        "Palavras Negativas": ["grátis", "barato", "fake"]
    }

def caçador_lançamentos():
    return [
        {"Produto": "Produto X", "Oportunidade": "Alta demanda, baixa concorrência.", "Termômetro": "85/100"},
        {"Produto": "Produto Y", "Oportunidade": "Bom potencial de vendas.", "Termômetro": "78/100"}
    ]

def gerar_presell(produto):
    return {
        "Título": f"Oferta Especial para {produto}!",
        "Descrição": f"Garanta sua saúde com {produto}.",
        "Chamada para Ação": "Compre Agora!",
        "Link de Criação": "https://www.hostinger.com/br?REFERRALCODE=VBMCONTAT7WC"
    }

# Menu lateral
menu = st.sidebar.radio(
    "Módulos da Plataforma:",
    [
        "📊 Radar de Produtos", 
        "🛡️ Auditor de Mercado", 
        "✍️ Gerador de Anúncios", 
        "🛰️ Caçador de Lançamentos", 
        "🌐 Fabricante de Pre-sell", 
        "⚙️ Configurações"
    ]
)

# Radar de Produtos
if menu == "📊 Radar de Produtos":
    st.title("📊 MÓDULO: RADAR DE PRODUTOS")
    produtos = gerar_dados_radar()
    st.dataframe(produtos)

# Auditor de Mercado
elif menu == "🛡️ Auditor de Mercado":
    st.title("🛡️ MÓDULO: AUDITOR DE MERCADO")
    produto_audit = st.text_input("Digite o nome do produto:")
    if st.button("🔍 Iniciar Auditoria"):
        resultado = auditoria_produto(produto_audit)
        st.json(resultado)

# Gerador de Anúncios
elif menu == "✍️ Gerador de Anúncios":
    st.title("✍️ MÓDULO: GERADOR DE ANÚNCIOS")
    produto_anuncio = st.text_input("Digite o nome do produto:")
    if st.button("Criar Anúncio"):
        anuncio = gerar_anuncio(produto_anuncio)
        st.json(anuncio)

# Caçador de Lançamentos
elif menu == "🛰️ Caçador de Lançamentos":
    st.title("🛰️ MÓDULO: CAÇADOR DE LANÇAMENTOS")
    resultados = caçador_lançamentos()
    st.json(resultados)

# Fabricante de Pre-sell
elif menu == "🌐 Fabricante de Pre-sell":
    st.title("🌐 MÓDULO: FABRICANTE DE PRE-SELL")
    produto_presell = st.text_input("Digite o nome do produto para criar a pré-venda:")
    if st.button("Gerar Pré-venda"):
        presell = gerar_presell(produto_presell)
        st.json(presell)

# Configurações
elif menu == "⚙️ Configurações":
    st.title("⚙️ MÓDULO: CONFIGURAÇÕES")
    st.write("Área de Configurações em desenvolvimento.")
