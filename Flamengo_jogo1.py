

## Decidi usar o request para raspagem por eu ter mais familiaridade.

import requests
import pandas as pd


page = requests.get('https://www.sofascore.com/pt/football/match/boavista-flamengo/GucsCOc#id:13198164')

url = "https://www.sofascore.com/api/v1/event/13198164/statistics"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0"
}

## Fazendo a primeira requisição para a URL da API

response = requests.get(url, headers=headers)
if response.status_code == 200:
    data = response.json()

    all_data = []
## Eu busquei usar o all_data para trabalhar os dados, logo após de conferir a URL da API.
    for match_stats in data['statistics']:
        period = match_stats['period']
        
        for group in match_stats.get('groups', []):
            group_name = group.get('groupName', 'Unknown')

        
            for item in group['statisticsItems']:
                stats_name = item.get('name')
                home_value = item.get('home')
                away_value = item.get('away')


## Aqui eu encontrei em uma pesquisa em como colocar em dicionários para tratar melhor o all_data quando convertesse em um dataframe
                all_data.append({
                    'Period': period,
                    'Group': group_name,
                    'Statistic': stats_name,
                    'Home': home_value,
                    'Away': away_value
                })

    df = pd.DataFrame(all_data)

    excel_file = 'flaxboavista_stats.xlsx'
    df.to_excel(excel_file, index=False)

    print(f'Dados exportados para {excel_file}')

    print(df)

    ## AS EXPLICAÇÕES DESSE CÓDIGO SERVE PARA TODOS OS OUTROS Flamengo_JogoX.py