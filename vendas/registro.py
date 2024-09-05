import csv
from datetime import datetime

def registrar_venda():
    data = input("Data da venda (dd/mm/aaaa): ")
    produto = input("Nome do produto: ")
    quantidade = int(input("Quantidade vendida: "))
    valor_total = float(input("Valor total da venda: "))

    with open('vendas/dados/vendas.csv', mode='a', newline='') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)
        escritor_csv.writerow([data, produto, quantidade, valor_total])

    print("Venda registrada com sucesso!")
