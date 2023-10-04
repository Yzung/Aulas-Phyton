carteira: float
conv: float = 5.15
dolar: float
carteira = int(input())

dolar=carteira/conv

print('Eu tenho um total de R${}, e poderia comprar ${:.2f}! '.format(carteira, dolar))

