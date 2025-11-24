from model.email import Email
from model.nome_pessoa import NomePessoa

class Usuario:
    def __init__(self, nome, email):
        self.nome = NomePessoa(nome, "Nome Usuário")
        self.email = Email(email, "Email Usuário")
    
    def __str__(self):
        return f"Usuario: {self.nome.completo} - {self.email}"