import math

ângulo = float(input('Coloque o ângulo do objeto: '))
seno = math.sin(math.radians(ângulo))
print('O ângulo de {} tem o seno de {:.2f}'.format(ângulo,seno))
tangente = math.tan(math.radians(ângulo))
print('O ângulo de {} tem o tangente de {:.2f}'.format(ângulo,tangente))
coseno = math.cos(math.radians(ângulo))
print('O ângulo de {} tem o coseno de {:.2f}'.format(ângulo,coseno))