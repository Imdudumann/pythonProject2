n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
if n1 > n2:
    print('O primeiro número é o maior!')
elif n2 > n1:
    print('O segundo número é o maior!')
elif n1 == n2 or n2 == n1:
    print('Os dois valores são iguais!  ')