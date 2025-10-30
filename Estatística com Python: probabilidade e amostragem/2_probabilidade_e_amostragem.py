#%%

import pandas as pd
import numpy as np
import seaborn as sns
from scipy.special import comb
from scipy.stats import binom
from scipy.stats import poisson

# %%

#1 - CONHECENDO OS DADOS

dados = pd.read_csv('/home/ligia/Documents/ALURA/Engenharia/estatistica/Estatística com Python: probabilidade e amostragem/Curso de Estatistica 2/dados.csv')
dados

# %%

# ### UF

# |11|Rondônia|
# |12|Acre|
# |13|Amazonas|
# |14|Roraima|
# |15|Pará|
# |16|Amapá|
# |17|Tocantins|
# |21|Maranhão|
# |22|Piauí|
# |23|Ceará|
# |24|Rio Grande do Norte|
# |25|Paraíba|
# |26|Pernambuco|
# |27|Alagoas|
# |28|Sergipe|
# |29|Bahia|
# |31|Minas Gerais|
# |32|Espírito Santo|
# |33|Rio de Janeiro|
# |35|São Paulo|
# |41|Paraná|
# |42|Santa Catarina|
# |43|Rio Grande do Sul|
# |50|Mato Grosso do Sul|
# |51|Mato Grosso|
# |52|Goiás|
# |53|Distrito Federal|

# > ### Sexo	

# |0|Masculino|
# |1|Feminino|

# > ### Anos de Estudo

# |1|Sem instrução e menos de 1 ano|
# |2|1 ano|
# |3|2 anos|
# |4|3 anos|
# |5|4 anos|
# |6|5 anos|
# |7|6 anos|
# |8|7 anos|
# |9|8 anos|
# |10|9 anos|
# |11|10 anos|
# |12|11 anos|
# |13|12 anos|
# |14|13 anos|
# |15|14 anos|
# |16|15 anos ou mais|
# |17|Não determinados| 
# ||Não aplicável|

# > ### Cor

# |0|Indígena|
# |2|Branca|
# |4|Preta|
# |6|Amarela|
# |8|Parda|
# |9|Sem declaração|

# %%

# 2 - DISTRIBUIÇÕES DE PROBABILIDADE

# 2.1 Distribuição Binominal

#Em um volante de loteria da Mega Sena temos um total de **60 números** para escolher onde a aposta mínima é de **seis números**. Você que é curiosa(o) resolve calcular a probabilidade de se acertar na Mega Sena com apenas **um jogo**. 
#Para isso precisamos saber quantas **combinações de seis números podem ser formadas com os 60 números disponíveis**.


combinacoes = comb(60, 6)
combinacoes
# %%

probabilidade = 1/combinacoes
print(f'{probabilidade:.15f}')
# %%

#Em um concurso para preencher uma vaga de cientista de dados temos um total de **10 questões** de múltipla escolha com **3 alternativas possíveis** em cada questão. **Cada questão tem o mesmo valor.** 
#Suponha que um candidato resolva se aventurar sem ter estudado absolutamente nada. Ele resolve fazer a prova de olhos vendados e chutar todas as resposta. Assumindo que a prova **vale 10 pontos e a nota de corte seja 5**, 
#obtenha a probabilidade deste candidato **acertar 5 questões** e também a probabilidade deste candidato **passar para a próxima etapa do processo seletivo**.

n = 10

alt_por_questao = 3
p = 1 / alt_por_questao
q = 1 - p
k = 5

probabilidade = (comb(n, k) * (p ** k) * (q ** (n - k)))
print(f'{probabilidade:.8f}')
# %%

probabilidade = binom.pmf(k, n, p)
print(f'{probabilidade:.8f}')

# %%

binom.pmf([5,6,7,8,9,10], n, p).sum()
# %%

1 - binom.cdf(4, n, p)
# %%

binom.sf(4, n, p)
# %%

#Uma cidade do interior realiza todos os anos uma gincana para arrecadar fundos para o hospital da cidade. Na última gincana se sabe que a **proporção de participantes do sexo feminino foi de 60%**. 
#O total de equipes, com 12 integrantes, inscritas na gincana deste ano é de 30. Com as informações acima responda: Quantas equipes deverão ser formadas por **8 mulheres**?

p = 0.6
n = 12
k = 8 
probabilidade = binom.pmf(k, n, p)
equipes = 30 * probabilidade
equipes
# %%

# 2.2 Distribuição de Poisson

#Um restaurante recebe em média **20 pedidos por hora**. Qual a chance de que, em determinada hora escolhida ao acaso, o restaurante receba **15 pedidos**?

media = 20
k = 15
probabilidade = ((np.e **(-media)) * (media ** k)) / (np.math.factorial(k))
probabilidade
# %%

probabilidade = poisson.pmf(k, media)
probabilidade
# %%

