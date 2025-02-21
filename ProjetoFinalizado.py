

import pandas as pd
import numpy as np
from scipy import stats

df = pd.read_excel("flamengo_carioca_2025_corrigido.xlsx") ## Puxei essa planilha depois de manipular, organizar e corrigir em outro código.

## Estou filtrando o dataframe df para selecionar apenas as linhas que possuem o valor de "Statistic" nas colunas citadas.
estatisticas_numericas = df[df["Statistic"].isin(["Expected goals", "Total shots", "Shots on Goalkeeper saves", "Corner kicks"])]

## Decidi separar os dados filtrados em diferente posições, como "home(mandante)" e "away(visitante)" para manipular melhor e não ter dados misturados
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


## Tive a ideia de criar dataframe para expectativas de gols, assim me gerando boas análises e ideias sobre os jogos do Flamengo.
df_xG_home = df[(df['Statistic'] == 'Expected goals') &
                (df['Flamengo_Posicao'] == 'Home')]
df_xG_away = df[(df['Statistic'] == 'Expected goals') &
                (df['Flamengo_Posicao'] == 'Away')]

print(df_xG_home)
print(df_xG_away)

## Acabei fazendo média da expectativa de gols separados em home e away de uma forma "manual", porque não consegui buscar de forma mais "prática" usando algum script.
xG_home = [0.97, 1.64, 1.0, 2.66, 0.91]
media_home = sum(xG_home) / len(xG_home)

xG_away = [1.25, 3.00, 1.92, 3.37, 1.07]
media_away = sum(xG_away) / len(xG_away)

print(f'A media de expectativa de goals jogando como mandante e: {media_home:.2f}')
print(f'A media de expectativa de goals jogando como visitante e: {media_away:.2f}')

## A mesma ideia que tive em fazer com expectativa de gols, eu busquei também na parte de finalizações, para uma apuração melhorada e a parte.
df_totalShots_home = df[(df['Statistic'] == 'Total shots') &
                (df['Flamengo_Posicao'] == 'Home')]

df_totalShots_away = df[(df['Statistic'] == 'Total shots') &
                (df['Flamengo_Posicao'] == 'Away')]

print(df_totalShots_home)
print(df_totalShots_away)

totalShots_home = [9, 14, 13, 28, 6]
media_Shome = round(sum(totalShots_home) / len(totalShots_home))

totalShots_away = [13, 20, 21, 18, 10]
media_Saway = round(sum(totalShots_away) / len(totalShots_away))

print(f'A media de expectativa de chutes jogando como mandante e: {media_Shome}')
print(f'A media de expectativa de chutes jogando como mandante e: {media_Saway}')


finalizacoes_mandante = [9, 14, 13, 28, 6]
finalizacoes_visitante = [13, 20, 21, 18, 10]


## Eu pensei em uma forma de usar algum pensamento ou termo de data science para enriquecer esse projeto e optei por usar o teste de hipótese, para clarear sobre  a diferença mandante x visitante
t_stat, p_value = stats.ttest_ind(finalizacoes_mandante, finalizacoes_visitante)

print(f'Estatistica t: {t_stat:.4f}')
print(f'Valor-p: {p_value:.4f}')

alpha = 0.05
if p_value < alpha:
    print("Rejeitamos a hipotese nula. Ha uma diferenca significativa nas finalizaoees entre casa e fora de casa.")
else:
    print("Nao rejeitamos a hipotese nula. Nao ha uma diferenca significativa nas finalizacoes entre casa e fora de casa.")