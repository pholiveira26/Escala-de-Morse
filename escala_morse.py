import os 

def duas_opcoes():
    limpar_tela()
    print('\033[1;31;47mNESTA OPÇÃO SÓ SÃO VÁLIDOS OS NÚMEROS 1 E 2. POR FAVOR, TENTE NOVAMENTE!\033[m')

def tres_opcoes():
    limpar_tela()
    print('\033[1;31;47mNESTA OPÇÃO SÓ SÃO VÁLIDOS OS NÚMEROS 1, 2 E 3. POR FAVOR, TENTE NOVAMENTE!\033[m')

def limpar_tela():
    # Limpa a tela no Windows e no Linux/Mac
    os.system('cls' if os.name == 'nt' else 'clear')

def pula_linha():
    print('-=' *30)

def texto_tela(item):
    print(item)

texto_queda = '[1] cliente sem histórico de quedas nos últimos 3 meses\n\
[2] Queda durante o período de internação ou histórico recente por fatores fisiológicos nos últimos 3 meses'

texto_diagnostico_secundario = '[1] Não\n\
[2] Sim'

texto_mobilidade = '[1] Nenhum/Acamado/Repouso no leito \n\
[2] Bengala/Muleta\n\
[3] Mobiliário ou parede'

texto_terapia_endovenosa = '[1] Não \n\
[2] Sim'

texto_marcha = '[1] Normal/Acamado/Cadeira de rodas \n\
[2] Lenta/Fraca\n\
[3] Alterada/Cambaleante'

texto_estado_mental = '[1] Orientado\n\
[2] Desorientado/Confuso'

while True:
    classificacao_de_risco = 0

    pula_linha()
    print('-' * 20, 'ESCALA DE MORSE', '-' * 20)
    print('\033[0;30;44mHISTÓRICO DE QUEDAS: \033[m') # Aqui eu posso colocar em cores, ou outra forma que chame a atenção

    texto_tela(texto_queda)
    queda = int(input('-------------> PONTUAÇÃO: '))

    if queda == 1:
        classificacao_de_risco += 0

    elif queda == 2:
        classificacao_de_risco += 25

    else:
        duas_opcoes()
        continue

# NOVA LINHA DE CÓDIGO
    pula_linha()
    print('\033[0;30;44mDIAGNÓSTICO SECUNDÁRIO\033[m')
    texto_tela(texto_diagnostico_secundario)
    diagnostico_secundario = int(input(('-------------> PONTUAÇÃO: ')))

    if diagnostico_secundario == 1:
        classificacao_de_risco += 0

    elif diagnostico_secundario == 2:
        classificacao_de_risco += 15

    else:
        duas_opcoes()
        continue

# NOVA LINHA DE CÓDIGO:
    pula_linha()
    print('\033[0;30;44mAUXÍLIO NA MOBILIDADE:\033[m')
    texto_tela(texto_mobilidade)
    mobilidade = int(input(('-------------> PONTUAÇÃO: ')))

    if mobilidade == 1:
        classificacao_de_risco += 0

    elif mobilidade == 2:
        classificacao_de_risco += 15

    elif mobilidade == 3:
        classificacao_de_risco += 30

    else:
        tres_opcoes()
        continue


    pula_linha()
    print('\033[0;30;44mTERAPIA ENDOVENOSA:\033[m')
    texto_tela(texto_terapia_endovenosa)
    terapia_endovenosa = int(input('-------------> PONTUAÇÃO: '))

    if terapia_endovenosa == 1:
        classificacao_de_risco += 0

    elif terapia_endovenosa == 2:
        classificacao_de_risco += 20

    else:
        duas_opcoes()
        continue


    pula_linha()
    print('\033[0;30;44mMARCHA:\033[m')
    texto_tela(texto_marcha)
    marcha =  int(input('-------------> PONTUAÇÃO: '))

    if marcha == 1:
        classificacao_de_risco += 0

    elif marcha == 2:
        classificacao_de_risco += 10

    elif marcha == 3:
        classificacao_de_risco += 20

    else:
        tres_opcoes()
        continue


    pula_linha()
    print('\033[0;30;44mESTADO MENTAL:\033[m')
    texto_tela(texto_estado_mental)
    estado_mental = int(input('-------------> PONTUAÇÃO: '))

    if estado_mental == 1:
        classificacao_de_risco += 0

    elif estado_mental == 2:
        classificacao_de_risco += 15

    else:
        duas_opcoes()
        continue

    pula_linha
    if classificacao_de_risco >= 0 and classificacao_de_risco <= 24:
        print('\033[1;32;40mESSE PACIENTE APRESENTA BAIXO RISCO DE QUEDA\033[m')

    elif classificacao_de_risco >= 25 and classificacao_de_risco <= 44:
        print('\033[1;33;40mESSE PACIENTE APRESENTA RISCO MODERADO DE QUEDA\033[m')
    
    else:
        print('\033[1;31;40mESSE PACIENTE APRESENTA RISCO ELEVADO DE QUEDA\033[m')
    break

print(f'O resultado da soma dos itens foi de {classificacao_de_risco}')
