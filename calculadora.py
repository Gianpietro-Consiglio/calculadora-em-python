import time
history = []

while True:
    menu = ('Adição', 'Subtração', 'Divisão', 'Multiplicação', 'Histórico')
    soma = 0
    lista = []
    print('*' * 30)
    for x in menu:
        soma += 1
        print(f'[{soma}] {x}')
    print('*' * 30)    
    print('')    
    resposta = int(input('Escolha sua opção: '))
    print('')
    if resposta == 1:
        z = int(input('Quntos números você quer somar? '))
        c = 0
        while c < z:
            c += 1
            num = int(input(f'Escolha um número[{c}]: '))
            lista.append(num)
        print('') 
        print('-' * 25)
        print(f'Resultado da soma = {sum(lista)}')
        history.append(sum(lista))
        print('-' * 25)
        again = str(input('Voltar ao menu? ').lower())
        if again == "sim":
            print('Ok, retornando...')
            time.sleep(2)
            print('')           
        else:
            print('Finalizando...')
            time.sleep(2)
            print('')
            break    

    elif resposta == 2:
        num = int(input('Selecione um número: '))
        num2 = int(input('Selecione mais um número: '))
        print('')
        print('-' * 25)
        print(f'Resultado da subtração = {num - num2}')
        history.append(num - num2)
        print('-' * 25)
        print('')
        again = str(input('Voltar ao menu? ').lower())
        if again == "sim":
            print('Ok, retornando...')
            time.sleep(2)
            print('')           
        else:
            print('Finalizando...')
            time.sleep(2)
            print('')
            break  

    elif resposta == 3:
        num = int(input('Selecione um número: '))
        num2 = int(input('Selecione mais um número: ')) 
        print('')
        print('-' * 25)
        print(f'Resultado da divisão = {num / num2}')
        history.append(num / num2)
        print('-' * 25)
        print('')
        again = str(input('Voltar ao menu? ').lower())
        if again == "sim":
            print('Ok, retornando...')
            time.sleep(2)
            print('')           
        else:
            print('Finalizando...')
            time.sleep(2)
            print('')
            break  


    elif resposta == 4:
        num = int(input('Selecione um número: '))
        num2 = int(input('Selecione mais um número: ')) 
        print('')
        print('-' * 25)
        print(f'Resultado da multiplicação = {num * num2}')
        history.append(num * num2)
        print('-' * 25)
        print('')
        again = str(input('Voltar ao menu? ').lower())
        if again == "sim":
            print('Ok, retornando...')
            time.sleep(2)
            print('')           
        else:
            print('Finalizando...')
            time.sleep(2)
            print('')
            break  
    elif resposta == 5:
        print(f'Seu histório de resultados de contas = {history}')
        print('')  
        again = str(input('Voltar ao menu? ').lower())
        if again == "sim":
            print('Ok, retornando...')
            time.sleep(2)
            print('')           
        else:
            print('Finalizando...')
            time.sleep(2)
            print('')
            break  

    else:
        print('Não foi possível concluir sua solicitação!')
        print('')
        again = str(input('Voltar ao menu? ').lower())
        if again == "sim":
            print('Ok, retornando...')
            time.sleep(2)
            print('')           
        else:
            print('Finalizando...')
            time.sleep(2)
            print('')
            break  
        break                
