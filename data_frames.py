import pandas as pd

vCaminhoTabela = r"data\indexdata.csv"
dados = pd.read_csv(vCaminhoTabela)

#CRIAR UM DF APENAS COM AS COLUNAS ESPECIFICADAS
df_cotacao = dados[['Index','Date','Close']] 
print(df_cotacao)

#CRIAR UM DF APENAS COM OS REGISTROS ONDE O CAMPO INDEX SEJA DIFERENTE DE NYA
df_cotacao_remover = df_cotacao.loc[(df_cotacao['Index'] != 'NYA')] 
print(df_cotacao_remover)

#CRIAR UM DF APENAS COM OS REGISTRO QUE NÃO ESTEJAM NO DF df_cotacao_remover 
df_cotacao_final = df_cotacao.drop(df_cotacao_remover.index)
print(df_cotacao_final)

