import string
from utils import ler_string

def questao10() -> None:
    """
    Questão 10 - Validação de senha.
    Lê uma senha e verifica se ela atende aos critérios de segurança.
    """
    Passworld: str = input("Digite a sua senha: ")

    qtde_mai: int = 0
    qtde_min: int = 0
    qtde_num: int = 0
    qtde_simb: int = 0

    for caractere in Passworld:
        if caractere.isupper():
            qtde_mai += 1
        elif caractere.islower():
            qtde_min += 1
        elif caractere.isdigit():
            qtde_num += 1
        elif caractere in string.punctuation:
            qtde_simb += 1

    if (len(Passworld) >= 8 and 
        qtde_mai >= 1 and
        qtde_min >= 1 and 
        qtde_num >= 1 and
        qtde_simb >= 1):
        print("Senha válida!")
    else:
        print("Senha inválida!")
        print("A senha deve conter pelo menos:")
        if len(Passworld) < 8:
            print("- 8 caracteres")
        if qtde_mai < 1:
            print("- 1 letra maiúscula")
        if qtde_min < 1:
            print("- 1 letra minúscula")
        if qtde_num < 1:
            print("- 1 número")
        if qtde_simb < 1:
            print("- 1 símbolo especial")
