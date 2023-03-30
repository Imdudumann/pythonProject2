decide = int(input('Digite 1 para binario, 2 para octal e 3 para hexadecimal: '))
num = int(input('Digite o valor a ser convertido: '))
if decide == 1:
    print(format(num, 'b'))
elif decide == 2:
    print(format(num,'o'))
elif decide == 3:
    print(format(num,'x'))
