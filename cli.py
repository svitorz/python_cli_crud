import crud


def execute_command(comando):
    match comando:
        case 1:
            users = crud.list_users()
            if users:
                for user in users:
                    name = user[0]
                    id = user[1]
                    print(f"\nId:{id} Nome:{name}\n")
            else:
                print("Nenhum usuário encontrado\n")
        case 2:
            insert = False
            try:
                name = input("Insira seu nome:\n")
                email = input("\nInsira seu email:\n")
                password = input("\nInsira sua senha:\n")

                insert = crud.insert_user(name, email, password)
                if insert is True:
                    print("Usuário inserido com sucesso!\n")
                else:
                    print("Erro ao inserir usuário!\n")
            except ValueError:
                print("Insira valores válidos.\n")

        case 3:
            try:
                update = False
                id = int(input("Insira o id do usuário que deseja editar:\n"))

                name = input("Insira o novo nome:")
                email = input("Insira o novo email:")
                password = input("Insira a nova senha:")
                update = crud.update_user(id, name, email, password)

                if update is True:
                    print("Usuário alterado com sucesso!\n")
                else:
                    print("Houve um erro ao editar usuário!\n")
            except ValueError:
                print("Insira valores válidos.\n")

        case 4:
            delete = False
            try:
                id = int(input("Insira o id do usuário que deseja excluir:\n"))
                delete = crud.delete_user(id)
                if delete is True:
                    print("Usuário excluído com sucesso!\n")
                else:
                    print("Erro ao exluir usuário\n")
            except ValueError:
                print("Insira um valor inteiro.\n")


def cli():
    table = crud.create_table()

    if table is not True:
        return

    while True:
        try:
            escolha = int(
                input(
                    "Digite um número para a operação que deseja realizar: \n1-Listar usuários.\n2-Inserir novo usuário.\n3-Editar usuário.\n4-Excluir usuário.\n5-Ver informações de usuário.\n0-Para encerrar a execução.\n"
                )
            )
        except ValueError:
            print("Insira um valor válido\n")
            return
        execute_command(escolha)
        if escolha == 0:
            break


cli()
