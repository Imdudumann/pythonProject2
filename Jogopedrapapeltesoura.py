import random


print('-='*15)
print('   JOGO PEDRA PAPEL TESOURA')
print('-='*15)
lista = ['pedra','papel','tesoura']
randomizador = random.randint(0,2)
escolha = lista[randomizador]
print('''Escolha um número para iniciar o jogo
[1] para pedra
[2] para papel
[3] para tesoura''')
myChoice = int(input('Digite sua opção: '))
if myChoice == 1 and escolha == 'pedra':
    print('Você escolheu {} e o computador escolheu {}, EMPATE!'.format('pedra',escolha))
elif myChoice == 1 and escolha == 'papel':
    print('Você escolheu {} e o computador escolheu {}, VOCÊ PERDEU!'.format('pedra',escolha))
elif myChoice == 1 and escolha == 'tesoura':
    print('Você escolheu {} e o computador escolheu {}, VOCÊ GANHOU!'.format('pedra',escolha))
elif myChoice == 2 and escolha == 'pedra':
    print('Você escolheu papel e o computador escolheu {}, VOCÊ GANHOU!'.format(escolha))
elif myChoice == 2 and escolha == 'papel':
    print('Você escolheu papel e o computador escolheu {}, EMPATE!'.format(escolha))
elif myChoice == 2 and escolha == 'tesoura':
    print('Você escolheu papel e o computador escolheu {}, VOCÊ PERDEU!'.format(escolha))
elif myChoice == 3 and escolha == 'pedra':
    print('Você escolheu tesoura e o computador escolheu {}, VOCÊ PERDEU!'.format(escolha))
elif myChoice == 3 and escolha == 'papel':
    print('Você escolheu tesoura e o computador escolheu {}, VOCÊ GANHOU!'.format(escolha))
elif myChoice == 3 and escolha == 'tesoura':
    print('Você escolheu tesoura e o computador escolheu {}, EMPATE!'.format(escolha))