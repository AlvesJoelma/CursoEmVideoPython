alunos = []
geral = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2 ) / 2
    alunos.append([nome, [nota1, nota2], media])

    resp = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if resp in 'N':
        break
print('*'*25)
print(f'{"N°":<4}{" NOME":<10}{"  MÉDIA":>8}')
print('-'*25)
for i, a in enumerate(alunos):
    print(f'{i:<4} {a[0]:<10} {a[2]:>8.1f}')
print('-'*25)
while True:
    opçao = int(input('Mostrar notas de qual aluno? 999 interompe '))
    if opçao == 999:
        print('Finalizando.')
        break
    if opçao <= len(alunos)-1:
        print(f'Notas de {alunos[opçao][0]} são {alunos[opçao][1]}.')
