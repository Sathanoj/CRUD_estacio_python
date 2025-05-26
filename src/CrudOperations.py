
from DataBaseManeger import DataBaseManager
from src.Cliente import Cliente


class CRUD:
    def __init__(self):
        self.db = DataBaseManager(
            "localhost",
            "estacionamento",
            "root",
            "12345"
        )
        self.connection = self.db.connect()
        self.cursor = self.connection.cursor()



    def tupla_pra_cliente(self, tupla) -> Cliente:
        id_cliente, nome, endereco, cpf, telefone = tupla
        return Cliente(nome=nome, endereco = endereco, cpf = cpf, telefone = telefone)

    def create_cliente(self, cliente: Cliente):
        sql = "INSERT INTO cliente (nome, endereco, cpf, telefone) VALUES (%s, %s, %s, %s);"
        valores = (cliente.nome, cliente.endereco, cliente.cpf, cliente.telefone)
        self.cursor.execute(sql,valores)
        self.connection.commit()
        print("Cliente salvo com sucesso!")


    def all_clientes(self):
        self.cursor.execute("SELECT * FROM cliente;")
        clientes = self.cursor.fetchall()
        for x in clientes:
            print(x)

    def cliente_ID(self, id: int):
        sql = "SELECT * FROM cliente where id = %s"
        self.cursor.execute(sql, (id,))
        resultado = self.cursor.fetchone()
        print(resultado)
        return self.tupla_pra_cliente(resultado)


    def atualizar_cliente(self, id: int, cliente_atualizado: Cliente):
        cliente_antigo = self.cliente_ID(id)
        print(f"Atualizando cliente: {cliente_antigo.nome}")
        sql = "UPDATE cliente SET nome = %s, endereco = %s, cpf = %s, telefone = %s WHERE id = %s;"
        valores = (cliente_atualizado.nome, cliente_atualizado.endereco, cliente_atualizado.cpf, cliente_atualizado.telefone, id)
        self.cursor.execute(sql, valores)
        self.connection.commit()
        print("Cliente atualizado.")


    def delete_cliente(self, id: int):
        sql = "DELETE FROM cliente WHERE id = %s"
        valor = (id,)
        self.cursor.execute(sql, valor)
        self.connection.commit()
        print("Cliente Deletado!")
