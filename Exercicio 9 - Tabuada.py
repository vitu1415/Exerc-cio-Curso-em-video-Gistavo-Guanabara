num = int(input('digite um número para ver a tabuada: '))
print('-'*30)
num_mutiplicado = 0
for x in range(1,11):
    num_mutiplicado = num * x
    print('{} X {} = {}'.format(num,x,num_mutiplicado))
print('-'*30)