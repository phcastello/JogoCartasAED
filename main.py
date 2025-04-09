from classes import *
import random

baralho = {
    1: "ás",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "10",
    11: "q",
    12: "j",
    13: "k"
}

if __name__ == "__main__":
    # Cria uma pilha de cartas
    pilhaJ1, pilhaJ2 = Stack(), Stack()
    J1, J2 = Player("Jogador 1"), Player("Jogador 2")

    for _ in range(10):
        cartaJ1 = random.choice(list(baralho.keys()))
        cartaJ2 = random.choice(list(baralho.keys()))
        pilhaJ1.push(cartaJ1)
        pilhaJ2.push(cartaJ2)

    # Para debug, imprimir as cartas de ambas as pilhas no inicio
    print(f"Pilha Jogador 1: {pilhaJ1.items}")
    print(f"Pilha Jogador 2: {pilhaJ2.items}")

    rodada = 10
    while rodada > 0:
        print(f"\nRodada {11 - rodada}")
        NcartaJ1 = pilhaJ1.show_top()
        NcartaJ2 = pilhaJ2.show_top()
        cartaJ1 = baralho[NcartaJ1]
        cartaJ2 = baralho[NcartaJ2]

        print(f"Jogador 1: {cartaJ1}\nJogador 2: {cartaJ2}")
        if NcartaJ1 > NcartaJ2:
            J1.add_point(NcartaJ1)
            print(f"Removendo carta do Jogador 1: {pilhaJ1.pop()}")
            print(f"Removendo carta do Jogador 2: {pilhaJ2.pop()}")
            print(f"Jogador 1 ganhou a rodada. Ele ganhou {NcartaJ1} pontos")
        elif NcartaJ2 > NcartaJ1:
            J2.add_point(NcartaJ2)
            print(f"Removendo carta do Jogador 1: {pilhaJ1.pop()}")
            print(f"Removendo carta do Jogador 2: {pilhaJ2.pop()}")
            print(f"Jogador 2 ganhou a rodada. Ele ganhou {NcartaJ2} pontos")
        else:
            print("Empate, ninguem ganha pontos.")
            print(f"Removendo carta do Jogador 1: {pilhaJ1.pop()}")
            print(f"Removendo carta do Jogador 2: {pilhaJ2.pop()}")
        print(f"Pilha Jogador 1: {pilhaJ1.items}")
        print(f"Pilha Jogador 2: {pilhaJ2.items}")
        rodada -= 1
    print(f"\nPlacar final: Jogador 1: {J1.score} - Jogador 2: {J2.score}")
    if J1.score > J2.score:
        print("Jogador 1 venceu!")
    elif J1.score < J2.score:
        print("Jogador 2 venceu!")
    else:
        print("Empate!")