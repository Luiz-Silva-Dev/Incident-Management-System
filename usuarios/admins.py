def toStringOCO():
    import sqlite3
    import func.ocorrencias as oco

    
    class Ocorrencia():
        def __init__(self, cpf, endereco, numero, cep, tipo, prioridade, estado):
            self.cpf = cpf
            self.endereco = endereco
            self.numero = numero
            self.cep = cep
            self.tipo = tipo
            self.prioridade = prioridade
            self.estado = estado

    i = 0

    conect = sqlite3.connect('./ocorrencias.db')


    program = f"select * from casos;"
    cursor = conect.cursor()
    cursor.execute(program)
    rows = cursor.fetchall()

    list_oco = []
    for cep, cpf, endereco, estado, numero, prioridade, tipo in rows:
        ocorrencia = Ocorrencia(cpf, endereco, numero, cep, tipo, prioridade, estado)
        list_oco.append(ocorrencia)
        i+=1

        print(f'''---------------------------------------------------------------------------------------
Ocorrencia {i}:
Cpf do Usuario: {ocorrencia.cpf}
Tipo: {ocorrencia.tipo}
Prioridade: {ocorrencia.prioridade}
Endereco: {ocorrencia.endereco}, {ocorrencia.numero}, {ocorrencia.cep}
Estado: {ocorrencia.estado}''')

def apagar_ocorrencia():
    import sqlite3
    import func.cadastro as cad
    import func.ocorrencias as oco
    toStringOCO()

    conect = sqlite3.connect('./ocorrencias.db')

    cursor = conect.cursor()

    print('Insira os dados de qual ocorrencia deseja selecionar como selecionada:')
    while True:
        cpf = input('Digite o cpf da ocorrencia: ')
        if cad.validar_cpf(cpf):
             break
        else:
             print('Cpf invalido!')
    while True:
        tipo = input('''Informe qual o numero da calsa da ocorrencia:
1)Lixo
2)Inundacao
3)Buracos
4)Acidente
5)Fogo
6)Dengue
7)Falta de Recursos 
Tipo de ocorrencia: ''')
        if tipo == '1':
            prioridade = oco.lixo()
            break
        elif tipo == '2':
            prioridade = oco.inundacao()
            break
        elif tipo == '3':
            prioridade = oco.buraco()
            break
        elif tipo == '4':
            prioridade = oco.acidente()
            break
        elif tipo == '5':
            prioridade = oco.fogo()
            break
        elif tipo == '6':
            prioridade = oco.dengue()
            break
        elif tipo == '7':
            prioridade = oco.frb()
            break
        else:
            print('Opcao invalida!')
            continue
    program = (f"delete from casos as C where cpf = '{cpf}' and tipo = {tipo} and prioridade = {prioridade};")
    cursor.execute(program)
    conect.commit()

    cursor.close()
    conect.close()

    print('Ocorrencia apagada com sucesso!')
    toStringOCO()

def admin_menu():
    import sqlite3
    import func.cadastro as cad

    while True:
        select = input('''
Menu Administrativo:
1)Visualizar Ocorrencias Gerais
2)Apagar Ocorrencias
3)Mudar Login
4)Adicionar Administrador
5)Encerrar
Selecione: ''')
        
        if select == '1':
            toStringOCO()
        elif select ==  '2':
            apagar_ocorrencia()
        elif select == '3':
            conect = sqlite3.connect('./ocorrencias.db')

            while True:
                novo_id = input('Digite seu novo ID: ')
                if cad.validar_id_admin(novo_id):
                    break
                else:
                    print('Id ja esta em uso!')
                    continue
            while True:
                nova_senha = input('Digite sua nova senha: ')
                if cad.validar_senha(nova_senha):
                        break
                else: 
                    print('Senha Invalida!')
                    continue

            while True:
                cpf = input('Digite se cpf de confirmacao: ')
                if cad.validar_cpf(cpf):
                    break
                else:
                    print('Cpf Invalido!')
                    continue

            program = f"select * from admins where cpf = '{cpf}' ;"
            cursor = conect.cursor()
            cursor.execute(program)
            rows = cursor.fetchall()

            nomes_usuarios = ''
            senhas = ''
            for cpf2, senha, nome in rows:
                if cpf2 == cpf:
                    nomes_usuarios = nome
                    senhas = senha

            program2 = f"update admins set usuario = '{novo_id}',  senha = '{nova_senha}' where cpf = '{cpf}' and usuario = '{nomes_usuarios}' and senha = '{senhas}';"
            cursor.execute(program2)
            conect.commit()

            cursor.close()
            conect.close()
            print('Dados atualizados com sucesso')
        elif select == '4':
            cad.cadas_admin()
        elif select == '5':
            break
        else:
            print('Opcao invalida!')
            continue