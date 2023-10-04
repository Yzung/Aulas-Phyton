valor: int
ant: int
suss: int

print('Digite um valor')
valor=int(input())

ant= valor-1
suss= valor+1

print('Antecessor: {}\n Sucessor: {}\n'.format(ant, suss))