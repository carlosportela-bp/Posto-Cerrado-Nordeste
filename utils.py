import dados

def ler_int(msg):
    """Le um numero inteiro do usuario sem deixar o programa quebrar."""
    # BUG DOCUMENTADO: antes eu fazia int(input()) direto no main.
    # se o cara digitasse letra dava ValueError e o sistema fechava td.
    # corrigi botando try/except aqui e pedindo de novo num while.
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("digita um numero!")


def cpf_valido(cpf):
    """Checa se o cpf tem 11 digitos e se ainda n foi usado."""
    if len(cpf) != 11 or not cpf.isdigit():
        print("cpf tem q ter 11 numeros")
        return False
    if cpf in dados.cpfs_cadastrados:  # set evitando duplicata
        print("esse cpf ja ta cadastrado")
        return False
    return True


def iniciais(nome):
    # pega as 3 primeiras letras do nome (slicing) pra mostrar resumido
    return nome[:3].upper()


def percorrer(lista):
    """Gerador q entrega um registro por vez (yield)."""
    for reg in lista:
        yield reg