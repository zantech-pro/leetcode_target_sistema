''''
5) Escreva um programa que inverta os caracteres de um string.
IMPORTANTE: a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código; b) Evite usar funções prontas, como, por exemplo, reverse;
'''


string = input("Digite um palavra >>> ")
string_nova = []
for letra in range(len(string), 0, -1):
    string_nova.append(string[letra-1])

print(f'Veja ela de forma invertida: "{''.join(string_nova)}"')