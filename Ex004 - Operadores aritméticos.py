# Lista de operadores aritméticos e suas representações

# '+' representa adição
# '-' representa subtração
# '*' representa multiplicação
# '/' representa divisão
# '**' representa potência
# '//' representa divisão inteira
# '%' representa resto da divisão
# '==' representa 'igual a'
# '=' representa atribuição de valores

# ordem aritmética

# 1. ()
# 2. **
# 3. *, /, //, %
# 4. +, -

#exemplos

# 5 + 3 * 2 == 11
# (5 + 3) * 2 == 16
# 3 * 5 + 4 ** 2 == 31
# 3 * (5 + 4)** 2 == 243

n1: int = 2
n2: int = 4

s= n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

raiz = n1**(1/2)

print(' Soma: {}\n Produto: {}\n divisão: {}\n Diferença: {}\n Potência: {}\n'.format(s, m, d, di, e))