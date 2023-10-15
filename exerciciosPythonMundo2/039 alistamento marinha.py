from datetime import date
atual = date.today().year
nas = int(input("Ano de nascimento"))
idade = date.today().year - nas
print("Você tem ", idade, " anos")
if idade < 18:
    falta = 18 - idade
    ano = atual + falta
    print("Você ainda não precisa se alistar. Deve fazer isso em ", falta, " anos.", ano)
elif idade == 18:
    print("Voce deve se alistar imediatamente")
elif idade >= 18:
    passou = idade - 18
    ano = atual - passou
    print("Você já tem idade para se alistar e deveria ter feito isso ha ", passou ," anos.", ano)