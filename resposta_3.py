''''
3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;
'''
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







