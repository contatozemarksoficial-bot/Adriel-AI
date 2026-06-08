import streamlit as st
import time

# Configuração premium de layout amplo Black para a Área de Assinantes
st.set_page_config(page_title="Adriel AI - Área de Assinantes", layout="wide")

# INJEÇÃO DE CÓDIGO CSS PREMIUM DEFINITIVO (BOTÕES CRESCENTES E CARDS DE LUXO)
st.markdown("""
<style>
    /* 🚀 BOTÕES CRESCENTES COM EFEITO FLUTUANTE (ZOOM AUTOMÁTICO) */
    div.stButton > button {
        background: linear-gradient(135deg, #050811 0%, #111b35 100%) !important;
        color: #00FF87 !important;
        border: 2px solid #00E5FF !important;
        font-size: 16px !important;
        font-weight: bold !important;
        padding: 12px 25px !important;
        border-radius: 12px !important;
        box-shadow: 0px 4px 10px rgba(0, 229, 255, 0.1) !important;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
        width: 100% !important;
        cursor: pointer !important;
    }
    
    /* 🔥 O EFEITO CRESCENTE QUANDO O MOUSE PASSA POR CIMA */
    div.stButton > button:hover {
        background: linear-gradient(135deg, #00FF87 0%, #00E5FF 100%) !important;
        color: #050811 !important;
        transform: scale(1.05) translateY(-2px) !important;
        box-shadow: 0px 8px 25px rgba(0, 255, 135, 0.5) !important;
    }
    
    /* Estilização para as Tabelas/Cards de Planos */
    .plano-card {
        background: #111b35;
        border: 2px solid #00E5FF;
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0px 4px 15px rgba(0, 229, 255, 0.1);
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

st.title("💎 MÓDULO 7: GESTÃO DE MEMBROS & PLANOS DE ASSINATURA")
st.markdown("Gerencie os planos de acesso recorrente do seu SaaS e configure os gateways de pagamento dos seus clientes.")
st.write("---")

# 🤖 O Robô Adriel AI se apresentando na tela de membros
st.markdown("""
<div style='background: #1e1e24; border-left: 5px solid #00E5FF; padding: 15px; border-radius: 10px; margin-bottom: 25px;'>
    <h4 style='color: #00E5FF; margin-top:0; margin-bottom: 5px;'>🤖 DIRETRIZ DO ROBÔ: MODELO DE MONETIZAÇÃO</h4>
    <p style='color: #e0e0e0; margin: 0; font-size: 15px;'>
        "José, organizei a tabela de planos crescentes de forma estratégica. O cliente visualiza os benefícios de cada pacote e o botão acende com efeito neon para garantir a conversão da assinatura!"
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("### 📊 TABELA DE PLANOS RECORRENTES (MENSALIDADES)")
st.write("")

# Criação de 3 colunas para colocar os planos lado a lado na tela
col_p1, col_p2, col_p3 = st.columns(3)

with col_p1:
    st.markdown("""
    <div class="plano-card">
        <h2 style='color: #ffffff; margin: 0;'>🌱 PLANO START</h2>
        <p style='color: #00E5FF; font-size: 14px;'>Para Iniciantes</p>
        <hr style='border-color: #00E5FF;'>
        <h1 style='color: #00FF87; margin: 10px 0;'>R$ 97<span style='font-size: 18px; color: white;'>/mês</span></h1>
        <p style='text-align: left; color: #e0e0e0; font-size: 14px;'>
            • Acesso ao Radar de Produtos<br>
            • Acesso ao Auditor de Mercado<br>
            • Validação Base de Infoprodutos<br>
            • Suporte por E-mail
        </p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Assinar Plano Start ➔", key="btn_start"):
        st.success("Redirecting para o Checkout de R$ 97,00...")

with col_p2:
    st.markdown("""
    <div class="plano-card" style="border-color: #00FF87; box-shadow: 0px 4px 20px rgba(0, 255, 135, 0.2);">
        <h2 style='color: #ffffff; margin: 0;'>🚀 PLANO PRO</h2>
        <p style='color: #00FF87; font-size: 14px; font-weight: bold;'>O MAIS VENDIDO ⭐</p>
        <hr style='border-color: #00FF87;'>
        <h1 style='color: #00FF87; margin: 10px 0;'>R$ 147<span style='font-size: 18px; color: white;'>/mês</span></h1>
        <p style='text-align: left; color: #e0e0e0; font-size: 14px;'>
            • <b>TUDO</b> do Plano Start<br>
            • Gerador de Anúncios (RSA)<br>
            • Caçador Ativo no WhatsApp<br>
            • Construtor Pre-Sell Hostinger
        </p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Assinar Plano Pro ➔", key="btn_pro"):
        st.success("Redirecting para o Checkout de R$ 147,00...")

with col_p3:
    st.markdown("""
    <div class="plano-card">
        <h2 style='color: #ffffff; margin: 0;'>🔥 PLANO ELITE</h2>
        <p style='color: #00E5FF; font-size: 14px;'>Acesso Total API</p>
        <hr style='border-color: #00E5FF;'>
        <h1 style='color: #00FF87; margin: 10px 0;'>R$ 297<span style='font-size: 18px; color: white;'>/mês</span></h1>
        <p style='text-align: left; color: #e0e0e0; font-size: 14px;'>
            • <b>TUDO</b> do Plano Pro<br>
            • Ativador Google Ads API Real<br>
            • Scanner de Políticas Integrado<br>
            • Suporte VIP Individual Mentoria
        </p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Assinar Plano Elite ➔", key="btn_elite"):
        st.success("Redirecting para o Checkout de R$ 297,00...")

st.write("---")
st.markdown("### ⚙️ CONFIGURAÇÃO DO GATEWAY DE PAGAMENTO (INTEGRAÇÃO DONO DO SOFTWARE)")
st.caption("Insira suas chaves de API da Kiwify, Hotmart ou Stripe para receber os pagamentos diretamente na sua conta bancária:")

col_g1, col_g2 = st.columns(2)
with col_g1:
    st.text_input("Token de Produção (Client Secret):", value="KIWIFY_SECRET_TOKEN_PRODUCTION", type="password")
with col_g2:
    st.selectbox("Selecione o Gateway Ativo:", ["Kiwify", "Stripe", "Appmax", "Hotmart"])

if st.button("💾 SALVAR CONFIGURAÇÕES DO GATEWAY", key="btn_save_gate"):
    st.success("✅ Chaves de pagamento salvas e integradas com sucesso na nuvem do Adriel AI!")
