print('{:=^40}'.format(' LOJAS MANN '))

print('-='*20)
print('         SIMULADOR DE DESCONTOS')
print('-='*20)
valor_produto = float(input('Digite o valor do produto: '))
opcao_pagamento = int(input('''Digite a forma de pagamento:
[1] Dinheiro ou Cheque
[2] Á vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
'''))
if opcao_pagamento == 1:
    print('O seu produto custa {} e você vai receber 10% de desconto! Seu produto vai sair por {}'.format(valor_produto,valor_produto-(valor_produto*10)/100))
elif opcao_pagamento == 2:
    print('O seu produto custa {} e você vai receber 5% de desconto! Seu produto vai sair por {}'.format(valor_produto,valor_produto-(valor_produto*5/100)))
elif opcao_pagamento == 3:
    print('Seu produto vai sair pelo preço normal de {}R$'.format(valor_produto))
elif opcao_pagamento == 4:
    print('Seu produto não vai ter desconto nessa modalidade de pagamento!',end=' ')
    print('Você vai pagar 20% de juros, seu produto vai custar {}'.format(valor_produto+(valor_produto*20/100)))
else:
    print('OPÇÃO INVALIDA DE PAGAMENTO!')
