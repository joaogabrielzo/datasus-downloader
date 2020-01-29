from ftplib import FTP
import os


ftp = FTP(host='ftp.datasus.gov.br')
ftp.login()
download_path = '/dissemin/publicos'

info = sorted([
    'SIHSUS - Arquivos dissemináveis para tabulação do Sistema de Informações Hospitalares do SUS',
    'SIASUS - Arquivos dissemináveis para tabulação do Sistema de Informações Ambulatoriais do SUS',
    'SIM - Arquivos dissemináveis para tabulação do Sistema de informações de Mortalidade',
    'CIH - Arquivos dissemináveis para tabulação do Sistema de Comunicação de Informação Hospitalar',
    'CIHA - Arquivos dissemináveis para tabulação do Sistema de Comunicação de Informação Hospitalar e Ambulatorial',
    'SINASC - Arquivos dissemináveis para tabulação do Sistema de informação de Nascidos Vivos',
    'SISPRENATAL - Arquivos dissemináveis para tabulação do Sistema de Monitoramento e Avaliação do Pré-Natal, Parto, Puerpério e Criança',
    'SISAB - Arquivos dissemináveis para tabulação do Sistema de Informação em Saúde para a Atenção Básica.',
    'SINAN - Arquivos dissemináveis para tabulação do Sistema de agravos de notificação compulsória.'
])


for i in info:
    print(str(info.index(i)) + ') ' + str(i))


pasta = int(input('\nDigite o número da pasta que quer acessar: \n'))


if pasta == 8:
    folder = download_path + '/CMD'
else:
    folder = download_path + '/' + info[pasta].split(' -')[0]
ftp.cwd(folder)


dir_create = info[pasta].split(' -')[0]

actual_path = os.path.dirname(os.path.abspath(__file__))


if (info[pasta].split(' -')[0] == 'CIH') | (info[pasta].split(' -')[0] == 'CIHA') | (
        info[pasta].split(' -')[0] == 'SIHSUS') | (info[pasta].split(' -')[0] == 'SISPRENATAL'):
    for i in ftp.nlst():
        print(str(ftp.nlst().index(i)) + ') ' + str(i))
    choice = int(input("\nDigite o número da pasta que deseja acessar: \n"))

    new_dir = str(ftp.nlst()[choice]) + '_' + str(dir_create)
    if not os.path.exists(actual_path + '/' + str(new_dir)):
        os.mkdir(actual_path + '/' + str(new_dir))

    try:
        ftp.cwd(folder + '/' + ftp.nlst()[choice] + '/' + 'Dados')
    except BaseException:
        try:
            ftp.cwd(folder + '/' + ftp.nlst()[choice] + '/' + 'CSV')
        except BaseException:
            ftp.cwd(folder + '/' + ftp.nlst()[choice])

    for item in ftp.nlst():
        handle = open(actual_path + '/' + new_dir + '/' + str(item), 'wb')

    print('\nDownload em andamento.')

    ftp.retrbinary('RETR ' + ftp.nlst()[0], handle.write)


elif info[pasta].split(' -')[0] == 'SISAB':
    ftp.cwd(folder + '/DadosSISAB')

    new_dir = 'Dados_' + str(dir_create)
    if not os.path.exists(actual_path + '/' + str(new_dir)):
        os.mkdir(actual_path + '/' + str(new_dir))

    for item in ftp.nlst():
        handle = open(actual_path + '/' + new_dir + '/' + str(item), 'wb')

    print('\nDownload em andamento.')

    ftp.retrbinary('RETR ' + ftp.nlst()[0], handle.write)


elif info[pasta].split(' -')[0] == 'SIASUS':
    for i in ftp.nlst()[:2]:
        print(str(ftp.nlst().index(i)) + ') ' + str(i))
    choice = int(input("\nDigite o número da pasta que deseja acessar: \n"))

    new_dir = str(ftp.nlst()[choice]) + '_' + str(dir_create)
    if not os.path.exists(actual_path + '/' + str(new_dir)):
        os.mkdir(actual_path + '/' + str(new_dir))
    ftp.cwd(folder + '/' + ftp.nlst()[choice] + '/' + 'Dados')

    for item in ftp.nlst():
        handle = open(actual_path + '/' + new_dir + '/' + str(item), 'wb')

    print('\nDownload em andamento.')

    ftp.retrbinary('RETR ' + ftp.nlst()[0], handle.write)


elif info[pasta].split(' -')[0] == 'SIM':
    for i in ftp.nlst():
        print(str(ftp.nlst().index(i)) + ') ' + str(i))
    choice = int(input("\nDigite o número da pasta que deseja acessar: \n"))
    first_choice = str(ftp.nlst()[choice])
    ftp.cwd(folder + '/' + first_choice)

    for i in ftp.nlst():
        print(str(ftp.nlst().index(i)) + ') ' + str(i))
    second_choice = int(
        input("\nDigite o número da pasta que deseja acessar: \n"))

    new_dir = str(
        first_choice +
        '_' +
        ftp.nlst()[second_choice] +
        '_' +
        str(dir_create))
    if not os.path.exists(actual_path + '/' + str(new_dir)):
        os.mkdir(actual_path + '/' + str(new_dir))
    ftp.cwd(folder + '/' + first_choice + '/' + ftp.nlst()[second_choice])

    for item in ftp.nlst():
        handle = open(actual_path + '/' + new_dir + '/' + str(item), 'wb')

    print('\nDownload em andamento.')

    ftp.retrbinary('RETR ' + ftp.nlst()[0], handle.write)


elif info[pasta].split(' -')[0] == 'SINAN':
    ftp.cwd(folder + '/Dados')

    for i in ftp.nlst():
        print(str(ftp.nlst().index(i)) + ') ' + str(i))
    choice = int(input("\nDigite o número da pasta que deseja acessar: \n"))

    new_dir = 'DADOS ' + str(ftp.nlst()[choice]) + '_' + str(dir_create)
    if not os.path.exists(actual_path + '/' + str(new_dir)):
        os.mkdir(actual_path + '/' + str(new_dir))
    ftp.cwd(folder + '/Dados/' + ftp.nlst()[choice])

    for item in ftp.nlst():
        handle = open(actual_path + '/' + new_dir + '/' + str(item), 'wb')

    print('\nDownload em andamento.')
    ftp.retrbinary('RETR ' + ftp.nlst()[0], handle.write)

elif info[pasta].split(' -')[0] == 'SINASC':
    for i in ftp.nlst():
        print(str(ftp.nlst().index(i)) + ') ' + str(i))
    choice = int(input("\nDigite o número da pasta que deseja acessar: \n"))

    new_dir = str(ftp.nlst()[choice]) + '_' + str(dir_create)
    if not os.path.exists(actual_path + '/' + str(new_dir)):
        os.mkdir(actual_path + '/' + str(new_dir))

    if choice == 5:
        ftp.cwd(folder + '/' + ftp.nlst()[choice])

        for item in ftp.nlst():
            handle = open(actual_path + '/' + new_dir + '/' + str(item), 'wb')

        print('\nDownload em andamento.')

        ftp.retrbinary('RETR ' + ftp.nlst()[0], handle.write)

    else:
        try:
            first_choice = str(ftp.nlst()[choice]) + '/Dados'
            ftp.cwd(folder + '/' + first_choice)

            for i in ftp.nlst():
                print(str(ftp.nlst().index(i)) + ') ' + str(i))
            second_choice = int(
                input("\nDigite o número da pasta que deseja acessar: \n"))

            ftp.cwd(
                folder +
                '/' +
                first_choice +
                '/' +
                ftp.nlst()[second_choice])
        except BaseException:
            first_choice = str(ftp.nlst()[choice])
            ftp.cwd(folder + '/' + first_choice)

            for i in ftp.nlst():
                print(str(ftp.nlst().index(i)) + ') ' + str(i))
            second_choice = int(
                input("\nDigite o número da pasta que deseja acessar: \n"))

            ftp.cwd(
                folder +
                '/' +
                first_choice +
                '/' +
                ftp.nlst()[second_choice])

        for item in ftp.nlst():
            handle = open(actual_path + '/' + new_dir + '/' + str(item), 'wb')

        print('\nDownload em andamento.')

        ftp.retrbinary('RETR ' + ftp.nlst()[0], handle.write)

print('\nDownload concluído.')

print('\nAlgumas pastas podem estar vazias ou conter arquivos inúteis.')
