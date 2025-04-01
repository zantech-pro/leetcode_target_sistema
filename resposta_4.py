''''
4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado: 
• SP – R$67.836,43 
• RJ – R$36.678,66
• MG – R$29.229,88 
• ES – R$27.165,48 
• Outros – R$19.849,53
Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora. 
'''


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