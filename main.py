from questao1 import questao1
from questao2 import questao2
from questao3 import questao3
from questao4 import questao4
from questao5 import questao5
from questao6 import questao6
from questao7 import questao7
from questao8 import questao8
from questao9 import questao9
from questao10 import questao10
from utils import ler_inteiro

def main() -> None:
    
    while True:
        print("\nEscolha uma questão para executar de 1 ao 10 ou 0 para sair:")
        for i in range(1, 11):
            print(f"{i} - Questão {i}")
        print("0 - Sair")

        opcao: int = ler_inteiro("Digite sua opção: ")

        if opcao == 0:
            print("Saindo do programa...")
            break
        elif opcao == 1:
            questao1()
        elif opcao == 2:
            questao2()
        elif opcao == 3:
            questao3()
        elif opcao == 4:
            questao4()
        elif opcao == 5:
            questao5()
        elif opcao == 6:
            questao6()
        elif opcao == 7:
            questao7()
        elif opcao == 8:
            questao8()
        elif opcao == 9:
            questao9()
        elif opcao == 10:
            questao10()
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
