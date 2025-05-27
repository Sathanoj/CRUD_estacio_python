# Sistema de Cadastro para Estacionamento

Este é um projeto simples de CRUD (Create, Read, Update, Delete) desenvolvido em Python para gerenciar **clientes** e **veículos** de um estacionamento. O sistema utiliza MySQL como banco de dados e interage com ele através da biblioteca `mysql-connector-python`.

## 📋 Funcionalidades

- Cadastro de clientes
- Cadastro de veículos vinculados aos clientes
- Listagem, edição e remoção de registros
- Relacionamento entre cliente e veículo com integridade referencial no banco de dados

## 🛠 Requisitos

- Python 3.12.3
- MySQL Server (latest)
- Biblioteca MySQL Connector para Python

Você pode instalar o conector MySQL com:

```bash
pip install mysql-connector-python
```
⚙️ Configuração do Banco de Dados

- Crie um banco de dados no MySQL para o projeto.

- Utilize os comandos abaixo para criar as tabelas necessárias:

```
CREATE TABLE cliente (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    endereco VARCHAR(150),
    cpf VARCHAR(14) UNIQUE NOT NULL,
    telefone VARCHAR(20)
);

CREATE TABLE veiculo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    marca VARCHAR(50) NOT NULL,
    modelo VARCHAR(50) NOT NULL,
    ano INT NOT NULL,
    placa VARCHAR(10) UNIQUE NOT NULL,
    cliente_id INT,
    FOREIGN KEY (cliente_id) REFERENCES cliente(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
```

🚀 Como Usar

- Certifique-se de que o MySQL está em execução e o banco de dados está configurado corretamente.
    
- Clone este repositório ou baixe os arquivos.

- Edite a classe crudOperations com os dados corretos do seu banco.

- Execute o projeto pelo arquivo principal:

💡 Observações

- O projeto opera via terminal (modo texto).
- Pode ser facilmente expandido com interface gráfica (Tkinter, PyQt) ou API (Flask, FastAPI).