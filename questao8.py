def questao8() -> None:
    """
    Questão 8 - Jogo de cartas.
    O usuário escolhe 4 cartas (A, B, C ou D) e recebe pontos conforme regras.
    """
    gabarito: list[str] = ['B', 'C', 'D', 'A']

    print("Escolha a sequência de 4 cartas (A, B, C ou D).")
    resposta: list[str] = []
    for i in range(4):
        carta: str = input(f"Digite a {i+1}ª carta: ").upper()
        while carta not in ['A', 'B', 'C', 'D']:
            carta = input("Entrada inválida. Digite A, B, C ou D: ").upper()
        resposta.append(carta)

    pontos: int = 0

    for i in range(4):
        if resposta[i] == gabarito[i]:
            pontos += 10

    pontos += resposta.count('A') * 5

    for i in range(3):
        if resposta[i] == 'C' and resposta[i+1] == 'D':
            pontos += 5
            break  

    if pontos > 50:
        pontos = 50

    print(f"\nSua sequência: {resposta}")
    print(f"Pontuação final: {pontos}")
