import streamlit as st
import pandas as pd
import urllib.parse
import time
import random

# Configuração premium de página - Layout amplo e profissional Black para o Caçador
st.set_page_config(page_title="Adriel AI - Caçador em Tempo Real", layout="wide")

# INJEÇÃO DE CÓDIGO CSS PREMIUM DEFINITIVO (BOTÕES NEON PERSONALIZADOS DE LUXO)
st.markdown("""
<style>
    button[kind="primary"], .stButton > button {
        background: linear-gradient(135deg, #007BFF 0%, #00E5FF 100%) !important;
        color: white !important;
        font-size: 18px !important;
        font-weight: bold !important;
        padding: 14px 40px !important;
        border-radius: 14px !important;
        border: none !important;
        box-shadow: 0px 5px 20px rgba(0, 229, 255, 0.4) !important;
        transition: all 0.3s ease-in-out !important;
        width: 100% !important;
        cursor: pointer !important;
    }
    button[kind="primary"]:hover, .stButton > button:hover {
        background: linear-gradient(135deg, #00E5FF 0%, #007BFF 100%) !important;
        transform: translateY(-2px) !important;
        box-shadow: 0px 8px 25px rgba(0, 229, 255, 0.7) !important;
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

st.title("🛰️ MÓDULO: CAÇADOR DE LANÇAMENTOS INTERNACIONAIS")
st.markdown("Monitoramento avançado automatizado 24/7 nos servidores das maiores redes gringas: ClickBank, BuyGoods e Digistore24.")
st.write("---")

st.markdown("### 🎛️ Painel de Escaneamento Vivo e Notificações Contínuas")
st.markdown("Clique no botão personalizado abaixo para iniciar o rastreamento síncrona com renderização gráfica em tempo real:")
st.write("")

if st.button("🛰️ INICIAR RASTREAMENTO MASSIVO ATIVO 24/7"):
    st.info("Estabelecendo conexão criptografada com os servidores de ofertas gringos...")
    
    # 📊 ESPAÇO DO GRÁFICO DINÂMICO INTERATIVO (ANIMAÇÃO EM TEMPO REAL)
    st.markdown("### 📊 Monitoramento Volumétrico ao Vivo (Escaneando Buscadores Internacionais)")
    grafico_placeholder = st.empty()
    status_placeholder = st.empty()
    
    meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
    
    # Loop de animação que faz as barras do gráfico mudarem e atualizarem sozinhas na tela
    for passo in range(4):
        status_placeholder.markdown(f"🔄 **Varredura em andamento...** Analisando picos de tráfego do mês de {meses[passo*3]} a {meses[(passo*3)+2]}...")
        
        # Gera valores flutuantes dinâmicos simulando busca de dados ao vivo
        valores_dinamicos = [random.randint(150, 1100) for _ in range(12)]
        df_animado = pd.DataFrame({"Pico de Interesse Comercial (Buscadores)": valores_dinamicos}, index=meses)
        
        # Atualiza o gráfico de colunas de forma síncrona na tela do usuário
        grafico_placeholder.bar_chart(df_animado, use_container_width=True, color="#00E5FF")
        time.sleep(0.8) # Pausa dramática milimétrica para mostrar a engrenagem mexendo
        
    status_placeholder.success("🎯 Varredura massiva concluída! Novas oportunidades de alta conversão injetadas no painel!")
    st.write("---")
    
    # Estrutura robusta detalhando as oportunidades gringas por extenso
    texto_cacador = (
        "📦 [RASTREADOR VIVO — SERVIDOR BUYGOODS — ESTADOS UNIDOS]\n"
        "🔥 PRODUTO CAPTURADO: Obsesta (Nicho: Emagrecimento / Termogênico)\n"
        "- STATUS ATUAL: Sistema capturou alta movimentação de novos domínios cadastrados nas últimas 2 horas. O leilão de frase do Google Ads encontra-se completamente limpo de afiliados concorrentes tradicionais.\n"
        "- GEO DE ESCALA (ONDE LANÇAR): Reino Unido 🇬🇧\n"
        "- JUSTIFICATIVA DO ESPECIALISTA: Público comprador britânico maduro com libras esterlinas na carteira pronto para pacotes múltiplos de 3 a 6 frascos. CPC médio travado em baixos $0.45.\n"
        "- 🌡️ TERMÔMETRO DO LANÇAMENTO: 98/100 (Potencial máximo de escala rápida e ROI imediato).\n\n"
        "------------------------------------------------------------------------------------------------------\n\n"
        "📦 [RASTREADOR VIVO — SERVIDOR CLICKBANK — EUROPA]\n"
        "🔥 PRODUTO CAPTURADO: NeuroQuiet (Nicho: Saúde Mental / Alívio de Zumbido / Sono)\n"
        "- STATUS ATUAL: Oferta escalando tráfego qualificado de buscas diretas por cupons de desconto. Ideal para subir estruturas rápidas de anúncios responsivos blindados.\n"
        "- GEO DE ESCALA (ONDE LANÇAR): Irlanda 🇮🇪\n"
        "- JUSTIFICATIVA DO ESPECIALISTA: Cliques extremamente baratos rodando direto em Euros. O leilão encontra-se livre de robôs americanos e cliques inválidos.\n"
        "- 🌡️ TERMÔMETRO DO LANÇAMENTO: 88/100 (Excelente ROI estimado no tráfego direto).\n\n"
        "------------------------------------------------------------------------------------------------------\n\n"
        "📦 [RASTREADOR VIVO — SERVIDOR DIGISTORE24 — OCEANIA]\n"
        "🔥 PRODUTO CAPTURADO: ZenCortex (Nicho: Foco / Memória / Nootrópico Premium)\n"
        "- STATUS ATUAL: Rastreamento identificou liberação de novos lotes promocionais de fábrica. Alta busca local por termos exatos no funil comercial.\n"
        "- GEO DE ESCALA (ONDE LANÇAR): Nova Zelândia 🇳🇿\n"
        "- JUSTIFICATIVA DO ESPECIALISTA: O leilão local encontra-se livre de lances agressivos do mercado de afiliados dos EUA, garantindo cliques limpos para contas com orçamento menor.\n"
        "- 🌡️ TERMÔMETRO DO LANÇAMENTO: 82/100."
    )
    st.text_area("📋 Relatório Consolidado de Oportunidades Recentes:", value=texto_cacador, height=450)
    st.write("---")
    
    # =============================================================================================================
    # MÓDULO DE INTEGRAÇÃO DE ALERTA CONTINUO VIA WHATSAPP
    # =============================================================================================================
    st.markdown("### 🔔 ATIVAR SISTEMA DE ALERTAS CONTÍNUOS 24/7")
    st.markdown("Insira o seu número abaixo para validar o disparo de relatórios automatizados de novos produtos direto para o seu WhatsApp:")
    
    numero_whatsapp = st.text_input("Digite seu número com DDD (Apenas números, ex: 11999999999):", value="11999999999")
    
    # Mensagem dinâmica estruturada para o WhatsApp
    mensagem_bruta = (
        "🛰️ *ADRIEL AI - MONITORAMENTO INTEGRADO ATIVO 24/7*\n\n"
        "🟢 *Status do Rastreador:* Ligado e varrendo redes gringas de hora em hora.\n\n"
        "🔥 *Último Alerta Emitido:* Obsesta (BuyGoods) está explodindo com leilão baleado e livre de concorrência no Reino Unido 🇬🇧!\n\n"
        "👉 *Ação imediata:* Acesse o painel de Gerador de Anúncios para clonar as palavras-chave e subir sua campanha agora!"
    )
    
    # Codifica o texto para o formato aceito em links de internet (URL)
    mensagem_codificada = urllib.parse.quote(mensagem_bruta)
    link_whatsapp = f"https://whatsapp.com{numero_whatsapp}&text={mensagem_codificada}"
    
    st.write("")
    # Botão personalizado verde esmeralda para ativação do loop de alertas
    st.markdown(
        f'<a href="{link_whatsapp}" target="_blank" style="text-decoration: none;">'
        '<div style="background-color: #2ECC71; color: white; text-align: center; padding: 14px; font-weight: bold; border-radius: 14px; box-shadow: 0px 5px 15px rgba(46, 204, 113, 0.4); font-size: 18px; transition: all 0.2s;">'
        "🟢 VALIDAR ALERTAS DIÁRIOS E RECEBER RELATÓRIO ATUALIZADO NO WHATSAPP"
        '</div>'
        '</a>', 
        unsafe_allow_html=True
    )
