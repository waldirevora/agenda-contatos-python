# Agenda Contatos Python - Fundamentos Python | Rocketseat

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
        print ("Adicionar contato")

    elif opcao == "2":
        print ("Listar contatos")

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