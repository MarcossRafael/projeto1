

import requests
import pandas as pd

page = requests.get('https://www.sofascore.com/pt/football/match/flamengo-botafogo/iOsGuc#id:13198201')

url = "https://www.sofascore.com/api/v1/event/13198201/statistics"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0"
}

response = requests.get(url, headers=headers)
if response.status_code == 200:
    data = response.json()

    all_data = []

    # Percorre as estatísticas do jogo
    for match_stats in data['statistics']:
        period = match_stats['period']

        # Para cada grupo de estatísticas
        for group in match_stats.get('groups', []):
            group_name = group.get('groupName', 'Unknown')

            # Para cada item dentro do grupo de estatísticas
            for item in group['statisticsItems']:
                stats_name = item.get('name')
                home_value = item.get('home')
                away_value = item.get('away')

                all_data.append({
                    'Period': period,
                    'Group': group_name,
                    'Statistic': stats_name,
                    'Home': home_value,
                    'Away': away_value
                })

    # Converte os dados para um DataFrame
    df = pd.DataFrame(all_data)

    # Exporta para Excel
    excel_file = 'flaxbot_stats.xlsx'
    df.to_excel(excel_file, index=False)

    print(f'Dados exportados para {excel_file}')

    print(df)