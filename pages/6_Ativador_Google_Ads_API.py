# Passo 1: Escolher objetivo
if st.session_state.ads_passo == 1:
    st.markdown("### 🎯 PASSO 1: ESCOLHER SEU OBJETIVO")
    obj_sel = st.radio("Selecione a meta:", OBJETIVOS_CAMPANHA)
    st.write("Objetivo selecionado:", obj_sel)  # Debug
    if st.button("PRÓXIMO PASSO ➔", key="to_p2"):
        st.session_state.v_objetivo = "Vendas" if "Vendas" in obj_sel else "Outros"
