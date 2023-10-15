primeiro = int(input("Primeiro termo"))
razão = int(input("Digite a razão"))
décimo = primeiro + (10-1) * razão
for c in range(primeiro,décimo + razão,razão):
    print(c)
print("ACABOU")