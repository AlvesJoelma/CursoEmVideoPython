nome= input("Seu nome: ").strip()
dividido= nome.split()
junto = "".join(dividido)
print(nome.upper())
print(nome.lower())
print(len(junto)) #qtas letras sem espaço
print(len(nome) - nome.count(' ')) #qtas letras sem espaço
print(nome.find(' ')) #qtas letras primeiro nome