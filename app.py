import streamlit as st
import pandas as pd
import time

# Configuração de Layout Amplo Premium Black para a Entrada do SaaS
st.set_page_config(page_title="Adriel AI - Core Dashboard", layout="wide", initial_sidebar_state="expanded")

# =============================================================================================================
# INJEÇÃO DE ÁUDIO REAL VIA JAVASCRIPT (O ROBÔ FALA AO CLICAR NA TELA)
# =============================================================================================================
texto_boas_vindas = "Olá, Comandante José Marques da Silva! O núcleo de Inteligência Artificial tridimensional está ativo nos servidores do Adriel A I. Handshake concluído."

st.markdown(f"""
<script>
    document.addEventListener('click', function() {{
        if (!window.audioDisparado) {{
            var msg = new SpeechSynthesisUtterance();
            msg.text = "{texto_boas_vindas}";
            msg.lang = "pt-BR";
            msg.rate = 1.0;
            msg.pitch = 0.85;
            window.speechSynthesis.speak(msg);
            window.audioDisparado = true;
        }}
    }});
</script>
""", unsafe_allow_html=True)

# =============================================================================================================
# INJEÇÃO DE CÓDIGO CSS PREMIUM DE ELITE (ESTILO BLACK E PISCADO NEON DO MENU)
# =============================================================================================================
st.markdown("""
<style>
    /* 🌌 Fundo Escuro de Luxo */
    .stApp {
        background-color: #050811 !important;
        color: #ffffff !important;
    }
    
    /* 📟 Customização da Barra Lateral Esquerda */
    [data-testid="stSidebar"] {
        background-color: #02040a !important;
        border-right: 1px solid #1e293b !important;
    }
    
    /* 🚨 ANIMAÇÃO PULSAR DO MENU LATERAL */
    @keyframes pulsa-neon {
        0% { border-color: #1e293b; box-shadow: 0 0 5px rgba(0, 229, 255, 0.1); }
        50% { border-color: #00FF87; box-shadow: 0 0 15px rgba(0, 255, 135, 0.4); }
        100% { border-color: #1e293b; box-shadow: 0 0 5px rgba(0, 229, 255, 0.1); }
    }

    [data-testid="stSidebarNav"] ul li a span {
        color: #ffffff !important; 
        font-weight: bold !important;
        font-size: 14px !important;
    }
    
    [data-testid="stSidebarNav"] ul li a {
        background-color: #0f172a !important; 
        border: 2px solid #1e293b !important;
        border-radius: 8px !important;
        margin-bottom: 8px !important;
        padding: 12px 14px !important;
        animation: pulsa-neon 3s infinite ease-in-out !important;
        display: block !important;
    }
    
    /* 🎨 ANIMAÇÃO DA CAIXA DE BOAS-VINDAS (ALTERNA CIANO <-> VERDE) */
    @keyframes alterna-cores {
        0% { border-color: #00E5FF; box-shadow: 0px 8px 32px rgba(0, 229, 255, 0.2); }
        50% { border-color: #00FF87; box-shadow: 0px 8px 32px rgba(0, 255, 135, 0.3); }
        100% { border-color: #00E5FF; box-shadow: 0px 8px 32px rgba(0, 229, 255, 0.2); }
    }

    .robo-card-welcome {
        background: linear-gradient(135deg, #0f172a 0%, #050811 100%) !important;
        border: 2px solid #00E5FF !important;
        border-radius: 16px !important;
        padding: 25px !important;
        margin-bottom: 25px !important;
        animation: alterna-cores 5s infinite ease-in-out !important;
    }
    
    /* Bloco dos Cards de Status */
    .status-card {
        background-color: #0f172a !important;
        border: 1px solid #1e293b !important;
        border-radius: 12px !important;
        padding: 20px !important;
        text-align: center;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.3) !important;
    }
</style>
""", unsafe_allow_html=True)

# =============================================================================================================
# 🦾 NÚCLEO REAL DE INTELIGÊNCIA ARTIFICIAL: AMBIENTE 3D ANIMADO EM CANVAS HTML5 / JS DIRECT
# =============================================================================================================
st.markdown("### 🧬 NÚCLEO DINÂMICO DE PROCESSAMENTO DA IA")

html_robo_real = """
<div style="text-align: center; background: #070c16; padding: 20px; border-radius: 16px; border: 1px solid #1e293b; box-shadow: 0px 10px 40px rgba(0,0,0,0.5);">
    <canvas id="canvasRobo3D" width="800" height="260" style="background: transparent; max-width: 100%;"></canvas>
</div>

<script>
    const canvas = document.getElementById('canvasRobo3D');
    const ctx = canvas.getContext('2d');
    let angulo = 0;

    function desenharIA() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        const centroX = canvas.width / 2;
        const centroY = canvas.height / 2;
        
        // 1. Renderização das Partículas de Dados e Conectividade ao redor do Robô
        angulo += 0.015;
        ctx.strokeStyle = '#00E5FF';
        ctx.lineWidth = 1.5;
        
        // Círculo Holográfico Externo Transmitindo Lotes
        ctx.beginPath();
        ctx.arc(centroX, centroY, 110, 0, Math.PI * 2);
        ctx.setLineDash([15, 25]);
        ctx.stroke();
        
        // Anel Interno em Rotação Inversa (Verde Neon)
        ctx.strokeStyle = '#00FF87';
        ctx.beginPath();
        ctx.arc(centroX, centroY, 90, angulo, angulo + Math.PI, false);
        ctx.setLineDash([40, 30]);
        ctx.stroke();

        ctx.beginPath();
        ctx.arc(centroX, centroY, 90, angulo + Math.PI, angulo, false);
        ctx.stroke();
        ctx.setLineDash([]); // Reseta traço

        // 2. CHASSI DO ROBÔ HUMANOIDE (Mapeamento Vetorial Complexo)
        ctx.fillStyle = '#ffffff';
        ctx.strokeStyle = '#00E5FF';
        ctx.lineWidth = 3;
        
        // Cabeça
        ctx.beginPath();
        ctx.roundRect(centroX - 25, centroY - 80, 50, 55, 15);
        ctx.fill();
        ctx.stroke();
        
        // Orelhas / Sensores Dinâmicos
        ctx.fillStyle = '#0f172a';
        ctx.beginPath();
        ctx.roundRect(centroX - 33, centroY - 65, 8, 25, 4);
        ctx.roundRect(centroX + 25, centroY - 65, 8, 25, 4);
        ctx.fill();
        ctx.stroke();
        
        // Olhos Acesos de LED (Pulsando)
        let brilhoLed = Math.abs(Math.sin(angulo * 2));
        ctx.fillStyle = `rgba(0, 229, 255, ${brilhoLed * 0.7 + 0.3})`;
        ctx.beginPath();
        ctx.arc(centroX - 12, cy = centroY - 55, 5, 0, Math.PI * 2);
        ctx.arc(centroX + 12, cy, 5, 0, Math.PI * 2);
        ctx.fill();
        
        // Boca Eletrônica de Grade Criptografada
        ctx.fillStyle = '#00FF87';
        ctx.fillRect(centroX - 10, centroY - 40, 20, 3);
        
        // Pescoço
        ctx.fillStyle = '#334155';
        ctx.fillRect(centroX - 10, centroY - 25, 20, 10);
        
        // Peito / Armadura do Torso
        ctx.fillStyle = '#ffffff';
        ctx.beginPath();
        ctx.moveTo(centroX - 45, centroY - 15);
        ctx.lineTo(centroX + 45, centroY - 15);
        ctx.lineTo(centroX + 35, centroY + 65);
        ctx.lineTo(centroX - 35, centroY + 65);
        ctx.closePath();
        ctx.fill();
        ctx.stroke();
        
        // Reator / Núcleo de Energia (Pulsando em Verde Neon)
        ctx.fillStyle = '#0f172a';
        ctx.beginPath();
        ctx.roundRect(centroX - 15, centroY, 30, 40, 6);
        ctx.fill();
        ctx.stroke();
        
        ctx.fillStyle = `rgba(0, 255, 135, ${brilhoLed})`;
        ctx.beginPath();
        ctx.arc(centroX, centroY + 20, 8, 0, Math.PI * 2);
        ctx.fill();
        
        // 3. BRAÇOS CONECTADOS DIRETAMENTE NAS TELAS LATERAIS DA FOTO
        ctx.lineWidth = 12;
        ctx.strokeStyle = '#ffffff';
        ctx.lineCap = 'round';
        ctx.lineJoin = 'round';
        
        // Braço Esquerdo Operando Painel de Dados
        ctx.beginPath();
        ctx.moveTo(centroX - 45, centroY - 10);
        ctx.lineTo(centroX - 100, centroY + 15);
        ctx.lineTo(centroX - 180, centroY - 15);
        ctx.stroke();
        
        // Braço Direito Operando Esfera
        ctx.beginPath();
        ctx.moveTo(centroX + 45, centroY - 10);
        ctx.lineTo(centroX + 100, centroY + 15);
        ctx.lineTo(centroX + 180, centroY - 15);
        ctx.stroke();
        
        // Acabamento interno dos braços (Preto Tecnológico)
        ctx.lineWidth = 4;
        ctx.strokeStyle = '#0f172a';
        ctx.beginPath();
        ctx.moveTo(centroX - 45, centroY - 10);
        ctx.lineTo(centroX - 100, centroY + 15);
        ctx.lineTo(centroX - 180, centroY - 15);
        ctx.moveTo(centroX + 45, centroY - 10);
        ctx.lineTo(centroX + 100, centroY + 15);
        ctx.lineTo(centroX + 180, centroY - 15);
        ctx.stroke();
        
        // 4. PANÉIS HOLOGRÁFICOS SECUNDÁRIOS DA FOTO (LATERAIS)
        // Esquerda: Caixa de Monitoramento
        ctx.fillStyle = 'rgba(0, 229, 255, 0.1)';
        ctx.strokeStyle = '#00E5FF';
        ctx.lineWidth = 1;
        ctx.beginPath();
        ctx.roundRect(centroX - 280, centroY - 70, 90, 35, 5);
        ctx.fill();
        ctx.stroke();
        ctx.fillStyle = '#00E5FF';
        ctx.font = 'bold 11px sans-serif';
        ctx.fillText('CORE: SECURE', centroX - 270, centroY - 48);
        
        // Linhas de pulso ligando a mão do robô à tela
        ctx.strokeStyle = '#00E5FF';
        ctx.lineWidth = 1.5;
        ctx.beginPath();
        ctx.arc(centroX - 180, centroY - 15, 6, 0, Math.PI * 2);
        ctx.fillStyle = '#00E5FF';
        ctx.fill();
        
        // Direita: Esfera Tridimensional de Monitoramento
        ctx.strokeStyle = '#00FF87';
        ctx.beginPath();
        ctx.arc(centroX + 180, centroY - 15, 6, 0, Math.PI * 2);
        ctx.fillStyle = '#00FF87';
        ctx.fill();
        
        ctx.strokeStyle = '#00FF87';
        ctx.lineWidth = 1.5;
        ctx.setLineDash([5, 5]);
        ctx.beginPath();
        ctx.arc(centroX + 240, centroY + 20, 35, 0, Math.PI * 2);
        ctx.stroke();
