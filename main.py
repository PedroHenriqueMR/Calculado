from Calculadora import calculadora_numerica
#Importa a função calculadora_numerica de outro arquivo

print('Olá!')
print('Vamos realizar cálculos matemáticos.')

while True:
#Abre o laço principal do programa. Ele repete tudo o que está dentro dele (menu, leitura dos números e cálculo) até que sejá digitado o numero 5.

    print('Escolha uma das opções abaixo ')
    print('Digite 1 para Multiplicação')
    print('Digite 2 para Divisão')
    print('Digite 3 para Adição')
    print('Digite 4 para Subtração')
    print('Digite 5 para Sair')
    #Menu

    while True:
    #Abre um segundo laço, usado só para validar a opção do menu. Ele repete até o usuário digitar algo válido.

        digito = input('Digite uma das opções acima: ')
        #Lê o que o usuário digitou.


        try:
            digito = int(digito)
        except ValueError:
            print('Valor inválido. Por favor, digite novamente.')
            continue
        #Tenta converter o texto para número inteiro.
        #Se der certo, segue em frente.
        #Se o usuário digitou algo como abc ou 2.5, o Python gera um ValueError.
        #O except captura o erro, mostra a mensagem e o continue volta ao início do laço para pedir de novo.


        if digito in (1, 2, 3, 4, 5):
            break
        print('Opção inexistente, escolha de 1 a 5')
        #Verifica se o número está entre as opções do menu.
        #Se estiver, o break encerra esse laço de validação.
        #Se não estiver (por exemplo, 9), mostra a mensagem de opção inexistente e o laço repete.


    if digito == 5:
        break
    #Já fora do laço de validação: se o usuário escolheu 5 (Sair), o break encerra o laço principal e o programa termina.


    while True:
        numero1 = input('Digite o primeiro valor a ser calculado: ')
        try:
            numero1 = int(numero1)
            break
        except ValueError:
            print('Valor inválido. Por favor, digite novamente.')
    # Outro laço de validação, agora para o primeiro número.
    #Lê o texto, tenta converter para int e, se conseguir, o break sai do laço. Se falhar, 
    #mostra o erro e pergunta de novo(sem precisar de continue, pois o laço já volta ao início sozinho).


    while True:
        numero2 = input('Digite o segundo valor a ser calculado: ')
        try:
            numero2 = int(numero2)
            break
        except ValueError:
            print('Valor inválido. Por favor, digite novamente.')
    #Idêntico ao anterior, mas para o segundo número.


    resultado = calculadora_numerica(digito, numero1, numero2)
    print(f'Calculo: {resultado}')
    #Chama a função importada, passando a operação escolhida e os dois números. O valor retornado é guardado em resultado.
