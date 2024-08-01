nombre = input('Indica tu nombre: ')
ventas = input('Cuánto has vendido este mes en dólares? ')
ventas = float(ventas)
comision = (round(ventas*0.13, 2))

print(f"La comision de {nombre} para este mes corresponde a {comision} dólares")