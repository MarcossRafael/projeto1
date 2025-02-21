

import pandas as pd

## Busquei o arquivo que eu fiz na soma dos 10 jogos do Flamengo, para que eu possa manipula-lo melhor aqui
df = pd.read_excel("flamengo_carioca_2025.xlsx")

## Eu percebi que o Flamengo em todos os jogos tinha posse de bola superior e assim decidi criar uma coluna para conseguir separar o Flamengo em "home" e "away".
## Eu pensei em separar em "home" e "away" para conseguir trabalhar melhor a busca das análises e não confundir dados com de outro time que o Flamengo enfrentou.
## Com isso, dessa forma, decidir procurar como fazer e olhando vídeos e documentação do python, eu achei uma saída incrível com o lambda.
df["Flamengo_Posicao"] = df.apply(
    lambda row: "Home" if row["Statistic"] == "Ball possession" and row["Home"] > row["Away"] else
                ("Away" if row["Statistic"] == "Ball possession" and row["Home"] < row["Away"] else None),
    axis=1
)

## Busquei preencher todas as linhas que tivessem valor vazio na coluna Flamengo_Posicao
df["Flamengo_Posicao"] = df["Flamengo_Posicao"].fillna(method="ffill")

## Salvei o arquivo .xlsx corrigido para que eu pudesse trabalhar toda minha análise nele
df.to_excel("flamengo_carioca_2025_corrigido.xlsx", index=False)

## Aqui eu usei esse script mais como confirmação do que eu tinha feito para ter certeza que tinha dado certo.
print(df[["Statistic", "Home", "Away", "Flamengo_Posicao"]].head(15))