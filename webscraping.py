import requests #importacao da biblioteca resquests.
from bs4 import BeautifulSoup   #importacao da biblioteca Beautifulsoup.

getMetas= requests.get('https://enttry.com.br/contato')  #fazendo request da pagina.
get_soup= BeautifulSoup(getMetas.text, 'html.parser')    #definindo as configuracoes da pagina.
for link in get_soup.findAll('meta'):   #uma condicao quando encontrar a palavra meta.
    print(link.get('name')) #printar o nome daquela meta.
    print(link.get('content'))  #printar o conteudo daquela meta.
