# ... (seu código acima)

# BARRA LATERAL E NAVEGAÇÃO
st.sidebar.title("🎛️ Adriel AI")
menu = st.sidebar.radio("Módulos:", ["📊 Radar", "🛡️ Auditor", "✍️ Gerador", "🛰️ Caçador", "🌐 Pre-sell"])

if menu == "📊 Radar":
    st.title("📊 Radar de Produtos")
    st.dataframe(st.session_state.dados_radar_dinamico, use_container_width=True)

elif menu == "🛡️ Auditor":
    prod = st.text_input("Produto:")
    if st.button("Auditar"):
        st.session_state.resposta_auditoria = executar_auditoria(prod)
    st.write(st.session_state.resposta_auditoria)

elif menu == "✍️ Gerador":
    prod = st.text_input("Produto:")
    if st.button("Gerar Ads"):
        st.session_state.resposta_gerador = executar_gerador(prod)
    st.code(st.session_state.resposta_gerador)

elif menu == "🛰️ Caçador":
    st.title("🛰️ Caçador de Lançamentos")
    st.write(executar_cacador())

elif menu == "🌐 Pre-sell":
    prod = st.text_input("Produto:")
    if st.button("Criar Pre-sell"):
        st.session_state.resposta_presell = executar_presell(prod)
    st.code(st.session_state.resposta_presell)
