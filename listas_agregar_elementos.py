lista_inicial = []

longitud_lista = len(lista_inicial)
print(f'Longitud de la variable lista_inicial es {longitud_lista}')

elemento_entero = 9
elemento_cadena = 'Hola mundo!'
elemento_double = 3.14
elemento_extra = 'Extra extra'

lista_inicial.append(elemento_entero)
lista_inicial.append(elemento_cadena)
lista_inicial.append(elemento_double)
lista_inicial.append(elemento_extra)

longitud_lista = len(lista_inicial)
print(f'Longitud de la variable lista_inicial es {longitud_lista}')
print(lista_inicial)

for elmt in lista_inicial:
    mensaje = f'{elmt} es de tipo {type(elmt)}'
    print(mensaje)

lista_inicial.pop()
lista_inicial.pop()
longitud_lista = len(lista_inicial)
print(f'Longitud de la variable lista_inicial es {longitud_lista}')
print(lista_inicial)