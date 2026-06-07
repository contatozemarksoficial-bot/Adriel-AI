import streamlit as st
import pandas as pd
import google.generativeai as genai

st.title("📊 Radar de Produtos")
st.write("Análise de mercado em tempo real.")

if st.button("Carregar Dados"):
    data = {"Produto": ["Sugar Defender", "ProDentim"], "Status": ["Validado", "Em Alta"]}
    st.dataframe(pd.DataFrame(data))
