# Métodos para validação dos tipos de dados existentes no código

valor = input('Digite algo: ')
print('O tipo do arquivo é: ', type(valor))
print('Só tem espaços no campo?: ', valor.isspace())
print('Esta em maiusculas?: ', valor.isupper())
print('Está em minusculas?: ', valor.islower())
print('Está capitalizada?: ', valor.istitle())

#Na dúvida digitar variável.is e então verificar o método desejado