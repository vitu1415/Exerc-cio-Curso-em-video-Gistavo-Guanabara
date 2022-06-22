from multiprocessing.spawn import import_main_path


import math

oposto = float(input('Comprimento do cateto oposto: '))
adjacente = float(input('comprimento do cateto adjacente: '))

hipotenusa = (oposto ** 2) + (adjacente ** 2)
hipotenusa = math.sqrt(hipotenusa)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))