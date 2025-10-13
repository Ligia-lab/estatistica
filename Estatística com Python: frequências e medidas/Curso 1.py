#%%



import pandas as pd
import numpy as np
import seaborn as sns
import scipy

# %%

#CONHECENDO OS DADOS

import zipfile

nome_arquivo_zip = 'Curso_de_Estatistica.zip'

with zipfile.ZipFile(nome_arquivo_zip, 'r') as zip_ref:
    zip_ref.extractall()
    
# %%

dados = pd.read_csv('Curso de Estatística/dados.csv')
dados.head()

# %%

#LEGENDA

# > ### UF

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


# Utilizar a seguinte classificação:

# A ► Acima de 20 SM
# B ► De 10 a 20 SM
# C ► De 4 a 10 SM
# D ► De 2 a 4 SM
# E ► Até 2 SM

# onde SM é o valor do salário mínimo na época. Em nosso caso R$ 788,00 (2015):

# A ► Acima de 15.760
# B ► De 7.880 a 15.760
# C ► De 3.152 a 7.880
# D ► De 1.576 a 3.152
# E ► Até 1.576


# %%

#-------------------------------------------------------
#TIPO DE DADOS

#Variáveis qualitativas ordinais
sorted(dados['Anos de Estudo'].unique())

# %%

#Variáveis qualitativas nominais
sorted(dados['UF'].unique())

# %%

#Variáveis quantitativas discretas 
dados.Idade.min()

# %%

#Variáveis quantitativas ordinal 
dados.Altura.min()

# %%

#--------------------------------------------------------
#DISTRIBUIÇÃO DE FREQUÊNCIAS

#Distribuição de frequências para variáveis qualitativas
#Método 1

frequencia = dados['Sexo'].value_counts()
percentual = dados['Sexo'].value_counts(normalize=True) * 100
dist_freq_qualitativos = pd.DataFrame({'Frequência': frequencia, 'Porcentagem (%)': percentual})
dist_freq_qualitativos.rename(index={0: 'Masculino', 1: 'Feminino'}, inplace=True)
dist_freq_qualitativos.rename_axis('Sexo',axis='columns', inplace=True)
dist_freq_qualitativos

# %%

#2.1 Distribuição de frequências para variáveis qualitativas
#Método 2

sexo = {0: 'Masculino',
        1: 'Feminino'}

cor = {0: 'Indígena',
        2: 'Branca',
        4: 'Preta',
        6: 'Amarela',
        8: 'Parda',
        9: 'Sem declaração'}


frequencia = pd.crosstab(dados.Sexo, 
                         dados.Cor)
frequencia.rename(index=sexo, inplace=True)
frequencia.rename(columns=cor, inplace=True)
frequencia


# %%

percentual = pd.crosstab(dados.Sexo, 
                         dados.Cor, 
                         normalize=True) * 100
percentual.rename(index=sexo, inplace=True)
percentual.rename(columns=cor, inplace=True)
percentual

# %%

#2.2 Distribuição de frequências para variáveis quantitativas (classes personalizadas)
#Passo 1 - Especificar os limites de cada classe

dados.Renda.min()
dados.Renda.max()

classes = [0, 1576, 3152, 7880, 15760, 200000]
labels = ['E', 'D', 'C', 'B', 'A']

# %%

#Passo 2 - Criar a tabela de frequências

pd.cut(x=dados.Renda, 
       bins=classes, 
       labels=labels, 
       include_lowest=True)

# %%

frequencia = pd.value_counts(pd.cut(x=dados.Renda, 
                                    bins=classes, 
                                    labels=labels, 
                                    include_lowest=True))
frequencia

# %%

percentual = pd.value_counts(pd.cut(x=dados.Renda, 
                                    bins=classes, 
                                    labels=labels, 
                                    include_lowest=True),
                            normalize=True) * 100
percentual
# %%

dist_freq_quantitativas_personalizadas = pd.DataFrame({'Frequência': frequencia, 'Porcentagem (%)': percentual})
dist_freq_quantitativas_personalizadas.sort_index(ascending=False)

# %%

#2.3 Distribuição de frequências para variáveis quantitativas (classes de amplitude fixa)
#Passo 1 - Difinindo o número de classes

#Regra de Sturges

n = dados.shape[0]
k = 1 + (10/3) * np.log10(n)
k
# %%
