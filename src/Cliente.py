
class Cliente:
    def __init__(self, nome, endereco, cpf, telefone):
        self.nome = nome
        self.endereco = endereco
        self.cpf = cpf
        self.telefone = telefone

    def __str__(self):
        return f"{self.nome}, {self.endereco}, {self.cpf}, {self.telefone}"