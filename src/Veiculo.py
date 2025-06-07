

class Veiculo:
    def __init__(self, marca, modelo, ano, placa, id=None):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.placa = placa
        self.id = id

    def __str__(self):
        return f"{self.marca}, {self.modelo}, {self.ano}, {self.placa}"

    def __repr__(self):
        return self.__str__()