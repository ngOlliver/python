vel = float(input('Qual a velocidade do carro? '))
if vel > 80:
    multa = (vel - 80) * 7
    print('Você recebeu uma multa de R${:.2f}'.format(multa))
else:
    print('Você não foi multado.')
