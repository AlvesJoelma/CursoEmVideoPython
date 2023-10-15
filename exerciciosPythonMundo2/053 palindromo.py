frase = str(input("Digite uma frase").upper()).strip()
palavras= frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso = inverso + junto[letra]
print("O inverso de ", junto, " é ", inverso)
if inverso==junto:
    print("Temos um palindromo")
else:
    print("Não temos um palindromo")
