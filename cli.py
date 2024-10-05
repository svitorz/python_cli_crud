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
                print("Nenhum usuário encontrado")
        case 2:
            insert = False
            try:
                name = input("Insira seu nome:")
                email = input("\nInsira seu email:")
                password = input("\nInsira sua senha:")

                insert = crud.insert_user(name, email, password)
                if insert is True:
                    print("Usuário inserido com sucesso!")
                else:
                    print("Erro ao inserir usuário!")
            except ValueError:
                print("Insira valores válidos.")

        case 3:
            try:
                update = False
                id = int(input("Insira o id do usuário que deseja editar:"))

                name = input("Insira o novo nome:")
                email = input("Insira o novo email:")
                password = input("Insira a nova senha:")
                update = crud.update_user(id, name, email, password)

                if update is True:
                    print("Usuário alterado com sucesso!")
                else:
                    print("Houve um erro ao editar usuário!")
            except ValueError:
                print("Insira valores válidos.")


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
            print("Insira um valor válido")
            return
        execute_command(escolha)
        if escolha == 0:
            break


cli()
