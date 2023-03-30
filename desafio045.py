import random


print('-='*15)
print('   JOGO PEDRA PAPEL TESOURA')
print('-='*15)

choices = ['Pedra','Papel','Tesoura']
choicePc = random.randint(choices)
print('''Escolha umas das opções abaixo:
[1] Pedra
[2] Papel
[3] Tesoura''')
myChoice = str(input('Qual é sua escolha? '))
if myChoice == '1' and choicePc == choices[0]:
    print('empate')
elif myChoice == '1' and choicePc == choices[1]:
    print('Você perdeu!')
elif myChoice == '1' and choicePc == choices[2]:
    print('Você ganhou!')
#print(choices[0],choices[1],choices[2])

