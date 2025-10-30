 #%%

import pandas as pd
import numpy as np
import seaborn as sns
import scipy

# %%

#CONHECENDO OS DADOS

dados = pd.read_csv('/home/ligia/Documents/ALURA/Engenharia/estatistica/Estatística com Python: frequências e medidas/Curso de Estatística 1/dados.csv')
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

k = int(k.round(0))
k

# %%

#Passo 2 - Criar a tabela de frequências

pd.value_counts(
    pd.cut(
        x=dados.Renda,
        bins=17,
        include_lowest=True
    ), sort=False
)

# %%

frequencia = pd.value_counts(
                pd.cut(
                        x=dados.Renda,
                        bins=17,
                        include_lowest=True
                ), sort=False
             )

percentual = pd.value_counts(
                pd.cut(
                        x=dados.Renda,
                        bins=17,
                        include_lowest=True
                ), sort=False,
                normalize=True 
             ) * 100

# %%

frequencia

# %%

percentual

# %%

dist_freq_quantitativas_amplitude_fixa = pd.DataFrame(
    {'Frequência' : frequencia, 'Porcentagem (%)': percentual}
)
dist_freq_quantitativas_amplitude_fixa

# %%

#2.4 Histograma

ax = sns.distplot(dados.Altura, kde=False)

ax.figure.set_size_inches(12,6)
ax.set_title('Distribuição de frequências - Altura', fontsize=18)
ax.set_xlabel('Metros', fontsize=14)
ax

# %%

ax = sns.distplot(dados.Altura)

ax.figure.set_size_inches(12,6)
ax.set_title('Distribuição de frequências - Altura - KDE', fontsize=18)
ax.set_xlabel('Metros', fontsize=14)
ax

# %%

dados.Altura.hist(bins = 50, figsize=(12,6))

# %%

dist_freq_quantitativas_personalizadas['Frequência'].plot.bar(width = 1, color = 'blue', alpha = 0.2, figsize = (12, 6))

# %%

# 3 MEDIDAS DE TENDÊNCIA CENTRAL

# DataFrame Exemplo

df = pd.DataFrame(data = {'Fulano': [8, 10, 4, 8, 6, 10, 8],
                          'Beltrano': [10, 2, 0.5, 1, 3, 9.5, 10],
                          'Sicrano': [7.5, 8, 7, 8, 8, 8.5, 7]},
                 index = ['Matemática',
                          'Português',
                          'Inglês',
                          'Geografia',
                          'História',
                          'Física',
                          'Química'])
df.rename_axis('Matérias', axis = 'columns', inplace = True)
df

#%%

# 3.1 Média aritmética

df['Fulano'].mean()

# %%

dados.Renda.mean()

# %%

dados.groupby(['Sexo'])['Renda'].mean()

# %%

# 3.2 Mediana

notas_fulano = df.Fulano
notas_fulano

# %%

notas_fulano = notas_fulano.sort_values()
notas_fulano

# %%

notas_fulano = notas_fulano.reset_index()
notas_fulano

# %%

n = notas_fulano.shape[0]
n

# %%

elemento_md = (n + 1) / 2
elemento_md

# %%

notas_fulano.loc[elemento_md - 1]

# %%

notas_fulano['Fulano'] = pd.to_numeric(notas_fulano['Fulano'], errors='coerce')

# %%

notas_fulano['Fulano'].median()

# %%

notas_beltrano = df.Beltrano.sample(6, random_state=101)
notas_beltrano

# %%

notas_beltrano.median()

# %%

dados.Renda.median()

# %%

dados.Renda.quantile()

# %%

# 3.3 Moda

df

# %%

df.mode()

# %%

dados.Renda.mode()

# %%

dados.Altura.mode()

# %%

# 3.4 Relação entre Média, Mediana e Moda

ax = sns.displot(dados.query('Renda < 20000').Renda)
ax.figure.set_size_inches(12, 6)
ax

# %%

Moda = dados.Renda.mode()[0]
Moda

# %%

Mediana = dados.Renda.median()
Mediana

# %%

Media = dados.Renda.mean()
Media

# %%

Moda < Mediana < Media

# %%

ax = sns.displot(dados.Altura)
ax.figure.set_size_inches(12, 6)
ax 

# %%

Moda = dados.Altura.mode()
Moda

# %%

Mediana = dados.Altura.median()
Mediana

# %%

Media = dados.Altura.mean()
Media

# %%

ax = sns.displot(dados['Anos de Estudo'], bins=17)
ax.figure.set_size_inches(12, 6)
ax 

# %%

Moda = dados['Anos de Estudo'].mode()[0]
Moda

# %%

Mediana = dados['Anos de Estudo'].median()
Mediana

# %%

Media = dados['Anos de Estudo'].mean()
Media

# %%

# 4 MEDIDAS SEPARATRIZES

# 4.1 Quartis, decis e percentis

dados.Renda.quantile([0.25, 0.5, 0.75])

# %%

[i/10 for i in range(1, 10)]

# %%

dados.Renda.quantile([i/10 for i in range(1, 10)])

# %%

dados.Renda.quantile([i/100 for i in range(1, 100)])

# %%

ax = sns.distplot(dados.Idade,
                  hist_kws = {'cumulative': True},
                  kde_kws = {'cumulative': True})
ax.figure.set_size_inches(14, 6)
ax.set_title('Distribuição de Frequências Acumulada', fontsize=18)
ax.set_ylabel('Acumulado', fontsize=14)
ax.set_xlabel('Anos', fontsize=14)
ax

# %%

dados.Idade.quantile([i/10 for i in range(1, 10)])

# %%

# 4.2 Box-plot

ax = sns.boxplot( x = 'Altura', data = dados, orient = 'h')
ax.figure.set_size_inches(12, 4)
ax.set_title('Altura', fontsize=18)
ax.set_xlabel('Metros', fontsize=14)
ax

# %%

ax = sns.boxplot( x = 'Altura', y = 'Sexo', data = dados, orient = 'h')
ax.figure.set_size_inches(12, 4)
ax.set_title('Altura', fontsize=18)
ax.set_xlabel('Metros', fontsize=14)
ax

# %%

ax = sns.boxplot( x = 'Renda', data = dados, orient = 'h')
ax.figure.set_size_inches(12, 4)
ax.set_title('Renda', fontsize=18)
ax.set_xlabel('R$', fontsize=14)
ax

# %%

ax = sns.boxplot( x = 'Renda', data = dados.query('Renda < 10000'), orient = 'h')
ax.figure.set_size_inches(12, 4)
ax.set_title('Renda', fontsize=18)
ax.set_xlabel('R$', fontsize=14)
ax

# %%

ax = sns.boxplot( x = 'Renda', y = 'Sexo', data = dados.query('Renda < 10000'), orient = 'h')
ax.figure.set_size_inches(12, 4)
ax.set_title('Renda', fontsize=18)
ax.set_xlabel('R$', fontsize=14)
ax

# %%

ax = sns.boxplot( x = 'Anos de Estudo', data = dados, orient = 'h')
ax.figure.set_size_inches(12, 4)
ax.set_title('Anos de Estudo', fontsize=18)
ax.set_xlabel('Anos', fontsize=14)
ax

# %%

ax = sns.boxplot( x = 'Anos de Estudo', y = 'Sexo', data = dados, orient = 'h')
ax.figure.set_size_inches(12, 4)
ax.set_title('Anos de Estudo', fontsize=18)
ax.set_xlabel('Anos', fontsize=14)
ax

# %%

# 5 MEDIDAS DE DISPERSÃO

# 5.1 Desvio médio absoluto

df

# %%

notas_fulano = df[['Fulano']]
notas_fulano

# %%

nota_media_fulano = notas_fulano.mean()[0]
nota_media_fulano

# %%

notas_fulano['Desvio'] = notas_fulano['Fulano'] - nota_media_fulano
notas_fulano

# %%

notas_fulano['|Desvio|'] = notas_fulano['Desvio'].abs()
notas_fulano

# %%

ax = notas_fulano['Fulano'].plot(style = 'o')
ax.figure.set_size_inches(14, 6)
ax.hlines(y = nota_media_fulano, xmin = 0, xmax = notas_fulano.shape[0] - 1, colors = 'red')
for i in range(notas_fulano.shape[0]):
    ax.vlines(x = i, ymin = nota_media_fulano, ymax = notas_fulano['Fulano'][i], linestyle='dashed')
ax

# %%

notas_fulano['|Desvio|'].mean()

# %%

desvio_medio_absoluto = notas_fulano['Fulano'].mad()
desvio_medio_absoluto

# %%

# 5.2 Variância

notas_fulano['(Desvio)^2'] = notas_fulano['Desvio'].pow(2)
notas_fulano

# %%

notas_fulano['(Desvio)^2'].sum() / (len(notas_fulano) - 1)

# %%

variancia = notas_fulano['Fulano'].var()
variancia 

# %%

# 5.3 Desvio padrão

np.sqrt(variancia)

# %%

desvio_padrao = notas_fulano['Fulano'].std()
desvio_padrao

# %%

df.mean()

# %%

df.std()

