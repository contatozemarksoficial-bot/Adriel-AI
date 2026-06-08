# =============================================================================================================
# PASSO 1: ESCOLHER SEU OBJETIVO DE CAMPANHA & METAS DE CONVERSÃO
# =============================================================================================================
if st.session_state.ads_passo == 1:
    st.markdown("### 🎯 PASSO 1: ESCOLHER SEU OBJETIVO")
    st.markdown("Escolha um objetivo para personalizar a experiência de acordo com as metas e configurações mais adequadas para sua campanha.")
    
    obj_sel = st.radio(
        "Selecione a meta que ajudaria esta campanha a alcançar o sucesso de acordo com seus critérios:",
        OBJETIVOS_CAMPANHA, index=0, key="radio_step1_meta"
    )
    
    st.write("---")
    st.markdown("#### ⚙️ Usar estas metas de conversão para melhorar Vendas")
    st.markdown("Metas de conversão identificadas como padrão da conta usarão dados de todas as suas campanhas para melhorar a estratégia de lances e o desempenho da campanha.")
    
    col1, col2, col3 = st.columns(3)
    with col1: st.info("**Metas de conversão**\n\nCompras (padrão da conta)")
    with col2: st.info("**Origem da conversão**\n\nSite")
    with col3: st.info("**Ações de conversão**\n\n1 ação")
    
    st.write("")
    if st.button("PRÓXIMO PASSO ➔", key="to_p2"):
        st.session_state.v_objetivo = "Vendas" if "Vendas" in obj_sel else "Outros"
        st.session_state.ads_passo = 2
        st.success("✅ Objetivo gravado na memória com sucesso!")
        time.sleep(0.3)
        st.rerun()
