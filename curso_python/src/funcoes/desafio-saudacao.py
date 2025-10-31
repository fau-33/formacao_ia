# Desafio saudação colocando as horas manha, tarde e noite

from datetime import datetime


def hora_atual():
    agora = datetime.now()
    return agora.hour


def saudacao():
    hora = hora_atual()

    match hora:
        case h if h in range(0, 6):
            s = "Boa madrugada!"
        case h if h in range(6, 12):
            s = "Bom dia!"
        case h if h in range(12, 18):
            s = "Boa tarde!"
        case _:
            s = "Boa noite!"

    return s


resultado = saudacao()
print(resultado)
