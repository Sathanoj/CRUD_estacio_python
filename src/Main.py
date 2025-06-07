from Cliente import Cliente
from Veiculo import Veiculo

from CrudOperations import CRUD
from src.CrudCliente import CurdCliente
from src.CrudVeiculo import CRUDVeiculo



configuration = {
    "host": "localhost",
    "database": "estacionamento",
    "user": "root",
    "password": "12345"
}

def menu():
    print("\n--- Estacionamento ---")
    print("1. Cadastrar Cliente")
    print("2. Selecionar Cliente pelo ID")
    print("3. Listar todos os Clientes")
    print("4. Atualizar Cliente")
    print("5. Deletar Cliente")
    print("6. Cadastrar Veículo para Cliente")
    print("7. Listar Veículos de um Cliente")
    print("8. Atualizar Veículo")
    print("9. Deletar Veículo")
    print("0. Sair")


def voltar_para_menu():
    escolha = input("Voltar para o menu principal? (Y/N) ")
    if escolha == "Y":
        main()
    elif escolha == "N":
        print("Programa finalizado!")
        exit()

def main():
    menu()
    crud_cliente = CurdCliente(configuration)
    crud_veiculo = CRUDVeiculo(configuration)

    while True:
        opcao = int(input("Escolha uma opcao:"))

        if opcao == 1:
            nome = input("Nome do cliente: ")
            endereco = input("Endereco do cliente: ")
            cpf = input("CPF do cliente: ")
            telefone = input("Telefone do cliente: ")

            cliente = Cliente(nome, endereco, cpf, telefone)
            crud_cliente.create(cliente)

        elif opcao == 2:
            cliente_id = int(input("qual o id do usuario? "))
            print("Qual cliente vai cadastrar o Carro? ")
            crud_cliente.get_by_id(cliente_id)

        elif opcao == 3:
            crud_cliente.all()

        elif opcao == 4:
            cliente_id = int(input("qual o id do usuario? "))
            cliente_existe = crud_cliente.get_by_id(cliente_id)
            if not cliente_existe:
                print(f"Cliente {cliente_id} não encontrado.")
                voltar_para_menu()

            print(f"Atualizando cliente: {cliente_existe[1]}")
            nome = input("Nome do cliente: ")
            endereco = input("Endereco do cliente: ")
            cpf = input("CPF do cliente: ")
            telefone = input("Telefone do cliente: ")

            cliente = Cliente(nome, endereco, cpf, telefone)
            crud_cliente.atualizar(cliente_id, cliente)


        elif opcao == 5:
            cliente_id = int(input("qual cliente voce quer deletar? "))
            crud_cliente.delete(cliente_id)
        # veiculo
        #
        elif opcao == 6:
            cliente_id = int(input("ID do cliente para cadastrar veículo: "))
            cliente_existe = crud_cliente.get_by_id(cliente_id)
            if not cliente_existe:
                print(f"Cliente {cliente_id} não encontrado.")
                voltar_para_menu()

            marca = input("Marca do veículo: ")
            modelo = input("Modelo do veículo: ")
            ano = input("Ano do veículo: ")
            placa = input("Placa do veículo: ")
            veiculo = Veiculo(marca, modelo, ano, placa, cliente_id)
            crud_veiculo.create(veiculo, cliente_id)

        elif opcao == 7:
            cliente_id = int(input("ID do cliente para listar veículos: "))
            resposta = crud_veiculo.veiculos_por_cliente(cliente_id)
            if resposta:
                print(f"Veículos do cliente {cliente_id}:")
                for v in resposta:
                    print(v)
            else:
                print("Nenhum veículo encontrado para este cliente.")

        # elif opcao == 8:
        #     veiculo_id = int(input("ID do veículo para atualizar: "))
        #     marca = input("Nova marca do veículo: ")
        #     modelo = input("Novo modelo do veículo: ")
        #     ano = input("Novo ano do veículo: ")
        #     placa = input("Nova placa do veículo: ")
        #     veiculo_atualizado = Veiculo(marca, modelo, ano, placa)
        #     crud_veiculo.atualizar(veiculo_id, veiculo_atualizado)
        #
        # elif opcao == 9:
        #     veiculo_id = int(input("ID do veículo para deletar: "))
        #     crud_veiculo.delete(veiculo_id)


if __name__ == '__main__':
    main()
