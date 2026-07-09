# Sistema de Registro de Vendas

Este projeto é um sistema simples de registro de vendas, que permite o armazenamento de dados de vendas em arquivos CSV e a geração de relatórios e gráficos para análise de desempenho. O objetivo é fornecer uma solução prática para registrar vendas, consultar relatórios e visualizar gráficos de maneira simples e rápida.

## Funcionalidades

- **Registro de vendas**: armazena data, produto, quantidade e valor total em `vendas/dados/vendas.csv`.
- **Relatórios**: exibe o total de vendas por produto e aponta o produto mais vendido.
- **Gráficos**: gera um gráfico de barras com a quantidade vendida por produto.

## Estrutura do Projeto

```
.
├── main.py                     # Ponto de entrada do sistema (menu principal)
├── requirements.txt             # Dependências do projeto
├── vendas/
│   ├── registro.py              # Registro de novas vendas
│   ├── relatorios.py            # Geração de relatórios em texto
│   └── dados/
│       └── vendas.csv           # Base de dados das vendas registradas
└── graficos/
    └── gerar_graficos.py        # Geração de gráficos com matplotlib
```

## Instalar as Dependências

```
pip install -r requirements.txt
```

## Como Executar o Projeto

1. Clonar o repositório
2. Executar no terminal o seguinte comando: `python main.py`

## Atalhos do Menu

Ao executar o sistema, escolha uma das opções digitando o número correspondente:

| Opção | Ação |
| ----- | ---- |
| `1` | Registrar uma venda |
| `2` | Gerar relatório |
| `3` | Gerar gráficos |
| `4` | Sair |
