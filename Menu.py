from program.func.login import *
from program.func.cadastro import *
from program.usuarios.admins import *
from program.usuarios.user import *

while True:
    escolha1 = input("""
Bem vindo ao sistema de ocorrencias!
1)Login
2)Cadastro   
O que deseja fazer: """)

    if (escolha1 == "1" or escolha1 == 1):
        break
    elif (escolha1 == "2" or escolha1 == 2):
        cadas_user()
        break
    else:
        print("Escolha invalida!")
        continue

while True:
        escolha = input("Logar como ? 1)Administrador 2)Usuario :")
        if (escolha == "1" or escolha == 1):
            usuario_inserido = input("Digite o nome de administrador: ")
            senha_inserida = input("Digite a senha: ")
            if test_admin(usuario_inserido, senha_inserida):
                user = 1
                break
            else:
                continue
        elif (escolha == "2" or escolha == 2):
            usuario_inserido = input("Digite o nome de usuário: ")
            senha_inserida = input("Digite a senha: ")
            if test_user(usuario_inserido, senha_inserida):
                user = 2
                break
            else:
                continue
        else:
            print("Forma de login invalida")
            continue

match user:
    case 1:
        admin_menu()
    case 2:
        usuario_menu()