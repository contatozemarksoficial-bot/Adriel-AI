import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(page_title="Adriel AI - Plataforma Master", layout="wide")

# Função para gerar dados de radar
def gerar_dados_radar():
    # Aqui definimos o comprimento desejado
    num_produtos = 30
    # Simulação dos dados do radar
    dados_radar = pd.DataFrame({
        "Ranking": [f"Top {i}" for i in range(1, 11)] + [f"Produto {i}" for i in range(11, num_produtos + 1)],
        "Nome do Produto": [
            "Produto A", "Produto B", "Produto C", "Produto D", "Produto E",
            "Produto F", "Produto G", "Produto H", "Produto I", "Produto J",
            "Produto K", "Produto L", "Produto M", "Produto N", "Produto O",
            "Produto P", "Produto Q", "Produto R", "Produto S", "Produto T",
            "Produto U", "Produto V", "Produto W", "Produto X", "Produto Y",
            "Produto Z", "Produto AA", "Produto AB", "Produto AC", "Produto AD",
            "Produto AE"
        ],
        "Status de Busca": ["🔥 SUBINDO"] * 10 + ["ESTÁVEL"] * 20,
        "Melhor País Estratégico": ["Reino Unido 🇬🇧", "EUA 🇺🇸", "Canadá 🇨🇦", "Austrália 🇦🇺"] * 7 + ["Brasil 🇧🇷"],
        "CPC Médio Estimado": ["$0.45", "$0.50", "$0.55", "$0.40", "$0.65"] * 6 + ["$0.60", "$0.70"],
        "Oportunidade": ["Alta validação com baixa concorrência."] * 10 + ["Oportunidade válida."] * 20
    })
    return dados_radar

# Função para auditoria de produto
def auditoria_produto(produto):
    return {
        "Produto": produto,
        "Status de Validação": "Validado com alta demanda.",
        "Benefícios": "Melhora a saúde, aumenta energia.",
        "Dores": "Falta de energia, dificuldade em emagrecer.",
        "Melhor País": "Reino Unido 🇬🇧",
        "CPC Estimado": "$0.55"
    }

# Função para gerar anúncios
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

# Função para caçador de lançamentos
def caçador_lançamentos():
    return [
        {"Produto": "Produto X", "Oportunidade": "Alta demanda, baixa concorrência.", "Termômetro": "85/100"},
        {"Produto": "Produto Y", "Oportunidade": "Bom potencial de vendas.", "Termômetro": "78/100"}
    ]

# Função para gerar pré-venda
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
    ["📊 Radar de Produtos", "🛡️ Auditor de Mercado", "✍️ Gerador de Anúncios", 
     "🛰️ Caçador de Lanç
