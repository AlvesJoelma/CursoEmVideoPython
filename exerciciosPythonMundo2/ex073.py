clubes = ('Palmeiras','Atlético Mineiro','Fortaleza','Bragantino','Athletico - PR','Flamengo','Ceara SC','Atlético - GO','Bahia','Corinthians','Fluminense','Santos','Juventude','Internacional','Cuiaba','Sport Recife','São Paulo', 'America - MG','Grêmio','Chapecoense')
print( 'LISTA CLUBES BRASILEIRÃO:')
print(clubes)
print('='*25)
print('5 PRIMEIROS COLOCADOS:')
print(clubes[0:5])
print('=' * 25)
print('4 ULTIMOS COLOCADOS:')
print(clubes[-4:])
print('='*25)
print('ORDEM ALFABÉTICA:')
print(sorted(clubes))
print('='*25)
print('COLOCAÇÃO CHAPECOENSE:')
print(f'{clubes.index("Chapecoense")+1}° posição')
print('='*25)

#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
# Depois mostre: a) Os 5 primeiros times. b) Os últimos 4 colocados. c) Times em ordem alfabética. d) Em que posição está o time da Chapecoense.