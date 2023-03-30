r1 = float(input('Digite o primeiro segmento de reta: '))
r2 = float(input('Digite o segundo segmento de reta: '))
r3 = float(input('Digite o terceiro segmento de reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('É um triângulo!',end=' ')
    if r1 == r2 == r3:
        print('É um triângulo equilatero!')
    elif r1 != r2 != r3 != r1:
        print('É um triângulo escaleno!')
    else:
        print('É um triangulo isoceles!')