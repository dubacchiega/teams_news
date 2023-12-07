import requests
from bs4 import BeautifulSoup

condition = True
while condition: 
    print('De qual time você gostaria de saber as notícias de hoje?')
    print("""
        1 - América-MG 
        2 - Athletico-PR 
        3 - Atlético-MG 
        4 - Bahia 
        5 - Botafogo 
        6 - Corinthians 
        7 - Coritiba 
        8 - Cruzeiro 
        9 - Cuiabá 
        10 - Flamengo 
        11 - Fluminense 
        12 - Fortaleza 
        13 - Goiás 
        14 - Grêmio 
        15 - Internacional 
        16 - Palmeiras 
        17 - Red Bull Bragantino 
        18 - Santos 
        19 - São Paulo
        20 - Vasco""")
    option = input('Digite a opção de time que queira saber a notícia: ')
    print()

    try:
        option = int(option)

    except ValueError:
        print('Digite apenas números')
        continue

    if option > 20 or option <= 0:
        print('Número não encontrado')
        continue
    condition = False

class Team():
    def __init__(self, option:int) -> None:
        self.option = option

    def team(self):
        match self.option:
            case 1:
                team_url = 'america-mg'
                return team_url
            case 2:
                team_url = 'athletico-pr'
                return team_url
            case 3:
                team_url = 'atletico-mg'
                return team_url
            case 4:
                team_url = 'bahia'
                return team_url
            case 5:
                team_url = 'botafogo'
                return team_url
            case 6:
                team_url = 'corinthians'
                return team_url    
            case 7:
                team_url = 'coritiba'
                return team_url
            case 8:
                team_url = 'cruzeiro'
                return team_url
            case 9:
                team_url = 'cuiaba'
                return team_url
            case 10:
                team_url = 'flamengo'
                return team_url
            case 11:
                team_url = 'fluminense'
                return team_url
            case 12:
                team_url = 'fortaleza'
                return team_url
            case 13:
                team_url = 'goias'
                return team_url
            case 14:
                team_url = 'gremio'
                return team_url
            case 15:
                team_url = 'internacional'
                return team_url
            case 16:
                team_url = 'palmeiras'
                return team_url
            case 17:
                team_url = 'red-bull-bragantino'
                return team_url
            case 18:
                team_url = 'santos'
                return team_url
            case 19:
                team_url = 'sao-paulo'
                return team_url
            case 20:
                team_url = 'vasco'
                return team_url

class TeamsNews:

    def __init__(self, url):
        self.url = url

    def scraping_news(self):
        response = requests.get(self.url)
        raw_html = response.text

        parsed_html = BeautifulSoup(raw_html, 'html.parser')

        filter_html = parsed_html.select_one(
            'body > section.collection-index').text  #type: ignore

        filter_html = filter_html.split('          ')
        print(f'---Notícias do {complete_url.upper()}---') #type: ignore
        print()
        for i, news in enumerate(filter_html):
            if i != 0:
                print(f'{i}) {news.strip()}')
                print()

if __name__ == '__main__':
    team = Team(option) #type:ignore
    complete_url = team.team()
    scraping_news = f'https://www.uol.com.br/esporte/futebol/times/{complete_url}/'
    team_news = TeamsNews(scraping_news)
    team_news.scraping_news()