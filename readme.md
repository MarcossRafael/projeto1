# Análise de desempenho do Flamengo - Carioca 2025

Este projeto tem como objetivo analisar o desempenho do Flamengo no Campeonato Carioca de 2025 com base em diversas estatísticas de jogo.

## Estatísticas Analisadas

- **Total de finalizações (Total Shots)**
- **Gols esperados (Expected Goals - xG)**
- **Média de finalizações por Jogo**
- **Média de gols esperados por Jogo**
- **Teste de hipótese**

## Resultados Obtidos

### 1. **Média de Finalizações (Total Shots)**

- **Em casa**: O Flamengo teve uma média de **14 finalizações por jogo**.
- **Fora de casa**: A média aumentou para **16,4 finalizações por jogo, no qual eu arredondei para 16 para melhor entendimento**.

#### Insight:
O Flamengo mostrou que mesmo jogando como visitante desempenha super bem e agressivamente de acordo com os número de finalizações em comparação quando joga de mandante.

### 2. **Média de Gols Esperados (xG)**

- **Em casa**: A média de gols esperados foi de **1,436 gols por jogo**.
- **Fora de casa**: A média aumentou para **2,122 gols por jogo**.

#### Insight:
A expectativa de gols do Flamengo jogando como visitante é relativamente maior do que jogando de mandante. Ademais, é devido à sua maior agressividade e finalizações jogando fora, mostrando que mesmo estando em uma questão de visitante consegue se manter bem nas partidas.

### 3. **Eficiência nas Finalizações**

- Comparando o número de finalizações com os gols esperados, podemos avaliar a eficiência do time.
- O Flamengo pode melhorar a conversão das finalizações em gols, especialmente em casa, onde o time teve mais dificuldades em alcançar os gols esperados.

#### Insight:
Apesar de ter uma média de finalizações considerável, o Flamengo pode ter mais eficiência na conversão dessas finalizações em gols, especialmente jogando em casa.

#### Teste de hipótese:
Utilizei o **teste t de Student** para classificar duas amostras independentes, uma vez que as amostras são derivadas de dois grupos distintos: jogos como mandante e jogos como visitantes.
Foi usado um **nível de significância de 0.005**.
Obtive resultados para:
- **estatística t:** -0.5541
- **valor-p:** 0.5947

Com base no teste realizado, pude concluir que, de acordo com os dados analisados, não há nenhuma diferença significativa nas finalizações entre os jogos de mandante e visitante. Portanto, a quantidade de finalizações entre ambas situações parecem ter quase o mesmo resultado.


## Conclusão

A análise mostra que o Flamengo tende a ser mais ofensivo fora de casa, com mais finalizações e uma expectativa de gols maior. A melhoria na eficiência das finalizações pode ser um fator importante para o sucesso do time em casa e assim tendo uma consagração maior no campeonato.