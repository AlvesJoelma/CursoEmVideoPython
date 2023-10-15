peso = float(input("Peso: "))
altura = float(input("Altura: "))
imc = peso / (altura**2)
if imc < 18.5:
    print("ABAIXO DO PESO")
elif 18.5 <= imc < 25:
    print("PESO IDEAL")
elif imc >= 25 and imc < 30:
    print("SOBREPESO")
elif imc >= 30 and imc < 40:
    print("OBESIDADE")
elif imc >40:
    print("OBESIDADE MORBIDA")