from utils import ler_inteiro, ler_string

def questao6() -> None:
    """
    Questão 6 - Obrigatoriedade do voto.
    Lê idade e nacionalidade e informa se o voto é obrigatório, opcional ou não permitido.
    """
    idade: int = ler_inteiro("Digite sua idade: ")
    nacionalidade: str = ler_string("Digite sua nacionalidade: Brasileiro ou Estrangeiro ")

    if idade >= 18 and nacionalidade == "Brasileiro":
        print("Obrigatorio votar")
    elif idade >= 16 and idade <= 17 and nacionalidade == "Brasileiro":
        print("Opcional votar")
    elif idade >= 18 and nacionalidade == "Estrangeiro":
        print("Opcional votar")
    else:
        print("Não pode votar")
