# Agenda Contatos Python - Fundamentos Python | Rocketseat

# Adicionar contatos
contatos = []

def adicionar_contato(contatos):
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("E-mail: ")

    contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "favorito": False
    }

    contatos.append(contato)

    print()
    print("Contato adicionado com sucesso.")

# Listar contatos
def listar_contatos(contatos):
    if not contatos:
        print()
        print("Nenhum contato cadastrado")
        return

    print()
    print("Contatos cadastrados:")

    for indice, contato in enumerate(contatos, start=1):
        print(
            f"{indice}. {contato['nome']} | "
            f"{contato['telefone']} | "
            f"{contato['email']}"
        )

# Menu interativo
while True:
    print ()
    print ("Agenda de contatos")
    print ()
    print ("1. Adicionar contato")
    print ("2. Listar contatos")
    print ("3. Editar contato")
    print ("4. Marcar ou desmarcar contato como favorito")
    print ("5. Listar contatos favoritos")
    print ("6. Apagar contato")
    print ("0. Sair")
    print ()

    opcao = input("Escolha uma opção: ")
    print ()

    if opcao == "0":
        print ("Programa encerrado.")
        print ()
        break

    elif opcao == "1":
        adicionar_contato(contatos)

    elif opcao == "2":
        listar_contatos(contatos)

    elif opcao == "3":
        print ("Editar contato")

    elif opcao == "4":
        print ("Marcar ou desmarcar contato como favorito")

    elif opcao == "5":
        print ("Listar contatos favoritos")

    elif opcao == "6":
        print ("Apagar contato")

    else:
        print ("Opção inválida.")