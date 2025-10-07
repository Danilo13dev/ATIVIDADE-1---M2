from utils import ler_float

def questao4() -> None:
    """
    Questão 4 - Média escolar.
    Lê três notas e mostra se o aluno foi aprovado, recuperação ou reprovado.
    """
    media1: float = ler_float("Digite a nota 1: ")
    media2: float = ler_float("Digite a nota 2: ")
    media3: float = ler_float("Digite a nota 3: ")

    media: float = (media1 + media2 + media3) / 3

    if media >= 7:
        print("Aprovado")
    elif media >= 5 and media < 7:
        print("Recuperação")
    elif media < 5:
        print("Reprovado")
    elif media == 0:
        print("Reprovado automático")
    else:
        print("erro")
