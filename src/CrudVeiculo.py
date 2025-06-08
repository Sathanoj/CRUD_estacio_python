from Veiculo import Veiculo
from src.CrudOperations import CRUD


class CRUDVeiculo(CRUD):
    def __init__(self, configuration):
        super().__init__("veiculo",configuration)

    # def tupla_pra_veiculo(self, tupla) -> Veiculo:
    #     id_veiculo, marca, modelo, ano, placa, id_cliente = tupla
    #     veiculo = Veiculo(marca, modelo, ano, placa, id_cliente)
    #     veiculo.id = id_veiculo
    #     return veiculo

    def create(self, veiculo: Veiculo, cliente_id: int):
        sql = "INSERT INTO veiculo (marca, modelo, ano, placa, cliente_id) VALUES (%s, %s, %s, %s, %s);"
        valores = (veiculo.marca, veiculo.modelo, veiculo.ano, veiculo.placa, cliente_id)
        self.cursor.execute(sql, valores)
        self.connection.commit()
        print("Veículo cadastrado com sucesso!")

    def veiculos_por_cliente(self, client_id: int):
        sql = "SELECT * FROM veiculo WHERE cliente_id = %s"
        self.cursor.execute(sql, (client_id,))
        resultados = self.cursor.fetchall()
        if resultados:
            # return [self.tupla_pra_veiculo(tupla) for tupla in resultados]
            return resultados
        return None

    def atualizar(self, id: int, veiculo_atualizado: Veiculo):
        sql = "UPDATE veiculo SET marca = %s, modelo = %s, ano = %s, placa = %s WHERE id = %s"
        valores = (
            veiculo_atualizado.marca,
            veiculo_atualizado.modelo,
            veiculo_atualizado.ano,
            veiculo_atualizado.placa,
            id
        )
        self.cursor.execute(sql, valores)
        self.connection.commit()
        print("Veículo atualizado com sucesso.")