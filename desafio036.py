print('-='*20)
print('SIMULADOR DE COMPRA DE IMÓVEL')
print('-='*20)
casa = float(input('Digite o valor do imóvel: R$'))
salario = float(input('Digite quanto você ganha mensalmente: R$'))
anos = int(input('Em quantos anos você pretende pagar esse imóvel? '))
prestação = casa /(anos*12)
parcelaMinima = salario *30/100
print('A parcela do imovel custa {:.2f}'.format(prestação),end=' ')
print('30% do seu salário é {}'.format(parcelaMinima))
if prestação <= parcelaMinima:
    print('EMPRÉSTIMO APROVADO!')
else:
    print('EMPRÉSTIMO NEGADO!')