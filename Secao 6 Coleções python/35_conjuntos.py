"""Programação em Python
1. Crie um programa que lê 6 valores inteiros, armazene em uma lista e em seguida mostre na tela os valores
lidos.
"""
""" 
numeros = []

for i in range(1,7):
    inf_num = int(input(f'Informe o {i}º número para inserir na lista: '))
    numeros.append(inf_num)
print(numeros)

2. Faça um programa que possua uma lista denominada A que armazene 6 números inteiros. O programa
deve executar os seguintes passos:
a) Atribua os seguintes valores a essa lista: 1, 0, 5, -2, -5, 7.
b) Armazene em uma variável inteira a soma entre os valores das posições A[0], A[1] e A[5] da lista e mostre
na tela esta soma.
c) Modifique a lista na posição 5, atribuindo a esta posição o valor 100.
d) Mostre na tela cada valor da lista A, um em cada linha.
"""
a = [1, 0, 5, -2, -5, 7]

#for i in range(1,7):
#    lis_num = int(input(f'Informe o {i}º número para inserir na lista: '))
#    a.append(lis_num)
#print(a)
print(a)
print(a[0],a[1],a[5])
soma = a[0] + a[1] + a[5]
print(soma)

a.pop(5)
print(a)

a.insert(5,100)
for numero in a:
    print(numero)


"""
3. Faça um programa que leia 10 valores, armazene-os em uma lista e apresente quantos valores pares ele
possui.
"""

lista: list[int] = []

contador_pares: int = 0

while len(lista) < 10:
    valor: int = int(input(f'Informe o valor {len(list) + 1}/10: '))
    lista.append(valor)

    if valor % 2 == 0:
        contador_pares = contador_pares + 1

if contador_pares > 0:
    print(f'A lista {lista} possui {contador_pares} pares.')
else:
    print(f'A lista {lista} não possui valores pares')
