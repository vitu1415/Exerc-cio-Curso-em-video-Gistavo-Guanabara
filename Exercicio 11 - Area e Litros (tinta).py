largura = float(input('Qual é a largura: '))
altura = float(input('Qual é a altura: '))
area = largura * altura
tinta = area / 2

print('A parede do tem dimesão de {} X {} e sua area é de {} m².'.format(largura, altura,area))
print('Para printar essa parede vai precisar de {} L de tinta.'.format(tinta))