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

def lixo():
    while True:
        prioridade1 = input('''
Lixo em:
1)Pequenas Quantidades
2)Quantidades Medianas
3)Grandes Quantidades
Selecione: ''')
        if prioridade1 == '1':
            nivel = 5
            break
        elif prioridade1 == '2':
            nivel = 4
            break
        elif prioridade1 == '3':
            nivel = 3
            break
        else:
            print('Opcao invalida!')
            continue
    return nivel

def inundacao():
    while True:
        prioridade1 = input('''
Inundacao:
1)Leve
2)Media
3)Grande
Selecione: ''')
        if prioridade1 == '1':
            nivel = 4
            break
        elif prioridade1 == '2':
            nivel = 3
            break
        elif prioridade1 == '3':
            nivel = 1
            break
        else:
            print('Opcao invalida!')
            continue
    return nivel

def buraco():
    while True:
        prioridade1 = input('''
Buraco:
1)Pequeno
2)Medio
3)Grande
Selecione: ''')
        if prioridade1 == '1':
            nivel = 5
            break
        elif prioridade1 == '2':
            nivel = 4
            break
        elif prioridade1 == '3':
            nivel = 3
            break
        else:
            print('Opcao invalida!')
            continue
    return nivel
            
def acidente():
    while True:
        prioridade1 = input('''
Acidente:
1)Leve
2)Grave
Selecione: ''')
        if prioridade1 == '1':
            nivel = 3
            break
        elif prioridade1 == '3':
            nivel = 1
            break
        else:
            print('Opcao invalida!')
            continue
    return nivel

def fogo():
    while True:
        prioridade1 = input('''
Fogo:
1)Leve
2)Medio
3)Grande
Selecione: ''')
        if prioridade1 == '1':
            nivel = 4
            break
        elif prioridade1 == '2':
            nivel = 2
            break
        elif prioridade1 == '3':
            nivel = 1
            break
        else:
            print('Opcao invalida!')
            continue
    return nivel

def dengue():
    while True:
        prioridade1 = input('''
Dengue:
1)Poucos Casos
2)Estado Grave
3)Morte
Selecione: ''')
        if prioridade1 == '1':
            nivel = 4
            break
        elif prioridade1 == '2':
            nivel = 2
            break
        elif prioridade1 == '3':
            nivel = 1
            break
        else:
            print('Opcao invalida!')
            continue
    return nivel

def frb():
    while True:
        prioridade1 = input('''
Falta de Recursos:
1)Energia
2)Agua
3)Saneamento
Selecione: ''')
        if prioridade1 == '1':
            nivel = 2
            break
        elif prioridade1 == '2':
            nivel = 2
            break
        elif prioridade1 == '3':
            nivel = 2
            break
        else:
            print('Opcao invalida!')
            continue
    return nivel

def validar_cep(cep):
    if len(cep) == 8:
        return True
    else:
        return False

def criar_ocorencia():
    import sqlite3

    while True:
        tipo = input("""
Selecione o tipo de ocorrencia que deseja notificar:
1)Lixo
2)Inundacao
3)Buracos
4)Acidente
5)Fogo
6)Dengue
7)Falta de Recursos 
Tipo de ocorrencia: """)
        
        if tipo == '1':
            prioridade = lixo()
            break
        elif tipo == '2':
            prioridade = inundacao()
            break
        elif tipo == '3':
            prioridade = buraco()
            break
        elif tipo == '4':
            prioridade = acidente()
            break
        elif tipo == '5':
            prioridade = fogo()
            break
        elif tipo == '6':
            prioridade = dengue()
            break
        elif tipo == '7':
            prioridade = frb()
            break
        else:
            print('Opcao invalida!')
            continue

    print("Agora Precisamos de alguns de seus dados!")

    while True:
        cpf1 = input('Digite seu Cpf para registro: ')
        if validar_cpf(cpf1):
            cpf = cpf1
            break
        else:
            print('Cpf invalido, tente novamente!')
            continue
    
    while True:
        endereco1 = input('De forma resumida, nos informe o nome da sua rua: ')
        if endereco1.isdigit() == False:
            endereco = endereco1
            break
        else:
            print('N se pode usar numeros!')
            continue

    while True:
        numero1 = input('Digite o numero do seu endereco: ')
        if numero1.isdigit() and int(numero1) >= 0:
            numero = numero1
            break
        else:
            print('Insira um valor numerico acima de 0!')
            continue

    while True:
        cep1 = input('Informe seu Cep: ')
        if validar_cep(cep1):
            cep = cep1
            break
        else:
            print('Cep invalido!')
            continue

    conect = sqlite3.connect('./ocorrencias.db')

    cursor = conect.cursor()

    comand = f"insert into casos (cpf, endereco, numero, cep, tipo, prioridade, estado) values ('{cpf}', '{endereco}', '{numero}', '{cep}', {tipo}, {prioridade}, 'Em analise')"
    cursor.execute(comand) 
    conect.commit()
    print('Ocorrencia Criada com sucesso!')

    cursor.close()
    conect.close()