import socket


class Cliente:

    SERVER = '127.0.0.10'
    PORT = 12345

    def __init__(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

            s.connect((self.SERVER, self.PORT))
            s.send(b'X')

            data = s.recv(1024)

        print("Recebido do servidor: {}".format(repr(data)))


def main():

    cliente = Cliente()

    cliente.__init__()


if __name__ == '__main__':
    main()
