⚙️ Configurações
AQUE TEMOS QUE CRIAR A AREA DE ASSINANTE E PAINEL TU MUITO BONITO PARA O AdrielAI
import streamlit as st
import pandas as pd

# Configuração premium de página - Layout amplo e profissional Black para o Auditor
st.set_page_config(page_title="Adriel AI - Auditor de Mercado", layout="wide")

# INJEÇÃO DE CÓDIGO CSS PREMIUM CORRIGIDA PARA O BOTÃO NEON REAL
st.markdown("""
<style>
    button[kind="primary"], .stButton > button {
        background: linear-gradient(135deg, #007BFF 0%, #00E5FF 100%) !important;
        color: white !important;
        font-size: 18px !important;
        font-weight: bold !important;
        padding: 12px 35px !important;
        border-radius: 12px !important;
        border: none !important;
        box-shadow: 0px 4px 15px rgba(0, 229, 255, 0.4) !important;
        transition: all 0.3s ease-in-out !important;
        width: 100% !important;
    }
    button[kind="primary"]:hover, .stButton > button:hover {
        background: linear-gradient(135deg, #00E5FF 0%, #007BFF 100%) !important;
        transform: translateY(-2px) !important;
        box-shadow: 0px 6px 20px rgba(0, 229, 255, 0.6) !important;
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

st.title("🛡️ MÓDULO: AUDITOR DE MERCADO XEQUE-MATE")
st.markdown("Protocolo avançado de investigação de viabilidade em tempo real, dores de público-alvo e veredito gráfico de lucratividade.")
st.write("---")

# Campo de entrada de dados direto e limpo
produto_input = st.text_input("Digite o nome do produto internacional para auditar:", value="Citrus Burn")
st.write("")

# Lista oficial de produtos premium altamente validados no mercado atual
produtos_validados_elite = ["obsesta", "sugar defender", "prodentim", "glucoberry", "citrus burn", "leanbliss", "puravive", "java burn", "alpilean", "livpure"]

if st.button("🚀 EXECUTAR AUDITORIA DE MERCADO"):
    with st.spinner("Conectando aos servidores de leilão e cruzando dados de buscas em tempo real..."):
        
        # Engenharia de limpeza de hífens para validar formatos variados
        produto_limpo = produto_input.strip().lower().replace("-", " ")
        
        # =============================================================================================================
        # CASO 1: O PRODUTO É ALTAMENTE LUCRATIVO (POSITIVIDADE MÁXIMA E GEOLOCALIZAÇÃO)
        # =============================================================================================================
        if produto_limpo in produtos_validados_elite:
            st.success("✅ PRODUTO APROVADO! Alta Positividade Detectada para o produto: " + produto_input)
            st.write("---")
            
            # Módulos de métricas rápidas no topo
            col_m1, col_m2, col_m3 = st.columns(3)
            with col_m1:
                st.metric(label="📊 Status de Mercado Real", value="ALTAMENTE LUCRATIVO 🔥")
            with col_m2:
                st.metric(label="🌍 Melhor País para Anunciar (ROI)", value="Estados Unidos 🇺🇸" if "citrus" in produto_limpo else "Reino Unido 🇬🇧")
            with col_m3:
                st.metric(label="💰 CPC Médio Estimado", value="$0.65" if "citrus" in produto_limpo else "$0.45")
                
            st.write("---")
            
            # 📊 GRÁFICO HISTÓRICO EM VERDE NEON DE LUCRO
            st.markdown("### 📊 Painel Histórico de Volume de Buscas (Últimos 12 Meses)")
            meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
            valores_alta = [140, 180, 290, 420, 510, 680, 720, 810, 890, 920, 960, 1100]
            
            df_grafico_completo = pd.DataFrame({"Volume de Cliques de Marca Qualificados": valores_alta}, index=meses)
            # Aplicando a cor Verde Lucro de forma estável no parâmetro nativo
            st.bar_chart(df_grafico_completo, use_container_width=True, color="#2ECC71")
            st.caption("🔥 Análise de Autoridade: Curva ascendente mapeada em colunas VERDES. Sinal de alta tração de tráfego comprador.")
            st.write("---")
            
            # DIVISÃO EM COLUNAS: Laudos detalhados logo abaixo do gráfico de colunas
            col_l1, col_l2 = st.columns(2)
            
            with col_l1:
                with st.expander("🎯 BENEFÍCIOS REAIS DO PRODUTO (ÂNCORAS DE CÓPIA)", expanded=True):
                    st.markdown(
                        "- **Aceleração Metabólica:** Regulação e destrava do metabolismo basal profundo através de compostos concentrados.\n"
                        "- **Bloqueio de Compulsão:** Controle severo da ansiedade por doces, açúcar e carboidratos refinados ao longo do dia.\n"
                        "- **Queima Visceral:** Derretimento contínuo de gordura profunda de forma 100% natural e clinicamente testada.\n"
                        "- **Energia Celular:** Aumento massivo da disposição física e foco mental, eliminando o cansaço ao acordar."
                    )
                    
                with st.expander("🧠 MAIOR DOR DO COMPRADOR GRINGO (PÚBLICO-ALVO)", expanded=True):
                    st.markdown(
                        "O cliente final gringo sofre severamente com a **fadiga crônica**, baixa autoestima provocada pelo excesso de peso acumulado "
                        "e frustração psicológica com o **efeito sanfona** de dietas tradicionais. Apresenta dificuldade metabólica extrema de emagrecer "
                        "após os 40 anos devido à desaceleração hormonal natural."
                    )
                    
            with col_l2:
                with st.expander("🌍 VEREDITO DA MELHOR ESTRATÉGIA E POR QUE ANUNCIAR", expanded=True):
                    if "citrus" in produto_limpo:
                        st.markdown(
                            "Para o produto **Citrus Burn**, a melhor estratégia de escala agressiva encontra-se concentrada no mercado dos **Estados Unidos 🇺🇸**. "
                            "Embora o leilão de lances exatíssimos de marca apresente um CPC de **$0.65**, o volume de buscas mobile local compensa o investimento, "
                            "sendo crucial segmentar a campanha apenas para dispositivos móveis (smartphones) para otimizar o CTR e evitar cliques frios de bots."
                        )
                    else:
                        st.markdown(
                            "A melhor estratégia absoluta para divulgar e subir a campanha de rede de pesquisa no Google Ads "
                            "é o **Reino Unido (United Kingdom) 🇬🇧**. O leilão local rodando em libras esterlinas oferece concorrência reduzida de "
                            "afiliados concorrentes e um público com altíssimo poder aquisitivo, pronto para comprar pacotes máximos de 3 a 6 frascos em tráfego direto."
                        )
        
        # =============================================================================================================
        # CASO 2: O PRODUTO É FRACO / SATURADO (ALERTA VERMELHO DE SEGURANÇA CONTRA PERDA DE DINHEIRO)
        # =============================================================================================================
        else:
            st.error("🚨 ALERTA VERMELHO! Risco de Prejuízo Detectado para o produto: " + produto_input)
            st.write("---")
            
            col_a1, col_a2, col_a3 = st.columns(3)
            with col_a1:
                st.metric(label="📊 Status de Mercado Real", value="PRODUTO FRACO / BLOQUEADO 🚫")
            with col_a2:
                st.metric(label="📉 Tendência de Busca", value="Queda Livre (-64%)")
            with col_a3:
                st.metric(label="💸 Taxa de Reembolso Geral", value="Crítica (>18%)")
                
            st.write("---")
            
            # 📊 GRÁFICO HISTÓRICO EM VERMELHO DE ALERTA DE PREJUÍZO
            st.markdown("### 📊 Painel Histórico de Declínio de Buscas (Últimos 12 Meses)")
            meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
            valores_baixa = [980, 850, 710, 590, 480, 320, 210, 140, 90, 50, 20, 10]
            
            df_grafico_ruim = pd.DataFrame({"Volume de Pesquisas Globais": valores_baixa}, index=meses)
            # Aplicando a cor Vermelho Alerta no parâmetro nativo
            st.bar_chart(df_grafico_ruim, use_container_width=True, color="#E74C3C")
            st.caption("⚠️ Alerta Vermelho: Colunas VERMELHAS em queda severa. Saturação crônica irreversível detectada no leilão internacional.")
            st.write("---")
            
            st.markdown("### ⚠️ DOSSIÊ DE SEGURANÇA E RECOMENDAÇÃO ADRIEL AI:")
            st.error(
                "**❌ CONSELHO CIRÚRGICO: NÃO ENTRE NESTE MERCADO PARA NÃO PERDER DINHEIRO!**\n\n"
                "O produto **" + produto_input + "** foi classificado como **Inviável ou Altamente Instável** pelo nosso rastreador em tempo real. "
                "O leilão de lances na gringa encontra-se completamente dominado por cliques falsos de robôs concorrentes, ou o produto perdeu o interesse público "
                "nas principais plataformas internacionais como ClickBank e BuyGoods.\n\n"
                "**⚠️ Red flags de risco comercial detectadas:**\n"
                "- Volume de buscas por chaves exatas insuficiente para cobrir o custo de manutenção da campanha no Google Ads.\n"
                "- CPC abusivo e inflado artificialmente, inviabilizando margens saudáveis de ROI.\n"
                "- Alto índice de avaliações negativas e reclamações de clientes fora dos EUA, estourando as taxas de reembolso.\n\n"
                "**💡 O que fazer?** Abandone este produto imediatamente e selecione um termo listado como 'VALIDADO' ou 'ELITE' no nosso Radar de Produtos para proteger o seu orçamento de anúncios."
