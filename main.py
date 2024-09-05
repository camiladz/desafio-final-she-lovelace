from vendas import registro, relatorios
from graficos import gerar_graficos

def main():
    while True:
        print("\nSistema de Registro de Vendas")
        print("1. Registrar uma venda")
        print("2. Gerar relatório")
        print("3. Gerar gráficos")
        print("4. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            registro.registrar_venda()
        elif escolha == "2":
            relatorios.gerar_relatorio()
        elif escolha == "3":
            gerar_graficos.gerar_grafico_vendas()
        elif escolha == "4":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
