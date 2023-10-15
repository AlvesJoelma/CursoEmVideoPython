vel= int(input("Qual a velocidade do carro? "))
multa = (vel - 80)*7
if vel > 80:
    print("Voce ultrapassou o limite de velocidade permitido.\nO valor da multa é R$ ", multa)
else:
    print("Você esta na velocidade permitida. Boa viagem !!!")