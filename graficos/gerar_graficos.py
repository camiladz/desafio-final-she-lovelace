import csv
import matplotlib.pyplot as plt

def gerar_grafico_vendas():
    with open('vendas/dados/vendas.csv', mode='r') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        next(leitor_csv)
        vendas = list(leitor_csv)

    if not vendas:
        print("Nenhuma venda registrada para gerar gráficos.")
        return

    produtos = [venda[1] for venda in vendas]
    quantidades = [int(venda[2]) for venda in vendas]

    plt.bar(produtos, quantidades)
    plt.xlabel('Produtos')
    plt.ylabel('Quantidade Vendida')
    plt.title('Vendas por Produto')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
