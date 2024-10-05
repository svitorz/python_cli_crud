import crud


def execute_command(comando):
    if comando == 1:
        users = crud.list_users()
        if users:
            for user in users:
                print(user)
        else:
            print("Nenhum usuário encontrado")


def cli():
    table = crud.create_table()

    if table is not True:
        return

    try:
        escolha = int(
            input(
                "Digite um número para a operação que deseja realizar: \n1-Listar  usuários.\n2-Inserir novo usuário.\n3-Editar usuário.\n4-Excluir usuário.\n5-Ver informações de usuário\n"
            )
        )
    except ValueError:
        print("Insira um valor válido")
        return

    execute_command(escolha)


cli()
