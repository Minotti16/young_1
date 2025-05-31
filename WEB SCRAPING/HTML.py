import requests
from bs4 import BeautifulSoup

url = 'https://br.ign.com/'
page = requests.get(url)


soup = BeautifulSoup(page.content, 'html.parser')

lista = ['samsung', 'nintendo','pokémon', 'the witcher 3']

for paragrafo in soup.find_all('body'):
    for palavra in lista:
        for paragrafo_str in paragrafo.stripped_strings:
            if palavra.upper() in str (paragrafo_str).upper():
                print('NOTA SOBRE', palavra.upper(), '\n', paragrafo_str, '\n' )
                break
