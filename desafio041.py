import datetime

data = datetime.date.today()
ano = data.strftime('%Y')
anoNascimento = int(input('Digite em que ano você nasceu: '))
newYear = int(ano)
idade = newYear - anoNascimento
print('Você tem {} anos.'.format(idade))
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif  idade <= 19:
    print('JUNIOR')
elif idade == 20:
    print('SÊNIOR')
elif idade > 20:
    print('MASTER')
