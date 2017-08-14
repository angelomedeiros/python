########################################
#              Exemplo I               #
########################################
a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))

if a > b :
    print("O primeiro número é maior!")
if b > a :
    print("O segundo número é maior")

print()

########################################
#              Exemplo II              #
########################################

idade = int(input("Digite a idade do seu carro: "))

if idade <= 3:
    print("Seu carro é novo!")
if idade > 3:
    print("Seu carro é velho!")

print()

########################################
#             Exemplo III              #
########################################

salário = float(input("Digite o salário para cálculo do imposto: "))
base = salário
imposto = 0

if base > 3000:
    imposto = imposto + ((base - 3000) * 0.35)
    base = 3000
if base > 1000:
    imposto = imposto + ((base - 1000) * 0.20)

print("Salário: R$%6.2f Imposto a pagar: R$%6.2f" % (salário,imposto))

########################################
#        Exemplo II > IV (else)        #
########################################

if idade <= 3:
    print("Seu carro é novo!")
else:
    print("Seu carro é velho!")
print()

########################################
#            Exemplo V (elif)          #
########################################

categoria = int(input("Digite a categoria do produto: "))

if categoria == 1:
    preço = 10
elif categoria == 2:
    preço = 18
elif categoria == 3:
    preço = 23
elif categoria == 4:
    preço = 26
elif categoria == 5:
    preço = 31
else:
    print("Categoria inválida, digite um valor entre 1 e 5!")
    preço = 0
print("O preço do produto é: R$%6.2f" %preço)
