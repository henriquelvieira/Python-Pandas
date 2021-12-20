import pandas as pd
from matplotlib import pyplot as plt

vCaminhoTabela = r"data\indexdata.csv"
dados = pd.read_csv(vCaminhoTabela) #IMPORTAR CSV C/ TODAS AS COLUNAS
# dados = pd.read_csv(vCaminhoTabela, usecols=['Index', 'Date', 'Close']) #IMPORTAR CSV APENAS COM COLUNAS ESPECIFICADAS

#CRIAR UM DF APENAS COM AS COLUNAS ESPECIFICADAS
df_cotacao = dados[['Index','Date','Close']] 
# print(df_cotacao)

#RENOMEAR COLUNAS
# df_cotacao.rename(columns={'Date': 'dt_ini',
#                            'Close': 'dt_fim'
#                           }, inplace=True)

#CRIAR UM DF APENAS COM OS REGISTROS ONDE O CAMPO INDEX SEJA DIFERENTE DE NYA
df_cotacao_remover = df_cotacao.loc[(df_cotacao['Index'] != 'NYA')] 
# print(df_cotacao_remover)

#CRIAR UM DF APENAS COM OS REGISTRO QUE NÃO ESTEJAM NO DF df_cotacao_remover 
df_cotacao_filtrado = df_cotacao.drop(df_cotacao_remover.index)
# print(df_cotacao_filtrado)

#CRIAR DV FILTRANDO OS REGISTROS PELO INTERVALO DO INDICE
df_cotacao_final = df_cotacao_filtrado[13900:]
# df_cotacao_final = df_cotacao_filtrado[13900:13904] 
print(df_cotacao_final)

#GERAÇÃO DE UM GRÁFICO COM BASE NOS DADOS DO DF
plt.figure(figsize=(15,4))
plt.style.use('ggplot')
plt.title('Cotação histórica da Bolsa NYA')
plt.plot(df_cotacao_final['Date'], df_cotacao_final['Close'], ls='--')
plt.legend(df_cotacao_final['Index'], loc=2)
plt.xticks(['2021-03-23', '2021-04-23', '2021-05-28'])
plt.show()
