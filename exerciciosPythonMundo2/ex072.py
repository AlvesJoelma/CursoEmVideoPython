cont = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezeseis','dezesete','dezoito','dezenove','vinte')
while True:
    num = int(input('Digite um numero entre 0 e 20:'))
    if 0 < num > 20:
        print('Tente novamente.')
    else:
        print(f'Voce digitou o numero {cont[num]}')
        resp = ' '
        while resp not in 'SN':
            resp = str(input('Deseja continuar?')).strip().upper()[0]
        if resp == 'N':
            break

#Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.