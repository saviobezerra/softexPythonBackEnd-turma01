from models.cliente import Cliente
from models.produto import Produto
from dao.cliente_dao import ClienteDAO
from dao.produto_dao import ProdutoDAO


dao_cliente = ClienteDAO()
dao_produto = ProdutoDAO()


def menu_principal():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Cadastrar Cliente")
        print("2 - Listar Clientes")
        print("3 - Cadastrar Produto")
        print("4 - Listar Produtos")
        print("5 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            cadastrar_cliente()
        elif opcao == "2":
            listar_clientes()
        elif opcao == "3":
            cadastrar_produto()
        elif opcao == "4":
            listar_produtos()
        elif opcao == "5":
            print("Encerrando...")
            break
        else:
            print("Opção inválida!")


def cadastrar_cliente():
    nome = input("Nome: ")
    email = input("Email: ")
    telefone = input("Telefone: ")

    cliente = Cliente(nome, email, telefone)
    dao_cliente.salvar(cliente)
    print("✅ Cliente cadastrado!")


def listar_clientes():
    clientes = dao_cliente.listar()
    print("\n=== LISTA DE CLIENTES ===")
    for c in clientes:
        print(c)


def cadastrar_produto():
    nome = input("Nome do produto: ")
    preco = float(input("Preço: "))

    produto = Produto(nome, preco)
    dao_produto.salvar(produto)
    print("✅ Produto cadastrado!")


def listar_produtos():
    produtos = dao_produto.listar()
    print("\n=== LISTA DE PRODUTOS ===")
    for p in produtos:
        print(p)


menu_principal() #inicia o programa
