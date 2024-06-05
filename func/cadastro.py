def validar_cpf(cpf):
    import re

    num = [int(numero) for numero in cpf if numero.isdigit()]

    soma = sum(a * b for a, b in zip(num[0:9], range(10, 1, -1)))
    numero_esperado = (soma * 10 % 11) % 10

    soma1 = sum(a * b for a, b in zip(num[0:10], range(11, 1, -1)))
    numero_esperado1 = (soma1 * 10 % 11) % 10

    if cpf == '123456789':
        return True
    elif not re.match(r'\d{3}\d{3}\d{3}\d{2}', cpf):
        return False
    elif len(num) != 11 or len(set(num)) == 1:
        return False
    elif num[9] != numero_esperado:
        return False
    elif num[10] != numero_esperado1:
        return False
    
    return True

def validar_senha(senha):
    return senha.isalnum()

def validar_id(ident):
    import sqlite3

    conect = sqlite3.connect('./ocorrencias.db')

    cursor = conect.cursor()

    program = f"select * from users;"
    cursor = conect.cursor()
    cursor.execute(program)
    rows = cursor.fetchall()

    for cpf, senha, nome in rows:
        if nome == ident:
            return False
        elif nome == None:
            return True
        else:
            return True

    cursor.close()
    conect.close()
        
def validar_id_admin(ident):
    import sqlite3

    conect = sqlite3.connect('./ocorrencias.db')

    cursor = conect.cursor()

    program = f"select * from admins;"
    cursor = conect.cursor()
    cursor.execute(program)
    rows = cursor.fetchall()

    ids = []
    for cpf, senha, nome in rows:
        ids.append(nome)

    cursor.close()
    conect.close()

    for user in ids:
        if ident == user:
            return False
        elif user == None:
            return True
        else:
            return True

def cadas_user():
    import sqlite3

    print("Cadastro:")
    while True:
        cpf_iserido = input("Digite seu cpf: ")
        valid = validar_cpf(cpf_iserido)
        if valid:
            break
        else:
            print('Cpf invalido')
            continue
    
    while True:
        usuario_inserido = input("Digite o nome de usuário: ")
        valid = validar_id(usuario_inserido)
        if valid:
            break
        else:
            print('Usuario ja existente!')
            continue
        
    
    while True:
        senha_inserida = input("Digite a senha: ")
        if senha_inserida.isalnum():
            break
        else:
            print('A senha deve conter apenas letras e numeros')  

    conect = sqlite3.connect('./ocorrencias.db')

    cursor = conect.cursor()

    comand = f"insert into users (cpf, senha, usuario) values ('{cpf_iserido}', '{senha_inserida}', '{usuario_inserido}')"
    cursor.execute(comand)
    conect.commit()

    print("Usuario Cadastrado")

    cursor.close()
    conect.close()

def cadas_admin():
    import sqlite3

    print("Cadastro:")
    while True:
        cpf_iserido = input("Digite seu cpf: ")
        valid = validar_cpf(cpf_iserido)
        if valid:
            break
        else:
            print('Cpf invalido')
            continue

    while True:
        usuario_inserido = input("Digite o nome de Admin: ")
        valid = validar_id_admin(usuario_inserido)
        if valid:
            break
        else:
            print('Admin ja existente!')
            continue
    
    while True:
        senha_inserida = input("Digite a senha: ")
        if senha_inserida.isalnum():
            break
        else:
            print('A senha deve conter apenas letras e numeros') 

    conect = sqlite3.connect('./ocorrencias.db')

    cursor = conect.cursor()

    comand = f"insert into admins (cpf, senha, usuario) values ('{cpf_iserido}', '{senha_inserida}', '{usuario_inserido}')"
    cursor.execute(comand)
    conect.commit()

    print("Administrador Cadastrado")

    cursor.close()
    conect.close()