from Veiculo import Veiculo
from DataBaseManeger import DataBaseManager
from src.CrudOperations import CRUD


class CRUDVeiculo(CRUD):
    def __init__(self, configuration):
        super().__init__("veiculo",configuration)

    def to_obj(self, tupla) -> Veiculo:
        id_veiculo, marca, modelo, ano, placa, id_cliente = tupla
        veiculo = Veiculo(marca, modelo, ano, placa, id_cliente)
        veiculo.id = id_veiculo
        return veiculo

    def veiculo_por_id(self, id: int) -> Veiculo:
        # sql = "SELECT * FROM veiculo WHERE id = %s"
        # self.cursor.execute(sql, (id,))
        # resultado = self.cursor.fetchone()
        # if resultado:
        #     return self.tupla_para_veiculo(resultado)
        # return None
        tupla = super().get_by_id(id)
        return self.to_obj(tuple) if tupla else None

    def create_veiculo(self, veiculo: Veiculo, id_cliente: int):
        sql = "INSERT INTO veiculo (marca, modelo, ano, placa, id_cliente) VALUES (%s, %s, %s, %s, %s);"
        valores = (veiculo.marca, veiculo.modelo, veiculo.ano, veiculo.placa, id_cliente)
        self.cursor.execute(sql, valores)
        self.connection.commit()
        print("Veículo cadastrado com sucesso!")

    # def all_veiculos(self):
    #     self.cursor.execute("SELECT * FROM veiculo")
    #     veiculos = self.cursor.fetchall()
    #     return [self.tupla_para_veiculo(v) for v in veiculos]


    def atualizar(self, id: int, veiculo_atualizado: Veiculo):
        sql = "UPDATE veiculo SET marca = %s, modelo = %s, ano = %s, placa = %s WHERE id = %s"
        valores = (veiculo_atualizado.marca, veiculo_atualizado.modelo,
                   veiculo_atualizado.ano, veiculo_atualizado.placa, id)
        self.cursor.execute(sql, valores)
        self.connection.commit()
        print("Veículo atualizado com sucesso.")

    # def delete_veiculo(self, id: int):
    #     sql = "DELETE FROM veiculo WHERE id = %s"
    #     self.cursor.execute(sql, (id,))
    #     self.connection.commit()
    #     print("Veículo deletado com sucesso.")