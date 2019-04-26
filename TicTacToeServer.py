import socket


class TicTacToeServer:

    HOST = ''              # Endereco IP do Servidor
    PORT = 5000            # Porta que o Servidor esta
    TCP_SOCKET = ''

    def __init__(self):
        pass

    def inicia_servidor(self,host_ip: str, host_port: int, num_conexoes: int):

        self.HOST = host_ip
        self.PORT = host_port

        self.TCP_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        orig = (self.HOST, self.PORT)

        self.TCP_SOCKET.bind(orig)
        self.TCP_SOCKET.listen(num_conexoes)

    def cria_conexao_jogador(self) -> tuple:

        return self.TCP_SOCKET.accept()

    @staticmethod
    def envia_mensagem(jogador, mensagem: str) -> bool:

        jogador.conexao.sendall(bytes(mensagem, 'utf8'))

        while True:
            try:
                jogador.conexao.sendall(bytes(mensagem, 'utf8'))
                break
            except ValueError:
                print("Erro ao enviar mensagem ao outro jogador")
                return False

        return True

    @staticmethod
    def recebe_mensagem(jogador: object):

        mensagem = ''

        while True:
            try:
                mensagem = jogador.conexao.recv(1024)
                if not mensagem:
                    break
                else:
                    return mensagem.decode('utf8')
            except ValueError:
                print("Erro ao receber mensagem do outro jogador")
                return False

    def get_tcp_socket(self):
        return self.TCP_SOCKET

'''
    def inicia_jogo(con, cliente):

        print('Conectado por: {}'.format(cliente))

        while True:
            msg_em_bytes = con.recv(1024)

            if not msg_em_bytes:
                break

            mensagem_cliente = msg_em_bytes.decode('utf8')


    def conectado(con, cliente):

        print('Conectado por: {}'.format(cliente))

        while True:
            msg = con.recv(1024)
            if not msg:
                break

            mensagem_cliente = msg.decode('utf8')

            if mensagem_cliente == 'sim':
                print('Você disse sim!')
            else:
                print(cliente, mensagem_cliente)

        print('Finalizando conexao do cliente: {}'.format(cliente))
        con.close()
        _thread.exit()
'''

