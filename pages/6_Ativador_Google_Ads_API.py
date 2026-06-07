import streamlit as st
import pandas as pd
import time
import re

# Configuração de layout amplo e profissional Black para o Assistente Guiado de Elite
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
st.markdown("Monte sua campanha etapa por etapa com auditoria e autocorreção de políticas anti-bloqueio integradas.")
st.write("---")

# Inicialização segura das etapas do funil na memória do servidor
if "passo_atual" not in st.session_state:
    st.session_state.passo_atual = 1

# Inicialização dos campos do anúncio para suportar a reedição e autocorreção via botão
if "t1_val" not in st.session_state: st.session_state.t1_val = "Citrus Burn Official Website"
if "t2_val" not in st.session_state: st.session_state.t2_val = "Buy Citrus Burn Online"
if "t3_val" not in st.session_state: st.session_state.t3_val = "Original Citrus Burn Formula"
if "d1_val" not in st.session_state: st.session_state.d1_val = "Order Citrus Burn from the official website today and get exclusive package discounts."
if "d2_val" not in st.session_state: st.session_state.d2_val = "Get the original product with a 100% 60-day money-back guarantee. Secure checkout."

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
        produto_atual = st.text_input("Nome do Produto Gringo:", value=st.session_state.get("produto", "Citrus Burn"))
        if produto_atual != st.session_state.get("produto", ""):
            st.session_state.produto = produto_atual
            # Atualiza sugestões iniciais se o produto mudar
            st.session_state.t1_val = f"{produto_atual} Official Website"
            st.session_state.t2_val = f"Buy {produto_atual} Online"
            st.session_state.t3_val = f"Original {produto_atual} Formula"
            st.session_state.d1_val = f"Order {produto_atual} from the official website today and get exclusive package discounts."
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
    st.markdown("Configure os termos de pesquisa de leilão.")
    
    prod = st.session_state.produto
    col_kw1, col_kw2 = st.columns(2)
    
    with col_kw1:
        lista_frase_padrao = f'"{prod} official website"\n"buy {prod} online"\n"{prod} discount price"\n"order {prod} online"'
        kw_frase = st.text_area("✏️ Palavras-Chave de Frase (Edite se quiser):", value=st.session_state.get("kw_frase", lista_frase_padrao), height=200)
        st.session_state.kw_frase = kw_frase
        
    with col_kw2:
        lista_neg_padrao = "scam\ncomplaints\ningredients\nside effects\nrefund\nfree pdf\namazon\nebay"
        kw_negativa = st.text_area("✏️ Palavras Negativas de Proteção (Edite se quiser):", value=st.session_state.get("kw_negativa", lista_neg_padrao), height=200)
        st.session_state.kw_negativa = kw_negativa

    st.write("")
    col_btn1, col_btn2 = st.columns([1, 10])
    with col_btn1:
        if st.button("⬅ Voltar"):
            st.session_state.passo_atual = 1
            st.rerun()
    with col_btn2:
        if st.button("IR PARA O ANÚNCIO ➔"):
            st.session_state.passo_atual = 3
            st.rerun()

# =============================================================================================================
# PASSO 3: REDAÇÃO DO ANÚNCIO RESPONSIVO COM AUTO-CORREÇÃO DE POLÍTICAS EM 1 CLIQUE
# =============================================================================================================
elif st.session_state.passo_atual == 3:
    st.markdown("### 📝 PASSO 3: REDAÇÃO DO ANÚNCIO (RESPONSIVO RSA) & PROTOCOLO DE COMPLIANCE")
    st.markdown("Escreva ou modifique os textos abaixo. O scanner Adriel AI caça violações e as corrige instantaneamente!")
    
    col_t1, col_t2 = st.columns(2)
    with col_t1:
        t1 = st.text_input("Título Principal 1 (Pin 1):", value=st.session_state.t1_val)
        t2 = st.text_input("Título Principal 2 (Pin 2):", value=st.session_state.t2_val)
        t3 = st.text_input("Título Principal 3 (Pin 3):", value=st.session_state.t3_val)
    with col_t2:
        d1 = st.text_input("Descrição do Anúncio (Máx 90 letras):", value=st.session_state.d1_val, max_chars=90)
        d2 = st.text_input("Descrição Secundária:", value=st.session_state.d2_val, max_chars=90)

    # Armazena temporariamente o texto digitado na tela pelo usuário
    st.session_state.t1_val, st.session_state.t2_val, st.session_state.t3_val = t1, t2, t3
    st.session_state.d1_val, st.session_state.d2_val = d1, d2

    st.write("---")
    st.markdown("#### 🔍 DIAGNÓSTICO DO RASTREADOR DE POLÍTICAS (RAIO-X DE BLOQUEIO)")
    
    # Dicionário de regras mapeando [Termo Proibido] -> [Substituto Seguro de Compliance]
    regras_correcao = {
        "cure": "support formula",
        "heals": "supports health",
        "weight loss instantly": "natural weight support",
        "guaranteed results": "satisfaction guarantee",
        "anxiety cure": "calm support ritual",
        "treat disease": "promote wellness lifestyle"
    }
    
    texto_completo_original = (t1 + " " + t2 + " " + t3 + " " + d1 + " " + d2).lower()
    
    violacao_termo = False
    violacao_capital = False
    gatilho_detalhado = ""
    
    # 1. Verifica se há palavras médicas banidas pelo Google
    for termo_ruim in regras_correcao.keys():
        if termo_ruim in texto_completo_original:
            violacao_termo = True
            gatilho_detalhado = termo_ruim
            break
            
    # 2. Verifica se há violação de CAPITALIZAÇÃO EXCESSIVA (Letras maiúsculas travadas como BUY NOW)
    letras_grandes = re.findall(r'\b[A-Z]{3,}\b', t1 + " " + t2 + " " + t3)
    if not violacao_termo and letras_grandes:
        violacao_capital = True
        gatilho_detalhado = f"Letras Maiúsculas Abusivas: {letras_grandes}"

    # Retorno visual inteligente na tela baseado na detecção de violações
    if violacao_termo or violacao_capital:
        st.error(f"❌ RISCO DE BLOQUEIO DETECTADO! Motivo: '{gatilho_detalhado}'. Esta estrutura viola as diretrizes editoriais ou de alegações médicas do Google Ads.")
        
        # ⚡ ENGENHARIA DE AUTOCORREÇÃO ATIVADA EM UM CLIQUE DE LUXO
        st.markdown("**💡 O Robô Adriel AI estruturou a correção segura para você. Clique abaixo para aplicar:**")
        if st.button("⚡ CORRIGIR TEXTO AUTOMATICAMENTE (ANTI-BLOQUEIO)"):
            
            # Corrige palavras médicas substituindo pelos sinônimos seguros
            for ruim, seguro in regras_correcao.items():
                st.session_state.t1_val = re.sub(ruim, seguro, st.session_state.t1_val, flags=re.IGNORECASE)
                st.session_state.t2_val = re.sub(ruim, seguro, st.session_state.t2_val, flags=re.IGNORECASE)
                st.session_state.t3_val = re.sub(ruim, seguro, st.session_state.t3_val, flags=re.IGNORECASE)
                st.session_state.d1_val = re.sub(ruim, seguro, st.session_state.d1_val, flags=re.IGNORECASE)
                st.session_state.d2_val = re.sub(ruim, seguro, st.session_state.d2_val, flags=re.IGNORECASE)
                
            # Corrige letras maiúsculas excessivas transformando em Capitalize Padrão (Title Case)
            if violacao_capital:
                st.session_state.t1_val = st.session_state.t1_val.title()
                st.session_state.t2_val = st.session_state.t2_val.title()
                st.session_state.t3_val = st.session_state.t3_val.title()
                
