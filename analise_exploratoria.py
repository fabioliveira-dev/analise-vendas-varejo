import pandas as pd # Importa a biblioteca pandas com o apelido 'pd' para facilitar a escrita

# Carrega o arquivo CSV gerado anteriormente para dentro de uma variável chamada 'df' (DataFrame)
df = pd.read_csv('vendas_loja.csv')

# O info() funciona como um Raio-X: mostra a quantidade de linhas, se existem valores nulos (buracos) e o tipo de cada coluna (texto, número, etc).
df.info()

# Converte a coluna 'Data' de texto (object) para formato de data real (datetime). Isso permite extrair dia, mês e ano depois.
df['Data'] = pd.to_datetime(df['Data'])

# Verificando se ouve a conversão de 'object' para 'datetime64'
df.info()

# O describe() gera um resumo estatístico das colunas numéricas (Média, Mínimo, Máximo, Desvio Padrão). Ajuda a encontrar erros (ex: preço negativo).
print(df.describe())

# Criamos uma nova coluna calculada: Multiplicamos a quantidade pelo preço unitário para saber o valor final da venda.
df['Valor_Total'] = df['Quantidade'] * df['Preco_unitario']
print(df.describe())

# Análise de Negócio 1: Agrupamos os dados por 'Cidade' e somamos o 'Valor_Total' para ver qual filial vende mais.
# O .sort_values(ascending=False) ordena do maior valor para o menor.
vendas_por_cidade = df.groupby('Cidade')['Valor_Total'].sum().sort_values(ascending=False)
print("\n--- Ranking de Vendas por Cidade ---")
print(vendas_por_cidade)

# Análise de Negócio 2: Ranking de produtos por faturamento total. Mostra quais itens trazem mais dinheiro para a empresa.
vendas_por_produtos = df.groupby('Produto')['Valor_Total'].sum().sort_values(ascending=False)
print("\n--- Ranking de Produtos por Faturamento ---")
print(vendas_por_produtos)

# Exportação de Resultados: Salvamos as tabelas resumidas em arquivos CSV.
# Isso transforma a análise de código em um produto entregável (relatório).
vendas_por_cidade.to_csv('ranking_vendas_cidades.csv')
vendas_por_produtos.to_csv('ranking_vendas_produtos.csv')
print("\nRelatórios de ranking gerados com sucesso!")