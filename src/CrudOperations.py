
from DataBaseManeger import DataBaseManager
from src.Cliente import Cliente


class CRUD:
    def __init__(self, table, configuration):
        self.table = table
        self.db = DataBaseManager(**configuration)
        self.connection = self.db.connect()
        self.cursor = self.connection.cursor()

    def all(self):
        self.cursor.execute(f"SELECT * FROM {self.table}")
        clientes = self.cursor.fetchall()
        for cliente in clientes:
            print(cliente)

    def get_by_id(self, id : int):
        sql = f"SELECT * FROM {self.table} WHERE id = %s"
        self.cursor.execute(sql, (id,))
        resultado = self.cursor.fetchone()
        print(resultado)

    def delete(self, id : int):
        self.cursor.execute(f"DELETE FROM {self.table} WHERE id = %s", (id,))
        self.connection.commit()

