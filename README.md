# leetcode_target_sistema
Respostas do Desafio postado na Gupy pela Targer Sistemas, usei python para elebaoração das repostas


1) Observe o trecho de código abaixo: int INDICE = 13, SOMA = 0, K = 0;
Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
Imprimir(SOMA);
Ao final do processamento, qual será o valor da variável SOMA?
**Esta no arquivo resposta_1.py**
```python
k = 0
soma = 0
indice = 13
while k < 13:
    k+=1
    soma+=1
print(soma)
```

3) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;
```python
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
```

3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;
```python
import json

menor_valor = 0
maior_valor = 0
num_dias_faturamento_superior_media_mensal = 0

dados_json = ''
with open('dados.json', 'r', encoding='utf-8') as file:
    dados_json = json.loads(file.read())

aux_dia = 0
valor = 0

menor_valor = 0
aux_dia_menor_fat = 0

count = 0
contador_media = 0
aux_media_soma = 0

for item in dados_json:
    if float(item['valor']) > valor:
        aux_dia = item['dia']
        valor = float(item['valor'])
    
    if float(item['valor']) <= menor_valor:
        if float(item['valor']) == 0 and count == 0:
            aux_dia_menor_fat = item['dia']
            menor_valor = float(item['valor'])
            count = 1

    if float(item['valor']) > 0:
        aux_media_soma += float(item['valor'])
        contador_media+=1


print(f'O dia {aux_dia_menor_fat}, possui o menor valor de faturamento {menor_valor}')
print(f'O dia {aux_dia}, possui o maior valor de faturamento {valor}')

media_faturamento = aux_media_soma / contador_media
lista_dias_acima_media = []
for item in dados_json:
    if float(item['valor']) > media_faturamento:
        lista_dias_acima_media.append((item['dia'], item['valor']))

for item in lista_dias_acima_media:
    print(f'O dia {item[0]}, faturou {item[1]} ficando acima da media do mês que deve media de {media_faturamento}')
```
4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
• SP – R$67.836,43
• RJ – R$36.678,66
• MG – R$29.229,88
• ES – R$27.165,48
• Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.  

```
valor_por_estados = list({'SP': 67836.43,
                 'RJ': 36678.66,
                 'MG': 29229.88,
                 'ES':  27165.48,
                 'Outros':  19849.53
                })

valor_por_estados_preco = {'SP': 67836.43,
                 'RJ': 36678.66,
                 'MG': 29229.88,
                 'ES':  27165.48,
                 'Outros':  19849.53
                }

valor_mensal_total = 0

for item in [valor_por_estados_preco]:
    for chave in valor_por_estados:
        valor_mensal_total += item[chave]

for item in [valor_por_estados_preco]:
    for chave in valor_por_estados:
        if 'Outros' in valor_por_estados:
            porcetagem = (item[chave] / valor_mensal_total)*100
            print(f'O estado {chave} representa {round(porcetagem, 2)}% do faturanto total.')
        else:
            porcetagem = (item[chave] / valor_mensal_total)*100
            print(f'O estado {chave} representa {round(porcetagem, 2)}% do faturanto total.')

print('Valor total faturado no mês: ',valor_mensal_total)
```

5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;

```python
string = input("Digite um palavra >>> ")
string_nova = []
for letra in range(len(string), 0, -1):
    string_nova.append(string[letra-1])

print(f'Veja ela de forma invertida: "{''.join(string_nova)}"')
```
