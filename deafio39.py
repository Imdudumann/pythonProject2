import datetime

data = datetime.date.today()
ano = data.strftime('%Y')
novoAno = int(ano)
anoNascimento = int(input('Digite o ano em que você nasceu: '))
idade = novoAno - anoNascimento
print('Você tem {} anos!'.format(idade))
if idade > 18:
    print('Já passou da hora de se alistar, você está atrasado em {} anos!'.format(idade-18))
elif idade <18:
    print('Ainda faltam {} anos para você se alistar'.format(18-idade))
elif idade == 18:
    print('Vá na junta militar o mais rapido possivel para não perder o prazo e pagar multa!')

