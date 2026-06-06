with tab3:
    st.subheader("⚙️ Máquina de Ads (Fundo de Funil)")
    prod_ads = st.text_input("Qual o produto para a campanha?")
    
    # Criamos uma chave no st.session_state para guardar o resultado
    if "res_ads" not in st.session_state:
        st.session_state.res_ads = None

    if st.button("Gerar Estrutura"):
        with st.spinner("Construindo campanha blindada..."):
            st.session_state.res_ads = model.generate_content(f"Crie uma campanha de Google Ads para {prod_ads}. Use políticas de tráfego seguro. Títulos, descrições, palavras-chave e negativas.")
            st.code(st.session_state.res_ads.text)

    # Só mostra o botão de download se já tiver sido gerado algo
    if st.session_state.res_ads:
        st.download_button("📥 Baixar Estrutura (.txt)", st.session_state.res_ads.text, file_name=f"Campanha_{prod_ads}.txt")
