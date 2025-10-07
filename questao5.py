from utils import ler_inteiro

def questao5() -> None:
    """
    Questão 5 - Validação de data.
    Lê dia, mês e ano e verifica se a data é válida.
    """
    dia: int = ler_inteiro("Digite o dia: ")
    mes: int = ler_inteiro("Digite o mês: ")
    ano: int = ler_inteiro("Digite o ano: ")

    if mes < 1 or mes > 12 or dia < 1 or dia > 31:
        print("Data invalida")
    elif mes == 2 and dia > 29:
        print("Data invalida")
    elif (mes in [4, 6, 9, 11]) and dia > 30:
        print("Data invalida")
    elif (mes in [1, 3, 5, 7, 8, 10, 12]) and dia > 31:
        print("Data invalida")
    else:
        print("Data valida")
