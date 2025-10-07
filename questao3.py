from utils import ler_float

def questao3() -> None:
    """
    Questão 3 - Cálculo do IMC.
    Lê peso e altura e classifica o IMC conforme a tabela.
    """
    peso: float = ler_float("Digite seu peso: ")
    altura: float = ler_float("Digite sua altura: ")

    imc: float = peso / (altura * altura)

    if imc < 18.5:
        print("Abaixo do peso")
    elif imc >= 18.5 and imc <= 24.9:
        print("Peso normal")
    elif imc >= 25 and imc <= 29.9:
        print("Sobrepeso")
    elif imc >= 30 and imc <= 34.9:
        print("Obesidade grau I")
    elif imc >= 35 and imc <= 39.9:
        print("Obesidade grau II")
    else:
        print("Obesidade grau III")
