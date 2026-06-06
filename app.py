def executar_presell(produto):
    try:
        model = genai.GenerativeModel(modelo_ativo)
        prompt = f"Pre-sell structure for {produto}"
        resposta = model.generate_content(prompt)
        return resposta.text
    except Exception:
        return f"""
        [HEADLINE SECURE]
        Special Discount Package on the Official Website Today!
        
        [SUBHEADLINE]
        Get the Authentic {produto} Formula Directly from the Manufacturer.
        
        [LOCAL DELIVERY]
        Available for United Kingdom Delivery 🇬🇧 - Fast Shipping Options.
        
        [AFFILIATE DISCLAIMER]
        *This website is an independent review site and receives compensation from product links.
        """
