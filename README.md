# 📊 Análise de Dados de Vendas - Varejo

Este projeto simula um pipeline de análise de dados para uma loja de varejo de eletrônicos. O objetivo foi gerar dados fictícios realistas, realizar limpeza e tratamento (ETL), e extrair insights de negócio para suporte à tomada de decisão.

## 🚀 Tecnologias Utilizadas
- **Python 3.12**
- **Pandas** (Manipulação e Análise de Dados)
- **NumPy** (Computação Numérica)
- **Git & GitHub** (Versionamento de Código)

## 📂 Estrutura do Projeto

1. **Geração de Dados (`gerar_dados.py`)**: Script responsável por criar um dataset fictício (`vendas_loja.csv`) contendo 1000 transações com:
   - Produtos variados (Notebooks, Periféricos, etc.)
   - Cidades filiais
   - Datas aleatórias (série temporal)
   - Preços e quantidades

2. **Análise Exploratória (`analise_exploratoria.py`)**: Script que consome o CSV gerado e realiza:
   - Limpeza de dados e conversão de tipos (Datetime)
   - Feature Engineering (Criação da coluna `Valor_Total`)
   - Estatística Descritiva (Médias, Máximos, Mínimos)
   - Agrupamentos (Groupby) para rankings

## 📈 Resultados Obtidos

O projeto gerou automaticamente dois relatórios em CSV com insights valiosos:
- `ranking_vendas_cidades.csv`: Performance de vendas por localidade.
- `ranking_vendas_produtos.csv`: Produtos com maior faturamento (Curva ABC).

## 🔧 Como Executar

1. Clone o repositório:
```bash
git clone [https://github.com/fabioliveira-dev/analise-vendas-varejo.git](https://github.com/fabioliveira-dev/analise-vendas-varejo.git)

2. Crie e ative o ambiente virtual:
```bash
python -m venv .venv
.\.venv\Scripts\Activate  # No Windows

3. Instale as dependências:
```bash
pip install -r requirements.txt

4. Execute a geração de dados e a análise:
```bash
python gerar_dados.py
python analise_exploratoria.py

Desenvolvido por Fabio de Oliveira 👨‍💻