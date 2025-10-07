from utils import ler_inteiro

def questao1() -> None:
    """
    Questão 1 - Cálculo de bônus salarial.
    Lê salário e tempo de empresa e aplica as regras de bônus.
    """
    salario: int = ler_inteiro("Digite seu salario: ")
    tempo: int = ler_inteiro("Digite seu tempo de empresa")

    if salario < 2000 and tempo >= 5:
        print(salario + (salario * 0.20))
    elif salario < 2000 and tempo < 5:
        print(salario + (salario * 0.10))
    elif salario >= 2000 and tempo >= 5:
        print(salario + (salario * 0.05))
    elif salario >= 2000 and tempo < 5:
        print(salario and ("sem bonus entregue"))
    else:
        print("erro")

