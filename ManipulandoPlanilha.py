

import pandas as pd

# Carregar o arquivo consolidado
df = pd.read_excel("flamengo_carioca_2025.xlsx")

# Criar uma nova coluna "Flamengo_Posicao" analisando "Ball possession"
df["Flamengo_Posicao"] = df.apply(
    lambda row: "Home" if row["Statistic"] == "Ball possession" and row["Home"] > row["Away"] else
                ("Away" if row["Statistic"] == "Ball possession" and row["Home"] < row["Away"] else None),
    axis=1
)

# Preencher todas as linhas do mesmo jogo com a posição do Flamengo
df["Flamengo_Posicao"] = df["Flamengo_Posicao"].fillna(method="ffill")

# Salvar o arquivo corrigido
df.to_excel("flamengo_carioca_2025_corrigido.xlsx", index=False)

# Mostrar as primeiras linhas para conferir
print(df[["Statistic", "Home", "Away", "Flamengo_Posicao"]].head(15))