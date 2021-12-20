import pandas as pd

vCaminhoTabela = r"data\exemplo_pandas.xlsx"
tabela = pd.read_excel(vCaminhoTabela)

# print(tabela)
# print(tabela[['Produto','Val. Total']])

valor_total = tabela['Val. Total'].sum()
valor_min = tabela['Val. Total'].min()
valor_max = tabela['Val. Total'].max()
print(f'Valor Total: {str(valor_total)}')
print(f'Menor Compra: {str(valor_min)}')
print(f'Maior Compra: {str(valor_max)}')

# tb_faturamento_produto = tabela[['Produto','Val. Total']]
# print(tb_faturamento_produto)
# print(tb_faturamento_produto[['Produto','Val. Total']].groupby('Produto').sum())

tb_faturamento_loja = tabela[['Loja','Produto','Val. Total']]
# print(tb_faturamento_loja)
print(tb_faturamento_loja[['Loja','Produto','Val. Total']].groupby(['Loja','Produto']).sum())