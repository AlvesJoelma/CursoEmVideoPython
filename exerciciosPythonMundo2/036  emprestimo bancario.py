casa = float(input("Qual o valor da casa? R$ "))
salario = float(input("Qual seu salário? R$ "))
anos = int(input("Em quantos anos deseja parcelar?"))
minimo = salario*30/100
parcela = casa / (anos*12)
print("Para pagar a casa em ", anos, " anos a prestação será de ", parcela)
if parcela <= minimo:
    print("Seu empréstimo foi APROVADO")
else:
    print("Seu emprestimo foi NEGADO")