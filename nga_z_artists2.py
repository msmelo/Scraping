# Importar bibliotecas
import requests
import csv
from bs4 import BeautifulSoup

# Criar um arquivo para gravar, adicionar linha de cabeçalhos
f = csv.writer(open('z-artist-names.csv', 'w'))
f.writerow(['Name','Link'])

# Coletar a primeira página da lista de artistas
pages = []

for i in range(1,5):
    url = 'https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ' + str(i) + '.htm'
    pages.append(url)

for items in pages:
    page = requests.get(item)
    # Criar o objeto BeautifulSoup
    soup = BeautifulSoup(page.text, 'html.parser')

    last_links = soup.find(class_='AlphaNav')
    last_links.decompose()

    # Pegar todo o texto da div BodyText
    artist_name_list = soup.find(class_='BodyText')

    # Pegar o texto de todas as instâncias da tag <a> dentro da div BodyText
    artist_name_list_items = artist_name_list.find_all('a')

    # Criar loop para imprimir todos os nomes de artistas
    for artist_name in artist_name_list_items:
        names = artist_name.contents[0]
        links = 'https://web.archive.org' + artist_name.get('href')
        #print(names)
        #print(links)
        # Adicionar em uma linha o nome de cada artista e o link associado
        f.writerow([names,links])
