import socket

HOST = '127.0.0.10'    # Endereco IP do Servidor
PORT = 1234            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)

print('Para sair use CTRL+X\n')

msg = input("Digite alguma coisa: ")

while msg != '\x18':
    tcp.send(bytes(msg, 'utf8'))
    msg = input("Digite alguma coisa: ")

    recebido = tcp.recv(1024)
    print("Mensagem do servidor: {}", repr(recebido))

tcp.close()