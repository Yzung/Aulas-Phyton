valor=int(input('Digite um número: \n'))

contador: int = 0
prod: int = 0

while contador <= 9:
    contador=contador+1
    prod=contador*valor
    print('| {:2}  X  {:2} = {:2} |'.format(valor, contador, prod))