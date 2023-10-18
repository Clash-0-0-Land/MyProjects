
sair=False
while True:


    usuario = input('\033[35mVocê:\033[m ').strip()

    arq_us = open('dados_usuario.txt', 'r')
    a_us = arq_us.read()
    dados_usu = a_us.split('\n')
    arq_us.close()

    arq_m = open('dados_machine.txt', 'r')
    a_machin = arq_m.read()
    machine_dados = a_machin.split('\n')
    arq_m.close()

    for q in range(len(dados_usu)):

        if usuario.lower() == dados_usu[q].lower() and len(dados_usu) == len(machine_dados):
            print(f'\033[32mCharbot: {machine_dados[q]}\033[m')
            if usuario == 'Tchau':
                sair=True
            break

        elif q == len(dados_usu)-1:


            print('='*70)
            dados_mac = input('\033[32mEsta pergunta não possui uma resposta associada.\nDifite a seguir o que você quer que a máquina responda:\033[m\n')
            a_mac = open('dados_machine.txt', 'a')
            a_mac.write(dados_mac+'\n')
            a_mac.close()

            print('\033[34mDados amarzenados com sucesso!\033[m')
            print('='*70)

            a_u = open('dados_usuario.txt', 'a')
            a_u.write(usuario+'\n')
            a_u.close()


    if sair==True:
        break




