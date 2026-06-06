import requests
from bs4 import BeautifulSoup

# Radar de Produtos
def radar_de_produtos(api_url):
    response = requests.get(api_url)
    produtos = response.json()
    top_produtos = sorted(produtos, key=lambda x: x['vendas'], reverse=True)[:10]
    outros_produtos = sorted(produtos, key=lambda x: x['concorrencia'])[10:30]
    
    return top_produtos, outros_produtos

# Auditor de Mercado
def auditor_de_mercado(nome_produto):
    # Aqui você poderia usar uma API ou um banco de dados para buscar informações
    info_produto = {
        'beneficios': 'Benefício 1, Benefício 2',
        'dores': 'Dor 1, Dor 2',
        'pais_recomendado': 'Brasil',
        'custo_por_clique': 0.5
    }
    return info_produto

# Gerador de Anúncios
def gerador_de_anuncios(nome_produto):
    titulo = f"Compre {nome_produto} Agora!"
    descricao = f"Descubra os benefícios de {nome_produto}."
    palavras_chave = [f'"{nome_produto} {i}"' for i in range(1, 16)]
    palavras_negativas = ["grátis", "promoção"]
    
    return {
        'titulo': titulo,
        'descricao': descricao,
        'palavras_chave': palavras_chave,
        'palavras_negativas': palavras_negativas
    }

# Caçador de Lançamentos
def cacador_de_lancamentos(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    lancamentos = []
    for item in soup.find_all('div', class_='lancamento'):
        lancamentos.append(item.text)
    
    return lancamentos

# Fabricante de Pre-sell
def fabricante_de_presell(nome_produto):
    url_compra = "https://www.example.com/" + nome_produto.replace(" ", "-")
    conteudo_presell = f"Página de pré-venda para {nome_produto}. Link para compra: {url_compra}"
    
    return conteudo_presell

# Configurações
class Configuracoes:
    def __init__(self):
        self.assinantes = []

    def adicionar_assinante(self, email):
        self.assinantes.append(email)

    def listar_assinantes(self):
        return self.assinantes

# Função principal para testar as funcionalidades
def main():
    # Teste do Radar de Produtos
    api_url = 'URL_DA_API_DE_PRODUTOS'
    top_produtos, outros_produtos = radar_de_produtos(api_url)
    print("Top 10 Produtos:", top_produtos)
    print("Outros Produtos:", outros_produtos)

    # Teste do Auditor de Mercado
    info = auditor_de_mercado('Nome do Produto')
    print("Informações do Produto:", info)

    # Teste do Gerador de Anúncios
    anuncio = gerador_de_anuncios('Produto Exemplo')
    print("Anúncio:", anuncio)

    # Teste do Caçador de Lançamentos
    lancamentos = cacador_de_lancamentos('URL_DOS_LANCAMENTOS')
    print("Lançamentos:", lancamentos)

    # Teste do Fabricante de Pre-sell
    presell = fabricante_de_presell('Produto Exemplo')
    print("Conteúdo de Pré-venda:", presell)

    # Teste de Configurações
    config = Configuracoes()
    config.adicionar_assinante('email@exemplo.com')
    print("Assinantes:", config.listar_assinantes())

if __name__ == "__main__":
    main()
