import mysql.connector
from mysql.connector import Error

class DataBaseManager:
    def __init__(self, host: str, database: str, user: str, password: str, port: int = 3306):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host = self.host,
                database = self.database,
                user = self.user,
                password = self.password,
                port = self.port
            )
            if self.connection.is_connected():
                print("Conexao MYSQL confirmada!")
                return self.connection
            return None
        except Error as e:
            print(f"Erro ao conectar: {e}")
            return False

    def execute_query(self, query, params, fetch):
        print("oi")
