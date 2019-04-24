def msg_colorida(msg: str, cor: str) -> str:
    """Uma breve descrição"""
    """
    Uma Breve descrição

    :param msg: A mensagem a ser impressa
    :param cor: vermelho, verde, amarelo, azul, roxo, ciano ou cinza
    :return: string
    """

    if cor == 'vermelho':
        return '\033[0;31m{}\033[m'.format(msg)
    if cor == 'verde':
        return '\033[0;32m{}\033[m'.format(msg)
    if cor == 'amarelo':
        return '\033[0;33m{}\033[m'.format(msg)
    if cor == 'azul':
        return '\033[0;34m{}\033[m'.format(msg)
    if cor == 'roxo':
        return '\033[0;35m{}\033[m'.format(msg)
    if cor == 'ciano':
        return '\033[0;36m{}\033[m'.format(msg)
    if cor == 'cinza':
        return '\033[0;37m{}\033[m'.format(msg)

    return msg


def valida_sim_nao(msg):

    while True:

        resposta = str(input(msg))

        if resposta.isalpha():
            if resposta == 's' or resposta == 'S' or resposta == "Sim" or resposta == "sim":
                return True
            elif resposta == 'n' or resposta == 'N' or resposta == "Não" or resposta == "não":
                return False

        print(msg_colorida("Resposta inválida!", "vermelho"))


def le_int(msg: str):
    """
    :param msg: Mensagem a ser exibida para o usuário
    :return: int
    :type msg: str
    """
    while True:
        n = str(input(msg))
        if n.isnumeric():
            return int(n)
        else:
            print(msg_colorida("Digite um número válido", "vermelho"))
