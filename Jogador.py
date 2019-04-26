from socket import socket


class Jogador:
    conexao: socket = ''
    endereco_ip: str = ''
    id: int = 0
    nickname: str = ''
    simbolo: str = ''

    def __init__(self):
        pass

    def cria_jogador(self, soquete, nickname, id):
        self.conexao, self.endereco_ip = soquete
        self.nickname = nickname
        self.id = id

    def get_nickname(self):
        return self.nickname

    def set_nickname(self, nickname):
        self.nickname = nickname

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def set_socket(self, soquete):
        self.conexao, self.endereco_ip = soquete
