#Tipos primitivos de dados

n1: int
n2: float
n3: bool
n4: str

soma: int

print('Digite outro número')
n1= int(input())

soma = n1 + n1

print('A soma entre {} e {} é : {}'.format(n1, n1, soma))

print('O tipo primitivo do valor é: ', type(soma))