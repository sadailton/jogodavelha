import selectors
import socket

class IniciaServidor:

    host = "127.0.0.10"
    porta = 1234
    sel = selectors.DefaultSelector()

    def __init__(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.porta))
            s.listen()

            conn, addr = s.accept()

            with conn:
                print("Escutando em: {}".format(addr))

                while True:
                    conn.sendall(b'Bem vindo!!')
                    data = conn.recv(1024)
                    if not data:
                        break
                    else:
                        conn.sendall(data)
                    print(type(data))


def main():

    servidor = IniciaServidor()

    servidor.__init__()


if __name__ == '__main__':
    main()


