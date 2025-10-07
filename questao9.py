from utils import ler_float, ler_string

def questao9() -> None:
    """
    Questão 9 - Desconto em produtos.
    Lê o preço do produto e se o cliente é VIP, e aplica o desconto.
    """
    preco: float = ler_float("Digite o preço do produto: R$ ")
    vip: str = ler_string("O cliente é VIP? (sim/não): ").lower()

    desconto: float = 0

    if preco >= 100:
        desconto = 0.20
    elif preco >= 50:
        desconto = 0.10
    else:
        desconto = 0.00

    if vip == "sim":
        desconto += 0.05

    preco_final: float = preco * (1 - desconto)

    print(f"\nPreço original: R$ {preco:.2f}")
    print(f"Desconto aplicado: {desconto*100:.0f}%")
    print(f"Preço final: R$ {preco_final:.2f}")
