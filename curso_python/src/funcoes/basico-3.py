from datetime import datetime


# Função SEM parâmetros e COM retorno
def hora_certa():
    agora = datetime.now()
    return f"{agora.hour:02d}:{agora.minute:02d}:{agora.second:02d}"


hora = hora_certa()
print(hora)
