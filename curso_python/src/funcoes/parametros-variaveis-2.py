import secrets
from datetime import datetime


def criar_usuario(**atributos):
    novo_usuario = {
        "nome": "",
        "email": "",
        "senha": secrets.token_urlsafe(20),
        "data_criacao": datetime.now(),
        "ativo": True,
    }

    novo_usuario.update(atributos)
    return novo_usuario


novo_usuario = criar_usuario(
    nome="Guilherme", email="guilherme@sp.senai.br", senha="123456"
)

print(novo_usuario)
