
class Cliente:
    def __init__(self, nome, endereco, cpf, telefone, id=None):
        self.nome = nome
        self.endereco = endereco
        self.cpf = cpf
        self.telefone = telefone
        self.id = id

    def __str__(self):
        return f"{self.nome}, {self.endereco}, {self.cpf}, {self.telefone}"

    def __repr__(self):
        return self.__str__()