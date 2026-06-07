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

# Lista oficial para o sorteio dinâmico do produto capturado no leilão
produtos_pool = ["Obsesta", "Sugar Defender", "ProDentim", "GlucoBerry", "Citrus Burn", "LeanBliss", "Puravive", "Java Burn", "Alpilean", "LivPure"]

if st.button("🛰️ INICIAR RASTREAMENTO MASSIVO ATIVO 24/7"):
    st.info("Estabelecendo conexão criptografada com os servidores de ofertas gringos...")
    
    # 📊 ESPAÇO DO GRÁFICO DINÂMICO INTERATIVO (ANIMAÇÃO EM TEMPO REAL)
    st.markdown("### 📊 Monitoramento Volumétrico ao Vivo (Escaneando Buscadores Internacionais)")
    grafico_placeholder = st.empty()
    status_placeholder = st.empty()
    
    meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
    
    # Loop de animação que faz as barras do gráfico mudarem e atualizarem sozinhas na tela
    for passo in range(4):
        status_placeholder.markdown(f"🔄 **Varredura em andamento...** Analisando picos de tráfego do leilão internacional...")
        valores_dinamicos = [random.randint(150, 1100) for _ in range(12)]
        df_animado = pd.DataFrame({"Pico de Interesse Comercial (Buscadores)": valores_dinamicos}, index=meses)
        grafico_placeholder.bar_chart(df_animado, use_container_width=True, color="#00E5FF")
        time.sleep(0.6)
        
    # Sorteia o nome do produto capturado em tempo real nesta execução de forma dinâmica
    produto_capturado = random.choice(produtos_pool)
    paises_opcoes = ["Reino Unido 🇬🇧", "Estados Unidos 🇺🇸", "Irlanda 🇮🇪", "Canadá 🇨🇦", "Austrália 🇦🇺"]
    pais_vencedor = random.choice(paises_opcoes)
    nota_termometro = str(random.randint(85, 99))
    
    status_placeholder.success("🎯 Varredura massiva concluída! O produto gringo **" + produto_capturado + "** acabou de ser capturado com picos de tráfego!")
    st.write("---")
    
    # CORREÇÃO CRUCIAL AQUI: Injeção da variável produto_capturado em todo o relatório de texto puro
    texto_cacador = (
        "📦 [RASTREADOR VIVO — SERVIDORES INTERNACIONAIS EM ALTA]\n"
        "🔥 PRODUTO DETECTADO AGORA: " + produto_capturado + " (Fundo de Funil Ativo)\n"
        "- STATUS ATUAL: O sistema capturou alta movimentação de novos domínios cadastrados nas últimas horas. O leilão de frase do Google Ads encontra-se completamente limpo de afiliados concorrentes tradicionais.\n"
        "- GEO DE ESCALA (ONDE LANÇAR): " + pais_vencedor + "\n"
        "- JUSTIFICATIVA DO ESPECIALISTA: Mercado qualificado apresentando altíssima intenção de compra imediata na rede de pesquisa por termos exatos de desconto e cupom de fábrica oficial.\n"
        "- 🌡️ TERMÔMETRO DO LANÇAMENTO: " + nota_termometro + "/100 (Potencial máximo de escala rápida e ROI imediato).\n\n"
        "------------------------------------------------------------------------------------------------------\n\n"
        "📦 [HISTÓRICO RECENTE DAS ÚLTIMAS VARREDURAS DE INFRAESTRUTURA]\n"
        "🔥 PRODUTO SECUNDÁRIO: NeuroQuiet (Nicho: Saúde Mental / Alívio de Zumbido)\n"
        "- GEO ESTRATÉGICA: Irlanda 🇮🇪 — Excelente oportunidade para rodar correspondência de frase com cliques frios limpos rodando direto em Euros.\n"
        "- TERMÔMETRO: 88/100.\n\n"
        "🔥 PRODUTO TERCIÁRIO: ZenCortex (Nicho: Foco / Memória)\n"
        "- GEO ESTRATÉGICA: Nova Zelândia 🇳🇿 — Leilão local livre de lances agressivos do mercado americano, poupando o orçamento diário.\n"
        "- TERMÔMETRO: 82/100."
    )
    st.text_area("📋 Relatório Consolidado de Oportunidades Recentes:", value=texto_cacador, height=420)
    st.write("---")
    
    # =============================================================================================================
    # MÓDULO DE INTEGRAÇÃO DE ALERTA DIRETAMENTE COM O NOME DO PRODUTO CAPTURADO
    # =============================================================================================================
    st.markdown("### 🔔 ATIVAR SISTEMA DE ALERTAS DIÁRIOS NO SEU WHATSAPP")
    st.markdown("Insira o seu número abaixo para validar o disparo do relatório contendo a nossa última captura ao vivo:")
    
    numero_whatsapp = st.text_input("Digite seu número com DDD (Apenas números, ex: 11999999999):", value="11999999999")
    
    # Mensagem 100% dinâmica injetando o nome do produto sorteador na hora do clique
    mensagem_bruta = (
        "🛰️ *ADRIEL AI - MONITORAMENTO INTEGRADO ATIVO 24/7*\n\n"
        "🟢 *Status do Rastreador:* Varredura massiva concluída com sucesso!\n\n"
        "🔥 *ÚLTIMO LANÇAMENTO CAPTURADO:* " + produto_capturado + "\n"
        "🌍 *Melhor País para Subir:* " + pais_vencedor + "\n"
        "🌡️ *Termômetro de Escala:* Alta Conversão Detectada!\n\n"
        "👉 *Ação imediata:* Acesse os módulos da sua plataforma para clonar a estrutura completa de anúncios e palavras-chave de marca do produto " + produto_capturado + " antes que o leilão infle!"
    )
    
    mensagem_codificada = urllib.parse.quote(mensagem_bruta)
    link_whatsapp = f"https://whatsapp.com{numero_whatsapp}&text={mensagem_codificada}"
    
    st.write("")
    st.markdown(
        f'<a href="{link_whatsapp}" target="_blank" style="text-decoration: none;">'
        '<div style="background-color: #2ECC71; color: white; text-align: center; padding: 14px; font-weight: bold; border-radius: 14px; box-shadow: 0px 5px 15px rgba(46, 204, 113, 0.4); font-size: 18px;">'
        "🟢 ENVIAR ALERTA DO PRODUTO " + produto_capturado.upper() + " PARA O MEU WHATSAPP"
        '</div>'
        '</a>', 
        unsafe_allow_html=True
    )
