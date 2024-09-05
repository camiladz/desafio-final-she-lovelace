import csv
from collections import Counter

def gerar_relatorio():
    with open('vendas/dados/vendas.csv', mode='r') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        vendas = list(leitor_csv)

    if not vendas:
        print("Nenhuma venda registrada.")
        return

    # Relatório de vendas por produto
    produtos = [venda[1] for venda in vendas]
    contador_produtos = Counter(produtos)
    
    print("\nRelatório de Vendas por Produto:")
    for produto, quantidade in contador_produtos.items():
        print(f"{produto}: {quantidade} vendas")

    # Produto mais vendido
    produto_mais_vendido = contador_produtos.most_common(1)[0]
    print(f"\nProduto mais vendido: {produto_mais_vendido[0]} ({produto_mais_vendido[1]} vendas)")
