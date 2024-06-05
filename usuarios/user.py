def toStringOCO(cpf):
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


    program = f"select * from casos as A where A.cpf = '{cpf}' ;"
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
Tipo {ocorrencia.tipo}
Prioridade: {ocorrencia.prioridade}
Endereco: {ocorrencia.endereco}, {ocorrencia.numero}, {ocorrencia.cep}
Estado: {ocorrencia.estado}''')

def usuario_menu():
    from func.ocorrencias import criar_ocorencia
    import sqlite3
    import func.cadastro as cad

    while True:
        select = input('''
Menu Usuario:
1)Adicionar uma Ocorrencia
2)Alterar dados de login
3)Visualizar Ocorrencias Feitas
4)Encerrar
Selecione: ''')
        
        if select == '1':
            criar_ocorencia()
        elif select ==  '2':
            conect = sqlite3.connect('ocorrencias.db')

            while True:
                novo_id = input('Digite seu novo ID: ')
                if cad.validar_id(novo_id):
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

            program = f"select * from users where cpf = '{cpf}' ;"
            cursor = conect.cursor()
            cursor.execute(program)
            rows = cursor.fetchall()

            nomes_usuarios = ''
            senhas = ''
            for cpf2, senha, nome in rows:
                if cpf2 == cpf:
                    nomes_usuarios = nome
                    senhas = senha
                    
            program2 = f"update users set usuario = '{novo_id}',  senha = '{nova_senha}' where cpf = '{cpf}' and usuario = '{nomes_usuarios}' and senha = '{senhas}';"
            cursor.execute(program2)
            conect.commit()

            cursor.close()
            conect.close()
            print('Dados atualizados com sucesso')
        elif select == '3':
            while True:
                cpf = input('Digite se cpf de confirmacao: ')
                if cad.validar_cpf(cpf):
                    break
                else:
                    print('Cpf Invalido!')
                    continue
            toStringOCO(cpf)
        elif select == '4':
            break
        else:
            print('Opcao invalida!')
            continue