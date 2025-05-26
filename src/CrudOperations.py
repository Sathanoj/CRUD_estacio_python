
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

    def create_cliente(self, cliente: Cliente):

        sql = "INSERT INTO clientes (nome, endereco, cpf, telefone) VALUES (%s, %s, %s, %s);"
        valores = (cliente.nome, cliente.endereco, cliente.cpf, cliente.telefone)
        self.cursor.execute(sql,valores)
        self.connection.commit()
        print("Cliente salvo com sucesso!")


    def all_clientes(self):
        self.cursor.execute("SELECT * FROM clientes;")
        clientes = self.cursor.fetchall()
        for x in clientes:
            print(x)

    def cliente_ID(self):
        self.cursor.execute("SELECT cliente where id")
