from src import Cliente
from src.CrudOperations import CRUD


class CurdCliente(CRUD):
    def __init__(self, configuration):
        super().__init__("cliente",configuration)


    def tupla_pra_cliente(self, tupla) -> Cliente:
        id_cliente, nome, endereco, cpf, telefone = tupla
        return Cliente(nome=nome, endereco=endereco, cpf=cpf, telefone=telefone)

    def create(self, cliente: Cliente):
        sql = "INSERT INTO cliente (nome, endereco, cpf, telefone) VALUES (%s, %s, %s, %s);"
        valores = (cliente.nome, cliente.endereco, cliente.cpf, cliente.telefone)
        self.cursor.execute(sql,valores)
        self.connection.commit()
        print("Cliente salvo com sucesso!")

    def atualizar(self, id: int, cliente_atualizado: Cliente):
        cliente_antigo = self.get_by_id(id)

        sql = "UPDATE cliente SET nome = %s, endereco = %s, cpf = %s, telefone = %s WHERE id = %s"
        valores = (
            cliente_atualizado.nome,
            cliente_atualizado.endereco,
            cliente_atualizado.cpf,
            cliente_atualizado.telefone,
            id
        )
        self.cursor.execute(sql, valores)
        self.connection.commit()
        print("Cliente atualizado.")

    #
    # def delete_cliente(self, id: int):
    #     sql = "DELETE FROM cliente WHERE id = %s"
    #     valor = (id,)
    #     self.cursor.execute(sql, valor)
    #     self.connection.commit()
    #     print("Cliente Deletado!")