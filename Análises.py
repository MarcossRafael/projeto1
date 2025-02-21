

import pandas as pd

df = pd.read_excel("flamengo_carioca_2025_corrigido.xlsx")

estatisticas_numericas = df[df["Statistic"].isin(["Expected goals", "Total shots", "Shots on Goalkeeper saves", "Corner kicks"])]

home_stats = estatisticas_numericas[estatisticas_numericas["Flamengo_Posicao"] == "Home"]
away_stats = estatisticas_numericas[estatisticas_numericas["Flamengo_Posicao"] == "Away"]


df_home = df[df['Flamengo_Posicao'] == 'Home']
df_away = df[df['Flamengo_Posicao'] == 'Away']

print("Estatisticas Numericas: ")
print(estatisticas_numericas)

print("\nEstatisticas quando Flamengo e home: ")
print(home_stats)

print("\nEstatistica quando Flamengo e away: ")
print(away_stats)

df_xG_home = df[(df['Statistic'] == 'Expected goals') &
                (df['Flamengo_Posicao'] == 'Home')]
df_xG_away = df[(df['Statistic'] == 'Expected goals') &
                (df['Flamengo_Posicao'] == 'Away')]

print(df_xG_home)
print(df_xG_away)

xG_home = [0.97, 1.64, 1.0, 2.66, 0.91]
media_home = sum(xG_home) / len(xG_home)

xG_away = [1.25, 3.00, 1.92, 3.37, 1.07]
media_away = sum(xG_away) / len(xG_away)

print(f'A media de expectativa de goals jogando como mandante é: {media_home}')
print(f'A media de expectativa de goals jogando como visitante é: {media_away}')