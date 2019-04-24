from validador_de_dados import *

class JogoDaVelha:
    jogo = []

    def __init__(self) -> object:
        self.jogo = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    def imprime_jogo(self, jogo):

        print()

        for i in range(0, 9):
            print(" {} |".format(jogo[i]), end=" ")
            if i == 2:
                print(end="\n")
                print("--- ---- ----")
            if i == 5:
                print(end="\n")
                print("--- ---- ----")

        print("\n")

        return True

    def troca_jogador(self, jogador: str) -> str:
        if jogador == 'X':
            return "O"
        else:
            return "X"

    def valida_jogada(self, jogo, jogador, jogada):

        if jogada > 8 or jogada < 0:
            return False

        if jogo[jogada] == "X" or jogo[jogada] == "O":
            print(msg_colorida("Posição já jogada.", "vermelho"))
            return False

        else:
            return True

    @staticmethod
    def verifica_jogo(jogo: list, jogador: str) -> int:
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
                return 1

        cont: int = 0
        for i in jogo:
            if i == 'X' or i == 'O':
                cont += 1

        if cont == 9:
            return 2
        else:
            return 0

    def cadastra_jogada(self, jogo: object, jogador: str, jogada: int) -> object:

        jogo[jogada] = jogador

        return jogo


def main():
    print(msg_colorida("Bem vindo ao jogo da velha!!", "verde"))
    jogador: str = "X"
    ganhou = 0
    jogar_novamente = valida_sim_nao("Deseja iniciar o jogo? (s/n): ")

    if jogar_novamente:
        jogodavelha = JogoDaVelha()

    while jogar_novamente:

        jogodavelha.imprime_jogo(jogodavelha.jogo)
        jogada: int = le_int("Informe a posição da jogada (jogador '{}'): ".format(jogador))

        while not jogodavelha.valida_jogada(jogodavelha.jogo, jogador, jogada):
            print(msg_colorida("Posição invalida!!!", "vermelho"))
            jogada: int = le_int("Informe a posição da jogada (jogador '{}'): ".format(jogador))

        jogodavelha.cadastra_jogada(jogodavelha.jogo, jogador, jogada)
        ganhou = jogodavelha.verifica_jogo(jogodavelha.jogo, jogador)

        if ganhou == 1:
            jogodavelha.imprime_jogo(jogodavelha.jogo)
            print("Parabéns!! Você ganhou!!\n")

            jogar_novamente = valida_sim_nao("Deseja jogar novamente? (s/n): ")

            if jogar_novamente:
                jogodavelha = JogoDaVelha()

        elif ganhou == 2:
            jogodavelha.imprime_jogo(jogodavelha.jogo)
            print("Deu velha!!")

            jogar_novamente = valida_sim_nao("Deseja jogar novamente? (s/n): ")

            if jogar_novamente:
                jogodavelha = JogoDaVelha()

        else:
            jogador = jogodavelha.troca_jogador(jogador)

    print("Até mais!!")

if __name__ == '__main__':
    main()
