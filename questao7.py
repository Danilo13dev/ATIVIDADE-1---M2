from utils import ler_inteiro, ler_float

def questao7() -> None:
    """
    Questão 7 - Classificação de risco financeiro.
    Lê idade, renda e dívidas e classifica o risco como Alto, Médio, Baixo ou Médio-Baixo.
    """
    idade: int = ler_inteiro("Digite sua idade: ")
    renda: float = ler_float("Digite sua renda mensal: ")
    dividas: float = ler_float("Digite o valor total das dívidas: ")

    if renda > 0:
        perc_divida: float = (dividas / renda) * 100
    else:
        perc_divida: float = 0
        print("Atenção: renda igual a zero!")

    if renda < 2000 and perc_divida > 50:
        risco: str = "Alto"
    elif (2000 <= renda <= 5000) or (30 <= perc_divida <= 50):
        risco = "Médio"
    elif renda > 5000 and perc_divida < 30:
        risco = "Baixo"
    else:
        risco = "Médio-Baixo"

    print(f"\nClassificação de risco: {risco}")
