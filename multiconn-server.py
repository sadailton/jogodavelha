import selectors
import socket
import types


def accept_wrapper(sock):
    conn, addr = sock.accept()
    print("Conexão aceita de: {}".format(addr))
    conn.setblocking(False)
    data = types.SimpleNamespace(addr=addr, inb=b'', outb=b'')
    eventos = selectors.EVENT_READ | selectors.EVENT_WRITE
    sel.register(conn, eventos, data=data)


def service_connection(key, mask):
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024)  # Should be ready to read
        if recv_data:
            data.outb += recv_data
        else:
            print('fechando conexão para: ', data.addr)
            sel.unregister(sock)
            sock.close()
    if mask & selectors.EVENT_WRITE:
        if data.outb:
            print('ecoando...: ', repr(data.outb), 'to', data.addr)
            sent = sock.send(data.outb)  # Should be ready to write
            data.outb = data.outb[sent:]


sel = selectors.DefaultSelector()

host = '127.0.0.10'
port = 12345

lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lsock.bind((host, port))
lsock.listen()
print('Escutando em: {}'.format((host, port)))
lsock.setblocking(False)
sel.register(lsock, selectors.EVENT_READ, data=None)

while True:
    eventos = sel.select(timeout=None)

    for chave, mascara in eventos:
        if chave.data is None:
            accept_wrapper(chave.fileobj)
        else:
            service_connection(chave, mascara)


