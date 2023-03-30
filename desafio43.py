peso = float(input('Digite quantos kilos você tem: '))
altura = float(input('Digite a sua altura: '))
alt = altura**2
imc = peso/(alt)
print('Seu IMC é {:.1f}'.format(imc))
if imc <= 18.5:
    print('Você está abaixo do peso!')
elif imc >= 18.5 and imc <= 25.0:
    print('Você está no seu peso ideal!')
elif imc >25.0 and imc <=30:
    print('Você está com sobrepeso!')
elif imc >= 30 and imc <=40:
    print('Você está com obesidade!')
elif imc > 40:
    print('Você está com obesidade morbida!')