# Bibliotecas do Python
from typing import Text
import requests
from requests.models import Response
from bs4 import BeautifulSoup
import pandas as pd

lista_de_compras = []

# Site de Pesquisa
url_base = 'https://lista.mercadolivre.com.br/'

# Entrada do Produto(INPUT)
produto_nome = input('Qual produto você deseja? ')

# Requisição 
response = requests.get(url_base + produto_nome) 

# Tratamento das informaçoes
site = BeautifulSoup(response.text, 'html.parser')

# Rastreando a posição no html
produtos = site.findAll('div', attrs={'ui-search-result__wrapper'})


# Varrendo todos Produtos do site

for produto in produtos:

    titulo = produto.find('h2', attrs={'class': 'ui-search-item__title'})

    link = produto.find('a', attrs={'class': 'ui-search-link'})

    real = produto.find('span', attrs={'class': 'price-tag-symbol'})

    valor = produto.find('span', attrs={'class': 'price-tag-fraction'})

    centavos = produto.find('span', attrs={'class': 'price-tag-cents'})

    #     Nome e link do Produto
    #print('Titulo do produto:', titulo.text)
    #print('Link do Produto:', link['href'])

    #Toamda de decisão se o produto nao tiver centavos
    if (centavos):
        lista_de_compras.append([titulo.text, real.text, valor.text, centavos.text, link['href']])
    else:
       lista_de_compras.append([titulo.text, link.text, valor.text])
        
remedio = pd.DataFrame(lista_de_compras, columns=['Titulo','real', 'valor', 'centavos','link'])
 
remedio.to_excel('nomeParaaqrquivo.xlsx', index=False)