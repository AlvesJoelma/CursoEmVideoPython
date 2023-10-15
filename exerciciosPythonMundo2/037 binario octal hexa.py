n = int(input("Digite um numero"))
print('''==*= OPÇÃO =*==
[1] Binário
[2] Octal
[3] Hexadecimal''')
escolha = int(input("Para que base deseja converter?"))
if escolha == 1:
    print(bin(n)[2:])
elif escolha == 2:
    print(oct(n)[2:])
elif escolha == 3:
    print(hex(n)[2:])
else:
    print("Opção inválida")