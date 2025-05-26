from Cliente import Cliente
from Veiculo import Veiculo

import CrudOperations

def menu():
    print("Estacionamento:")
    print("1. Cadastrar C")

def main():
    crud = CrudOperations.CRUD()

    while True:
        opcao = input("Choose your destiny:")
        if opcao == 1:
            nome = input()
            endereco = input()
            cpf = input()
            telefone = input()

            cliente = Cliente(nome, endereco, cpf, telefone)
            crud.create_cliente(cliente)

        elif opcao == 2:
            crud.all_clientes()

        elif opcao == 3:
            exit()


if __name__ == '__main__':
    main()
