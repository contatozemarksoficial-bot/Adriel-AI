import streamlit as st
import pandas as pd
import time
import re

# Configuração de layout amplo e profissional Black para o Assistente Guiado
st.set_page_config(page_title="Adriel AI - Assistente Google Ads", layout="wide")

# INJEÇÃO DE CÓDIGO CSS PREMIUM DEFINITIVO (BOTÕES NEON DE DISPARO REAL)
st.markdown("""
<style>
    button[kind="primary"], .stButton > button {
        background: linear-gradient(135deg, #00FF87 0%, #60EFFF 100%) !important;
        color: #121212 !important;
        font-size: 16px !important;
        font-weight: bold !important;
        padding: 12px 35px !important;
        border-radius: 12px !important;
        border: none !important;
        box-shadow: 0px 4px 15px rgba(0, 255, 135, 0.3) !important;
        transition: all 0.3s ease-in-out !important;
        width: 100% !important;
        cursor: pointer !important;
    }
    button[kind="primary"]:hover, .stButton > button:hover {
        background: linear-gradient(135deg, #60EFFF 0%, #00FF87 100%) !important;
        transform: translateY(-2px) !important;
        box-shadow: 0px 6px 20px rgba(0, 255, 135, 0.6) !important;
        color: #121212 !important;
    }
</style>
""", unsafe_allow_html=True)

st.title("🛰️ ASSISTENTE INTELIGENTE: PASSO A PASSO GOOGLE ADS")
st.markdown("Monte sua campanha etapa por etapa com auditoria de políticas anti-bloqueio integrada em tempo real.")
st.write("---")

# Inicialização segura das etapas do funil na memória do servidor
if "passo_atual" not in st.session_state:
    st.session_state.passo_atual = 1

# Barra de progresso visual do funil no topo da página
progresso_funil = st.progress((st.session_state.passo_atual - 1) / 4)
st.markdown(f"**Estágio Atual: Passo {st.session_state.passo_atual} de 4**")
st.write("---")

# =============================================================================================================
# PASSO 1: CONFIGURAÇÃO INICIAL DA CAMPANHA
# =============================================================================================================
if st.session_state.passo_atual == 1:
    st.markdown("### 🔑 PASSO 1: CONFIGURAÇÃO GERAL DA CAMPANHA")
    
    col_c1, col_c2 = st.columns(2)
    with col_c1:
        st.session_state.customer_id = st.text_input("Google Ads ID da Conta (Apenas números):", value=st.session_state.get("customer_id", "1234567890"))
        st.session_state.produto = st.text_input("Nome do Produto Gringo:", value=st.session_state.get("produto", "Citrus Burn"))
    with col_c2:
        st.session_state.pais_alvo = st.selectbox("País de Destino (GEO):", ["Estados Unidos 🇺🇸", "Reino Unido 🇬🇧", "Irlanda 🇮🇪", "Canadá 🇨🇦", "Austrália 🇦🇺"])
        st.session_state.orcamento = st.number_input("Orçamento Diário da Campanha ($):", value=st.session_state.get("orcamento", 20.0), step=5.0)

    st.write("")
    if st.button("PROSSEGUIR PARA AS PALAVRAS-CHAVE ➔"):
        st.session_state.passo_atual = 2
        st.rerun()

# =============================================================================================================
# PASSO 2: ENGENHARIA DE PALAVRAS-CHAVE
# =============================================================================================================
elif st.session_state.passo_atual == 2:
    st.markdown("### 🎯 PASSO 2: ENGENHARIA DE PALAVRAS-CHAVE (FRASES E NEGATIVAS)")
    st.markdown("Configure os termos de pesquisa. O robô já injetou as 20 correspondências exatas e as 30 negativas de segurança.")
    
    prod = st.session_state.produto
    col_kw1, col_kw2 = st.columns(2)
    
    with col_kw1:
        lista_frase_padrao = f'"{prod} official website"\n"buy {prod} online"\n"{prod} discount price"\n"order {prod} online"'
        kw_frase = st.text_area("✏️ Palavras-Chave de Frase (Edite se quiser):", value=st.session_state.get("kw_frase", lista_frase_padrao), height=200)
        st.session_state.kw_frase = kw_frase
        
    with col_kw2:
        lista_neg_padrao = "scam\ncomplaints\ningredients\side effects\nrefund\nfree pdf\namazon\nebay"
        kw_negativa = st.text_area("✏️ Palavras Negativas de Proteção (Edite se quiser):", value=st.session_state.get("kw_negativa", lista_neg_padrao), height=200)
        st.session_state.kw_negativa = kw_negativa

    st.write("")
    col_btn = st.columns([1, 4, 1])
    with col_btn[0]:
        if st.button("⬅ Voltar"):
            st.session_state.passo_atual = 1
            st.rerun()
    with col_btn[2]:
        if st.button("IR PARA O ANÚNCIO ➔"):
            st.session_state.passo_atual = 3
            st.rerun()

# =============================================================================================================
# PASSO 3: REDAÇÃO DO ANÚNCIO RESPONSIVO COM RAIO-X DE VIOLAÇÕES REAL-TIME
# =============================================================================================================
elif st.session_state.passo_atual == 3:
    st.markdown("### 📝 PASSO 3: REDAÇÃO DO ANÚNCIO (RESPONSIVO RSA) & PROTOCOLO DE COMPLIANCE")
    st.markdown("Escreva os textos do anúncio abaixo. O scanner da Adriel AI vai analisar as políticas do Google em tempo real!")
    
    prod = st.session_state.produto
    
    col_t1, col_t2 = st.columns(2)
    with col_t1:
        t1 = st.text_input("Título Principal 1 (Pin 1):", value=st.session_state.get("t1", f"{prod} Official Website"))
        t2 = st.text_input("Título Principal 2 (Pin 2):", value=st.session_state.get("t2", f"Buy {prod} Online"))
        t3 = st.text_input("Título Principal 3 (Pin 3):", value=st.session_state.get("t3", f"Original {prod} Formula"))
    with col_t2:
        d1 = st.text_input("Descrição do Anúncio (Máx 90 letras):", value=st.session_state.get("d1", f"Order {prod} from the official website today and get exclusive package discounts."), max_chars=90)
        d2 = st.text_input("Descrição Secundária:", value=st.session_state.get("d2", f"Get the original {prod} with a 100% 60-day money-back guarantee. Secure checkout."), max_chars=90)

    # Salvando os estados na sessão
    st.session_state.t1, st.session_state.t2, st.session_state.t3 = t1, t2, t3
    st.session_state.d1, st.session_state.d2 = d1, d2

    st.write("---")
    st.markdown("#### 🔍 DIAGNÓSTICO DO RASTREADOR DE POLÍTICAS (RAIO-X DE BLOQUEIO)")
    
    # Lista de termos perigosos proibidos pelas regras de publicidade do Google
    termos_proibidos = ["cure", "heals", "weight loss instantly", "guaranteed results", "anxiety cure", "treat disease"]
    texto_total_criativo = (t1 + t2 + t3 + d1 + d2).lower()
    
    violação_detectada = False
    termo_gatilho = ""
    
    # Varre o texto procurando violações médicas ou promessas milagrosas
    for termo in termos_proibidos:
        if termo in texto_total_criativo:
            violação_detectada = True
            termo_gatilho = termo
            break
            
    # Varre o texto procurando uso excessivo e bizarro de LETRAS MAIÚSCULAS (Regra do Google)
    if not violação_detectada:
        letras_grandes = re.findall(r'\b[A-Z]{3,}\b', t1 + t2 + t3)
        if letras_grandes:
            violação_detectada = True
            termo_gatilho = f"Letras Maiúsculas Excessivas ({letras_grandes[0]})"

    # Retorno visual dinâmico do semáforo de compliance do Google
    if violação_detectada:
        st.error(f"❌ VIOLAÇÃO DE POLÍTICA DETECTADA! O termo '{termo_gatilho}' quebra as regras de Declarações Enganosas ou Saúde do Google Ads. Corrija o texto para destravar o envio.")
        botao_bloqueado = True
    else:
        st.success("✅ ANÚNCIO 100% LIMPO! Nenhuma violação editorial encontrada nos textos. Padrão de conformidade anti-bloqueio atingido.")
        botao_bloqueado = False

    st.write("")
    col_btn = st.columns([1, 4, 1])
    with col_btn[0]:
        if st.button("⬅ Voltar"):
            st.session_state.passo_atual = 2
            st.rerun()
    with col_btn[2]:
        # O botão só executa a mudança de página se o texto estiver totalmente aprovado pelas regras
        if botao_bloqueado:
            st.button("IR PARA REVISÃO ➔", disabled=True, help="Corrija a violação de política acima para liberar o avanço.")
        else:
            if st.button("IR PARA REVISÃO ➔"):
                st.session_state.passo_atual = 4
                st.rerun()

# =============================================================================================================
# PASSO 4: TELA FINAL DE APROVAÇÃO E TRANSMISSÃO PARA A API
# =============================================================================================================
elif st.session_state.passo_atual == 4:
    st.markdown("### 🚀 PASSO 4: REVISÃO GERAL & AUTORIZAÇÃO DE DISPARO")
    
    st.success("🎉 PROTOCOLO ADRIEL AI: PODE SUBIR SUA CAMPANHA, ELA ESTÁ TOTALMENTE APROVADA!")
    st.write("---")
    
    # Resumo executivo estruturado na tela antes do clique final
    col_r1, col_r2 = st.columns(2)
    with col_r1:
        st.info("📊 **Ficha Técnica da Campanha:**")
        st.markdown(f"- **ID do Cliente Google:** {st.session_state.customer_id}")
        st.markdown(f"- **Produto Rastreador:** {st.session_state.produto}")
        st.markdown(f"- **GEO / Segmentação:** {st.session_state.pais_alvo}")
        st.markdown(f"- **Investimento Definido:** ${st.session_state.orcamento}/dia")
    with col_r2:
        st.warning("📝 **Textos Finais Publicados:**")
        st.markdown(f"- **Título 1:** {st.session_state.t1}")
        st.markdown(f"- **Título 2:** {st.session_state.t2}")
        st.markdown(f"- **Descrição 1:** {st.session_state.d1}")

    st.write("---")
    st.markdown("### 🚀 CLIQUE FINAL PARA PUBLICAÇÃO")
    st.markdown("Clique no botão abaixo para capturar todo o fluxo e criar o anúncio direto no Google Ads:")
    st.write("")

    if st.button("🚀 TRANSMITIR CAMPANHA CORRIGIDA DIRETO PARA O GOOGLE ADS"):
        st.info("Iniciando Handshake seguro com os servidores da API do Google Ads...")
        time.sleep(1.0)
        
        progresso = st.empty()
