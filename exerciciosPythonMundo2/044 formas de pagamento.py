valor = float(input("Valor do produto: R$ "))
print('''FORMA DE PAGAMENTO
[1] A vista
[2] A vista no cartão
[3] Até 2x no cartão
[4] Em 3x ou mais no cartão''')
opçao = int(input("Como deseja pagar? "))
if opçao == 1:
    novo = valor - (valor*10/100)
elif opçao == 2:
    novo = valor - (valor*5/100)
elif opçao == 3:
    novo = valor
elif opçao == 4:
    novo = valor + (valor * 20 / 100)
print("Você escolheu a opção ", opçao, " e vai pagar R$ ", novo)