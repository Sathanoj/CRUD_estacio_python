from Cliente import Cliente
from Veiculo import Veiculo

import CrudOperations

def menu():
    print("Estacionamento:")
    print("1. Cliente")
    print("2. Veiculo")
    print("3. Listar")

def main():
    menu()
    crud = CrudOperations.CRUD()

    while True:
        opcao = int(input("Escolha uma opcao:"))

        if opcao == 1:
            nome = input("Nome do cliente: ")
            endereco = input("Endereco do cliente: ")
            cpf = input("CPF do cliente: ")
            telefone = input("Telefone do cliente: ")

            cliente = Cliente(nome, endereco, cpf, telefone)
            crud.create_cliente(cliente)

        elif opcao == 2:
            cliente_id = int(input("qual o id do usuario? "))
            print("Qual cliente vai cadastrar o Carro? ")
            crud.cliente_ID(cliente_id)

        elif opcao == 3:
            crud.all_clientes()

        elif opcao == 4:

            nome = input("Nome do cliente: ")
            endereco = input("Endereco do cliente: ")
            cpf = input("CPF do cliente: ")
            telefone = input("Telefone do cliente: ")

            cliente = Cliente(nome, endereco, cpf, telefone)
            crud.atualizar_cliente(2, cliente)


        elif opcao == 5:
            cliente_id = int(input("qual cliente voce quer deletar? "))
            crud.delete_cliente(cliente_id)
        else:
            print("Opcao invalida.")


if __name__ == '__main__':
    main()
