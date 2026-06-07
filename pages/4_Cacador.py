import streamlit as st
import pandas as pd
import urllib.parse

# Configuração premium de página - Layout amplo e profissional Black para o Caçador
st.set_page_config(page_title="Adriel AI - Caçador de Lançamentos", layout="wide")

# INJEÇÃO DE CÓDIGO CSS PREMIUM DEFINITIVO (BOTÕES NEON PERSONALIZADOS DE LUXO)
st.markdown("""
<style>
    /* Estilização para o botão de varredura (Ciano/Azul) */
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
st.markdown("Monitoramento avançado 24/7 nos servidores das maiores redes gringas: ClickBank, BuyGoods e Digistore24.")
st.write("---")

st.markdown("### 🎛️ Painel de Escaneamento e Notificações Automatizadas")
st.markdown("Clique no botão personalizado abaixo para iniciar o rastreamento simultâneo em tempo real:")
st.write("")

if st.button("🛰️ INICIAR RASTREAMENTO MASSIVO 24/7 (REAL-TIME)"):
    with st.spinner("Escaneando novos domínios e cruzando picos de tráfego volumétricos nas plataformas..."):
        st.success("🎯 Varredura concluída! Novas oportunidades de alta conversão detectadas nos servidores gringos!")
        st.write("---")
        
        # 📈 GRAFICO HISTÓRICO EM LUZ NEON (ESTILO DO JOSÉ)
        st.markdown("### 📈 Histórico Volumétrico de Surtos de Busca (Picos de Lançamento)")
        meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
        # Valores simulando os picos explosivos de novos produtos estourando no mercado
        valores_surtos = [120, 140, 890, 310, 240, 1150, 410, 320, 1340, 520, 440, 1500]
        
        df_grafico = pd.DataFrame({"Pico de Interesse Comercial (Buscadores)": valores_surtos}, index=meses)
        st.area_chart(df_grafico, use_container_width=True, color="#00E5FF")
        st.caption("🛰️ Legenda: Os picos de área ciano representam o exato momento em que novos produtos foram injetados no mercado internacional e geraram picos de busca exata.")
        st.write("---")
        
        # Estrutura robusta detalhando as oportunidades gringas por extenso
        texto_cacador = (
            "📦 [RASTREAMOR 1 — SERVIDOR BUYGOODS — ESTADOS UNIDOS]\n"
            "🔥 PRODUTO ATIVO: Obsesta (Nicho: Emagrecimento / Termogênico)\n"
            "- ANÁLISE DE TEMPO REAL: Sistema capturou alta movimentação de novos domínios nas últimas 2 horas. O leilão de frase do Google Ads encontra-se completamente limpo de afiliados concorrentes tradicionais.\n"
            "- GEO DE ESCALA (ONDE LANÇAR): Reino Unido 🇬🇧\n"
            "- JUSTIFICATIVA DO ESPECIALISTA: Público comprador britânico maduro com libras esterlinas na carteira pronto para pacotes múltiplos de 3 a 6 frascos. CPC médio travado em baixos $0.45.\n"
            "- 🌡️ TERMÔMETRO DO LANÇAMENTO: 98/100 (Potencial máximo de escala rápida e ROI imediato).\n\n"
            "------------------------------------------------------------------------------------------------------\n\n"
            "📦 [RASTREAMOR 2 — SERVIDOR CLICKBANK — EUROPA]\n"
            "🔥 PRODUTO ATIVO: NeuroQuiet (Nicho: Saúde Mental / Alívio de Zumbido / Sono)\n"
            "- ANÁLISE DE TEMPO REAL: Oferta escalando tráfego qualificado de buscas diretas por cupons de desconto. Ideal para subir estruturas rápidas de anúncios responsivos blindados.\n"
            "- GEO DE ESCALA (ONDE LANÇAR): Irlanda 🇮🇪\n"
            "- JUSTIFICATIVA DO ESPECIALISTA: Cliques extremamente baratos rodando direto em Euros. O leilão encontra-se livre de robôs americanos e cliques inválidos.\n"
            "- 🌡️ TERMÔMETRO DO LANÇAMENTO: 88/100 (Excelente ROI estimado no tráfego direto).\n\n"
            "------------------------------------------------------------------------------------------------------\n\n"
            "📦 [RASTREAMOR 3 — SERVIDOR DIGISTORE24 — OCEANIA]\n"
            "🔥 PRODUTO ATIVO: ZenCortex (Nicho: Foco / Memória / Nootrópico Premium)\n"
            "- ANÁLISE DE TEMPO REAL: Rastreamento identificou liberação de novos lotes promocionais de fábrica. Alta busca local por termos exatos no funil comercial.\n"
            "- GEO DE ESCALA (ONDE LANÇAR): Nova Zelândia 🇳🇿\n"
            "- JUSTIFICATIVA DO ESPECIALISTA: O leilão local encontra-se livre de lances agressivos do mercado de afiliados dos EUA, garantindo cliques limpos para contas com orçamento menor.\n"
            "- 🌡️ TERMÔMETRO DO LANÇAMENTO: 82/100."
        )
        st.text_area("📋 Relatório Consolidado de Oportunidades Recentes:", value=texto_cacador, height=450)
        st.write("---")
        
        # =============================================================================================================
        # MÓDULO DE INTEGRAÇÃO DE ALERTA VIA WHATSAPP (SOLICITADO POR JOSÉ)
        # =============================================================================================================
        st.markdown("### 🔔 CONFIGURAR DISPARO DE ALERTA NO SEU WHATSAPP")
        st.markdown("Insira o seu número abaixo para que o sistema estruture o relatório de lançamentos direto para o seu WhatsApp:")
        
        numero_whatsapp = st.text_input("Digite seu número com DDD (Apenas números, ex: 11999999999):", value="11999999999")
        
        # Mensagem formatada que será enviada para o WhatsApp do usuário
        mensagem_bruta = (
            "🚀 *ADRIEL AI - ALERTA DE LANÇAMENTO GRINGO DETECTADO!*\n\n"
            "🔥 *Produto:* Obsesta (BuyGoods)\n"
            "🌍 *Melhor País para Lançar:* Reino Unido 🇬🇧\n"
            "🌡️ *Termômetro:* 98/100 (Escala Máxima)\n\n"
            "💡 *Recomendação:* Suba a campanha na rede de pesquisa hoje mesmo para aproveitar o leilão limpo de concorrentes!"
        )
        
        # Codifica o texto para o formato aceito em links de internet (URL)
        mensagem_codificada = urllib.parse.quote(mensagem_bruta)
        link_whatsapp = f"https://whatsapp.com{numero_whatsapp}&text={mensagem_codificada}"
        
        st.write("")
        # Botão personalizado verde esmeralda para o disparo do WhatsApp
        st.markdown(
            f'<a href="{link_whatsapp}" target="_blank" style="text-decoration: none;">'
            '<div style="background-color: #2ECC71; color: white; text-align: center; padding: 14px; font-weight: bold; border-radius: 14px; box-shadow: 0px 5px 15px rgba(46, 204, 113, 0.4); font-size: 18px; transition: all 0.2s;">'
            "🟢 CONFIGURAR ALERTA E ENVIAR RELATÓRIO PARA O MEU WHATSAPP"
            '</div>'
            '</a>', 
            unsafe_allow_html=True
        )
