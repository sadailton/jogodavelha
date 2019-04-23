
from validador_de_dados import *

def cria_jogo():
    jogo = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    return jogo


def imprime_jogo(jogo):
    for i in range(len(jogo)):
        print(" {:|^1} ".format(jogo[i]), end=" ")
        if i == 2:
            print(end="\n")
        elif i == 5:
            print(end="\n")
        elif i == 8:
            print(end="\n")

    return True


def troca_jogador(jogador: str) -> str:
    if jogador == 'X':
        return "O"
    else:
        return "X"


def valida_jogada(jogo, jogador, jogada):

    if jogo[jogada] == "X" or jogo[jogada] == "O":
        print(msg_colorida("Posição já jogada.", "vermelho"))
        return False
    if jogada > 8 or jogada < 0:
        return False
    else:
        return True


def verifica_jogo(jogo, jogador):
    sequencias_vencedoras = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for i, value in enumerate(sequencias_vencedoras):

        if jogo[sequencias_vencedoras[i][0]] == jogador \
                and jogo[sequencias_vencedoras[i][1]] == jogador \
                and jogo[sequencias_vencedoras[i][2]] == jogador:
            return True

    return False


def cadastra_jogada(jogo: object, jogador: str, jogada: int) -> object:

    jogo[jogada] = jogador

    return jogo


def main():
    print(msg_colorida("Bem vindo ao jogo da velha!!", "verde"))
    jogador: str = "X"
    ganhou = False
    jogar_novamente = valida_sim_nao("Deseja iniciar o jogo? (s/n): ")

    if jogar_novamente:
        jogo = cria_jogo()

    while jogar_novamente:

        imprime_jogo(jogo)
        jogada: int = le_int("Informe a posição da jogada (jogador '{}'): ".format(jogador))

        while not valida_jogada(jogada):
            print(msg_colorida("Posição invalida!!!", "vermelho"))
            jogada: int = le_int("Informe a posição da jogada (jogador '{}'): ".format(jogador))

        cadastra_jogada(jogo, jogador, jogada)
        ganhou = verifica_jogo(jogo, jogador)

        if ganhou:
            imprime_jogo(jogo)
            print("Parabéns!! Você ganhou!!\n")

            jogar_novamente = valida_sim_nao("Deseja jogar novamente? (s/n): ")

            if jogar_novamente:
                jogo = cria_jogo()

        else:
            jogador = troca_jogador(jogador)

    print("Até mais!!")


if __name__ == '__main__':
    main()
