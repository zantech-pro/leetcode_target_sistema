''''
    2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 
    e o próximo valor sempre será a soma dos 2 valores anteriores 
    (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde,
      informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;
'''
try:
    num = int(input('Informe um numero e descubra se ele é da sequencia de Fibinancci >>>'))

    a = 0
    b = 1
    lista_fibo = []
    lista_fibo.append(a)
    lista_fibo.append(b)


    while True:
        lista_fibo.append(lista_fibo[-2] + lista_fibo[-1])

        if num < lista_fibo[-1]:
            break
    print('Esta é a sequencia de Fibonacci', lista_fibo)
    if num in lista_fibo:
        print(f'O numero {num} informado pertence a sequencia de fibonacci...')
    else:
        print(f'O numero {num} informado ***NÃO*** pertence a sequencia de fibonacci...')
except ValueError as error:
    print(f'Entranda invalida, carregue o programa novamente')



