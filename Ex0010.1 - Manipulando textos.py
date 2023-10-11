nome: str = 'Vagner Carlesso da Silva'

maiuscula: str
minuscula: str
contador: int = 0
s_espaco: str = 'null'
total: str
p1_nome: str

print(nome)
print(nome.lower())
print(nome.upper())
total = nome.split()

print('\nPrimeiro nome: {}\nTotal de caracteres: {}'.format(total[0],len(total[0])))

s_espaco=total[0]
s_espaco=s_espaco+total[1]
s_espaco=s_espaco+total[2]
s_espaco=s_espaco+total[3]

print('\nO nome "{}" tem um total de:\n{} caracteres no total.\n{} Caracteres de texto.'
      '\n{} Espaços entre frases.'.format(nome, len(nome), len(s_espaco), nome.count(' ')))

#----------------------------------------------------------------------------------------------------
numero: str
condicao: bool = False
texto: str


numero=(input('Digite um número de 0 a 9999\n'))


print(numero.split())
