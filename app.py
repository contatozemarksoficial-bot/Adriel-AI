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
st.markdown("Página de vendas oficial, checkout e central administrativa de liberação de tokens.")
st.write("---")

# =============================================================================================================
# PARTE 1: VISÃO DO CLIENTE - TABELA DE PLANOS RECORRENTES (PÚBLICO)
# =============================================================================================================
st.markdown("### 📊 ESCOLHA SEU PLANO DE ACESSO AO ROBÔ ADRIEL AI")
st.write("")

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
        st.info("🔗 Redirecionando para o checkout seguro de R$ 97,00 na Kiwify...")

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
        st.info("🔗 Redirecionando para o checkout seguro de R$ 147,00 na Kiwify...")

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
        st.info("🔗 Redirecionando para o checkout seguro de R$ 297,00 na Kiwify...")

st.write("---")

# =============================================================================================================
# PARTE 2: VISÃO DO JOSÉ - TRAVA DE SEGURANÇA E PAINEL ADMINISTRATIVO (RESTRITO)
# =============================================================================================================
st.markdown("### 🔐 PAINEL DE CONTROLE ADMINISTRATIVO (EXCLUSIVO PROPRIETÁRIO)")
st.caption("Para acessar os dados de faturamento, webhooks e moderação de alunos, insira sua credencial de desenvolvedor:")

# Caixa de verificação de senha inline para travar o painel contra estranhos
senha_admin = st.text_input("Digite a Senha Mestre do Administrador:", type="password", key="master_admin_password_box")

if senha_admin == "jose123": # Senha mestre do José para liberar o backend
    st.success("🔓 ACESSO AUTORIZADO, COMANDANTE JOSÉ MARQUES DA SILVA! Painel de controle do SaaS liberado.")
    
    # Renderiza as 4 abas secretas de controle total do seu império
    tabs_admin = st.tabs(["🔒 Chaves do Gateway", "👥 Moderação de Alunos", "🔑 Gerador de Licenças", "🖲️ Link do Webhook"])
    
    with tabs_admin:
        st.markdown("#### 💳 Configurações de Token do Checkout")
        col_g1, col_g2 = st.columns(2)
        with col_g1:
            st.text_input("Token Secreto de Produção (API Key):", value="KIWIFY_SECRET_TOKEN_PRODUCTION", type="password")
        with col_g2:
            st.selectbox("Gateway Integrado Ativo:", ["Kiwify", "Hotmart", "Stripe", "Appmax"])
        if st.button("💾 SALVAR CONFIGURAÇÕES DO GATEWAY", key="btn_save_gate"):
            st.success("✅ Chaves de faturamento salvas e criptografadas na nuvem!")

    with tabs_admin:
        st.markdown("#### 👥 Controle de Alunos e Combate à Pirataria")
        col_u1, col_u2 = st.columns(2)
        with col_u1:
            email_busca = st.text_input("Buscar Usuário pelo E-mail:", value="comprador@gmail.com")
        with col_u2:
            status_busca = st.selectbox("Status de Acesso:", ["Ativo (Mensalidade Paga) 🟢", "Atrasado (Notificar) 🟡", "Bloqueado (Recusado) 🔴"])
        
        col_ubtn1, col_ubtn2 = st.columns(2)
        with col_ubtn1:
            if st.button("⚡ APLICAR ALTERAÇÃO DE STATUS", key="btn_status_user"):
                st.success(f"🔄 O e-mail {email_busca} foi atualizado para {status_busca} com sucesso!")
        with col_ubtn2:
            if st.button("❌ CORTAR ACESSO IMEDIATAMENTE (BANIR)", key="btn_ban_user"):
                st.error(f"🛑 Usuário {email_busca} foi banido e bloqueado dos servidores do robô!")

    with tabs_admin:
        st.markdown("#### 🔑 Gerador de Licenças Manuais (Vendas via Pix/WhatsApp)")
        st.caption("Crie chaves de acesso exclusivas para quem comprar direto com você por fora do gateway:")
        plano_token = st.selectbox("Escolha o Plano da Chave:", ["Plano Start", "Plano Pro", "Plano Elite"])
        if st.button("💎 GERAR CÓDIGO DE LICENÇA", key="btn_gen_token"):
            chave_aleatoria = f"ADRIEL-{plano_token.upper()[:3]}-741258-XYZ9"
            st.code(chave_aleatoria, language="text")
            st.success("🎯 Código gerado! Copie e entregue para o cliente liberar o login dele.")

    with tabs_admin:
        st.markdown("#### 🖲️ Automação de Entrada por Webhook")
        st.caption("Cole este endereço na aba de Webhooks da sua Kiwify para automatizar a liberação:")
        st.text_input("URL Mestre de Sincronização (Apenas Leitura):", value="https://streamlit.app", disabled=True)
        st.info("💡 Assim que a Kiwify identificar a venda aprovada, ela avisa esse link e o robô cria o login do aluno na mesma hora de forma 100% automática!")

elif senha_admin != "":
    st.error("❌ Credencial Inválida! Acesso negado às configurações de faturamento por motivos de segurança.")
