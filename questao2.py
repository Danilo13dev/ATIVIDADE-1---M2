from utils import ler_inteiro

def questao2() -> None:
    lado1 = ler_inteiro("Digite o lado 1: ")
    lado2 = ler_inteiro("Digite o lado 2: ")
    lado3 = ler_inteiro("Digite o lado 3: ")

    if lado1 == lado2 == lado3:
        print("equilátero")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("isósceles")
    else:
        print("escaleno")
