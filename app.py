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

# Editar contato
def editar_contato(contatos):
    if not contatos:
        print()
        print("Nenhum contato cadastrado.")
        return

    listar_contatos(contatos)

    try:
        indice = int(input("\nDigite o número do contato que deseja editar: ")) - 1

        if indice < 0 or indice >= len(contatos):
            print("Contato não encontrado.")
            return

        contato = contatos[indice]

        print()
        nome = input(f"Nome ({contato['nome']}): ").strip()
        telefone = input(f"Telefone ({contato['telefone']}): ").strip()
        email = input(f"E-mail ({contato['email']}): ").strip()

        if nome:
            contato["nome"] = nome

        if telefone:
            contato["telefone"] = telefone

        if email:
            contato["email"] = email

        print()
        print("Contato atualizado com sucesso.")

    except ValueError:
        print()
        print("Digite um número válido.")

# Controle de favoritos
def alternar_favorito(contatos):
    if not contatos:
        print()
        print("Nenhum contato cadastrado.")
        return

    listar_contatos(contatos)

    try:
        indice = int(input("\nDigite o número do contato: ")) - 1

        if indice < 0 or indice >= len(contatos):
            print("Contato não encontrado.")
            return

        contato = contatos[indice]

        contato["favorito"] = not contato["favorito"]

        print()

        if contato["favorito"]:
            print("Contato marcado como favorito.")
        else:
            print("Contato removido dos favoritos.")

    except ValueError:
        print()
        print("Digite um número válido.")

# Listar favoritos
def listar_favoritos(contatos):
    if not contatos:
        print()
        print("Nenhum contato cadastrado.")
        return

    print()
    print("Contatos favoritos:")

    favoritos_encontrados = False

    for indice, contato in enumerate(contatos, start=1):
        if contato["favorito"]:
            favoritos_encontrados = True

            print(
                f"{indice}. {contato['nome']} | "
                f"{contato['telefone']} | "
                f"{contato['email']}"
            )

    if not favoritos_encontrados:
        print("Nenhum contato favorito.")

# Apagar contato
def apagar_contato(contatos):
    if not contatos:
        print()
        print("Nenhum contato cadastrado.")
        return

    listar_contatos(contatos)

    try:
        indice = int(input("\nDigite o número do contato que deseja apagar: ")) - 1

        if indice < 0 or indice >= len(contatos):
            print("Contato não encontrado.")
            return

        contato_removido = contatos.pop(indice)

        print()
        print(f"Contato {contato_removido['nome']} apagado com sucesso.")

    except ValueError:
        print()
        print("Digite um número válido.")

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
        editar_contato(contatos)

    elif opcao == "4":
        alternar_favorito(contatos)

    elif opcao == "5":
        listar_favoritos(contatos)

    elif opcao == "6":
        apagar_contato(contatos)

    else:
        print ("Opção inválida.")