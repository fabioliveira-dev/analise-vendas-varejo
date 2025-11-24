import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# 1. Configuração Inicial
# A 'semente' (seed) garante que os números aleatórios sejam sempre iguais 
# toda vez que rodarmos o código. Isso é vital para reprodutibilidade.
np.random.seed(42)

# 2. Definição das variáveis do nosso cenário
qtd_vendas = 1000 #Vamos simular 1000 vendas
produtos = {
    'Notebook Gamer': 4500.00,
    'Mouse Sem Fio': 120.00,
    'Teclado Mecânico': 350.00,
    'Monitor 24pol': 800.00,
    'Headset RGB': 250.00,
    'Cadeira Ergonômica': 1200.00
}
lista_produtos = list(produtos.keys())
cidades = ['Marília', 'São Paulo', 'Bauru', 'Assis', 'Campinas']

#2. Gerando os dados aleatórios
print('Iniciando a geração de dados...')

data_dados = {
    # Gera 1000 escolhas aleatórias da lista de produtos
    'Produto': np.random.choice(lista_produtos, qtd_vendas),
    # Gera 1000 escolhas aleatórias de cidades
    'Cidade': np.random.choice(cidades, qtd_vendas),
    # Gera quantidades vendidas entre 1 e 5 unidades por venda
    'Quantidade': np.random.randint(1, 6, qtd_vendas),
    # Gera datas aleatórias nos últimos 365 dias
    'Data': [datetime.today() - timedelta(days=random.randint(0, 365)) for _ in range(qtd_vendas) ]
}

# 4. Criando o DataFrame (A Tabela do Pandas)
df = pd.DataFrame(data_dados)

# 5. Enriquecendo os dados (Feature Engineering básica)
# Vamos mapear o preço unitário baseado no produto escolhido
# O 'map' funciona como um PROCV do Excel
df['Preco_unitario'] = df['Produto'].map(produtos)

# 6. Visualizando uma amostra
print('\n--- Amostra dos Dados Gerados ---')
print(df.head())

# 7. Salvando em CSV (para usarmos na análise depois)
# index=False serve para não salvar o número da linha no arquivo
df.to_csv('vendas_loja.csv', index=False)
print("\nArquivo 'vendas_loja.csv' gerado com sucesso!")