#jeito mais longo
nome = str(input('Qual é seu nome completo? ')).strip()
nome = nome.lower()
nome = nome.count('silva')

if nome >= 1:
    print('Seu nome Tem Silva? True')
else:
    print('Seu nome Tem Silva? False')
#jeito mais rapido
nome = str(input('Qual é seu nome completo? ')).strip()
print('Seu nome tem Silva? {}'.format('Silva' in nome.lower()))