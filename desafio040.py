n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segundo nota: '))
media = (n1+n2)/2
print('Sua média foi {}'.format(media))
if media <= 5.0:
    print('REPROVADO')
elif media >= 5.0 and media <= 6.9:
    print('RECUPERAÇÃO')
elif media >= 7.0:
    print('APROVADO')
