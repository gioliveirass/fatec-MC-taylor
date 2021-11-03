# ===================
# Funções
# ===================

# =========================================================================================================================================

# Verifica se X está entre 0 e 90
def verifica_X(x):
    while x<0 or x>90:
        x = int(input('O valor de X precisa estar entre 0 e 90. Por favor, insira novamente: '))
    return x

# =========================================================================================================================================

# Converte X para radianos (R)
def converte_para_radianos(x):
    r = x * 3.1415/180
    return r

# =========================================================================================================================================

# Aplica regra de arredomdamento
def arredonda(somatorio, x):
    str_somatorio = str(somatorio)
    if x == 0: # Normalmente imprime 1.0, então só acrescentei mais dois zeros pra ficar 1.000
        return str_somatorio + '00'
    elif x == 1: # Arredonda para 1.0, então só acrescentei mais dois zeros pra ficar 1.000
        return str(round(somatorio, 3)) + '00'
    else:
        quarta_casa_apos_virgula = int(str_somatorio[5:6]) # começa na 5 pq excluí as duas primeiras (x.)
        if quarta_casa_apos_virgula <= 6:
            # retorna até a terceira casa após a virgula
            return str_somatorio[0:5]
        elif quarta_casa_apos_virgula <= 8:
            # uso uma função do python que arredonda já para maior se a quarta casa for maior que 5
            # como aqui é maior que 6, vai arredondar pra cima
            return round(somatorio, 3)
        elif quarta_casa_apos_virgula == 9:
            # a função round do python oculta o último zero
            # por isso utilizo ela pra arredondar pra cima e acrescento o zero na mão caso a quarta casa seja 9
            return str(round(somatorio, 3)) + '0'

# =========================================================================================================================================

# ===================
# Programa principal
# ===================

# Recebe e verifica X
X_digitado = int(input('Insira um valor X entre 0 e 90: '))
x = verifica_X(X_digitado)

# Converte X para radianos (R)
r = converte_para_radianos(x)

# ====================
# Parte da recorrência
# ====================

# Sempre começa com n=1, pois se n=0 o somatório é 1. Então:
cima = -r**2 # sempre começa sendo elevada a 2*n = 2*1 = 2
baixo = 2 # (2*n)! = (2*1)! = 2! = 2
somatorio = 1 + cima/baixo # precisa desse 1 porque o somatório começa com n=0, e aí soma com o cima/baixo do n=1

for n in range(2, 6): # Começa no 2 pq já temos o valor de n=0 e n=1, vai até 5 (o range não pega o 6)
    cima = cima * (-r**2) # Ex.: -r**2 * (-r**2) = r**4 (n=2)
    baixo = baixo * (2*n-1) * (2*n) # Ex.: 2 * 3 * 4 (n=2)
    somatorio = somatorio + cima/baixo
    

somatorio_arredondado = arredonda(somatorio, x)
print(somatorio_arredondado)

# print('Sem arredondar: ' + str(somatorio))
