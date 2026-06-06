import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(page_title="Adriel AI - Plataforma Master", layout="wide")

# Função para gerar dados de radar
def gerar_dados_radar():
    num_produtos = 30
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
def auditoria
