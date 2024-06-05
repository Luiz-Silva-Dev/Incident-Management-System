
def test_user(usuario_inserido, senha_inserida):
    import sqlite3

    conect = sqlite3.connect('./ocorrencias.db')

    cursor = conect.cursor()

    program = f"select senha, usuario from users where senha = '{senha_inserida}' and usuario = '{usuario_inserido}';"
    cursor = conect.cursor()
    cursor.execute(program)
    rows = cursor.fetchall()

    for senha, nome in rows:
        nome_usuario = nome
        senhas = senha

    cursor.close()
    conect.close()

    if usuario_inserido == nome_usuario:
        if senha_inserida == senhas:
            print("Acesso concedido! Bem-vindo, usuário.")
            return True
        else:
            print("Senha incorreta. Tente novamente.")
            return False
    else:
        print("Usuário não encontrado. Verifique o nome de usuário.")
        return False


def test_admin(usuario_inserido, senha_inserida):
    import sqlite3

    conect = sqlite3.connect('ocorrencias.db')

    cursor = conect.cursor()

    program = f"select senha, usuario from admins where senha = '{senha_inserida}' and usuario = '{usuario_inserido}';"
    cursor = conect.cursor()
    cursor.execute(program)
    rows = cursor.fetchall()

    for senha, nome in rows:
        nome_usuario = nome
        senhas = senha

    cursor.close()
    conect.close()

    if usuario_inserido == nome_usuario:
        if senha_inserida == senhas:
            print("Acesso concedido! Bem-vindo, Administrador.")
            return True
        else:
            print("Senha incorreta. Tente novamente.")
            return False
    else:
        print("Usuário não encontrado. Verifique o nome de administrador.")
        return False


