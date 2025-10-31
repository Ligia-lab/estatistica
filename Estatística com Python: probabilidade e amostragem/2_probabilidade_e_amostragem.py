#%%

import pandas as pd
import numpy as np
import seaborn as sns
from scipy.special import comb
from scipy.stats import binom
from scipy.stats import poisson
from scipy.stats import norm

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

# 2.3 Distribuição Normal

# Em um estudo sobre as alturas dos moradores de uma cidade verificou-se que o conjunto de dados segue uma **distribuição aproximadamente normal**, com **média 1,70** e **desvio padrão de 0,1**. 
# Com estas informações obtenha o seguinte conjunto de probabilidades:
# **A.** probabilidade de uma pessoa, selecionada ao acaso, ter menos de 1,80 metros.
# **B.** probabilidade de uma pessoa, selecionada ao acaso, ter entre 1,60 metros e 1,80 metros.    
# **C.** probabilidade de uma pessoa, selecionada ao acaso, ter mais de 1,90 metros.

tabela_normal_padronizada = pd.DataFrame(
    [], 
    index=["{0:0.2f}".format(i / 100) for i in range(0, 400, 10)],
    columns = ["{0:0.2f}".format(i / 100) for i in range(0, 10)])

for index in tabela_normal_padronizada.index:
    for column in tabela_normal_padronizada.columns:
        Z = np.round(float(index) + float(column), 2)
        tabela_normal_padronizada.loc[index, column] = "{0:0.4f}".format(norm.cdf(Z))

tabela_normal_padronizada.rename_axis('Z', axis = 'columns', inplace = True)

tabela_normal_padronizada
# %%

# **A.** probabilidade de uma pessoa, selecionada ao acaso, ter menos de 1,80 metros.

media = 1.7
desvio_padrao = 0.1
Z = (1.8 - media) / desvio_padrao

probabilidade = 0.8413  #usando a tabela

norm.cdf(Z)
# %%

# **B.** probabilidade de uma pessoa, selecionada ao acaso, ter entre 1,60 metros e 1,80 metros.    

Z_superior = (1.8 - media) / desvio_padrao
Z_inferior = (1.6 - media) / desvio_padrao

probabilidade = (0.8413 - 0.5) * 2

probabilidade = norm.cdf(Z_superior) - (1 - norm.cdf(Z_superior))
probabilidade
# %%

# **C.** probabilidade de uma pessoa, selecionada ao acaso, ter mais de 1,90 metros.

Z = (1.9 - media) / desvio_padrao

probabilidade = 1 - 0.9767

probabilidade = 1 - norm.cdf(Z)
probabilidade
# %%

# 3 - AMOSTRAGEM

# 3.1 População e Amostra



