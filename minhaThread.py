import threading
import Jogador


class MinhaThread (threading. Thread):

    threadID: int = ''
    name: str = ''
    jogador: object = ''

    def __init__(self, threadID, jogador: object):
        threading.Thread.__init__(self)

        self.threadID = threadID
        self.jogador = jogador
        self.name = jogador.nickname

    def run(self) -> None:

        print("Jogador iniciado! {}".format(self.jogador.get_nickname()))
        self.exit()









