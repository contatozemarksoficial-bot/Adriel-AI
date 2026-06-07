import streamlit as st
import pandas as pd

st.set_page_config(page_title="Radar de Produtos", layout="wide")

st.title("📊 Radar de Produtos [FILTRO XEQUE-MATE]")

# Seus dados do radar
dados_top10 = {
    "Ranking": [f"Top {i}" for i in range(1, 11)],
    "Product Name": ["Sugar Defender", "ProDentim", "GlucoBerry", "Citrus Burn", "LeanBliss", "Puravive", "Java Burn", "Alpilean", "LivPure", "Cortexi"],
    "Status": ["VALIDADO"] * 10
}

st.dataframe(pd.DataFrame(dados_top10), use_container_width=True)
st.button("📥 BAIXAR PLANILHA")
