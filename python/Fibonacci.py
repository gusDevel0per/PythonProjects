num = int(input("Entre com o numero: "))

aux=num
soma=0

while aux>=0:
    soma = soma + 1 +(aux-1)*2
    aux-=1

print(f"O quadrado de {num} é {soma}.")

        
