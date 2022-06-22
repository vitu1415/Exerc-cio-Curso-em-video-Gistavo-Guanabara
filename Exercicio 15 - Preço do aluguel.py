dias =  int(input('Quantos dias usou o carro: '))
km = float(input('Qunato km foi rodados: '))

val_dias = dias * 60
val_km = km * 0.15
val_total = val_dias + val_km
print('o total a pagar é de R${:.2f}'.format(val_total))