media = 0
soma = 0
numero_par = 0
numero_total = 0
numero=1

print("digite 0 para parar o programa")

while numero != 0:
    numero = float(input("Digite o número: "))

    numero_total += 1

    if numero%2 == 0:
        soma += numero
        numero_par += 1

media = (soma / (numero_par-1)) #+ 1

print("soma: {}".format(soma))
print("numero total: {}".format(numero_total-1))
print("numero par: {}".format(numero_par-1))
print("media: {}".format(media))
