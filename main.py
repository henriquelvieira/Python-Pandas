import pandas as pd

vCaminhoTabela = r"data\exemplo_pandas.xlsx"
tabela = pd.read_excel(vCaminhoTabela)

# print(tabela)
# print(tabela['Val. Total'])
# print(tabela[['Produto','Val. Total']])

# print(tabela['Val. Total'].sum())

# tb_faturamento_produto = tabela[['Produto','Val. Total']]
# print(tb_faturamento_produto)
# print(tb_faturamento_produto[['Produto','Val. Total']].groupby('Produto').sum())

tb_faturamento_loja = tabela[['Loja','Produto','Val. Total']]
print(tb_faturamento_loja)
print(tb_faturamento_loja[['Loja','Produto','Val. Total']].groupby(['Loja','Produto']).sum())