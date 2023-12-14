'''
{
    'user': {
        'email': 'g@mail.co',
        'created_at: '13-12-23',
        'city': 'Puerto Escondido',
        'coordinates': {
            'lat': 19.234324.
            'lon': -98.123123
        },
        'tags': [
            'python',
            'jupyter',
            'bedu'
        ]
    }
}
'''


diccionario_inicial = {}
print(type(diccionario_inicial))

diccionario_inicial['nombre'] = 'Galileo'
diccionario_inicial['apellidos'] = 'Guzman Ibanez'
diccionario_inicial['edad'] = 34
diccionario_inicial['peso'] = 80.5
diccionario_inicial['calificaciones'] = [9, 7, 8 , 5, 6]
diccionario_inicial['peso'] = 9
diccionario_inicial['coordinates'] = {
    'lat': 19.234324,
    'lon': -98.123123
}

print(diccionario_inicial)

nombre = diccionario_inicial['nombre']
for letra in nombre:
    print(letra)

edad = diccionario_inicial['edad']
print(edad)

print('-------------------')
peso = diccionario_inicial.get('peso', 100.0)
print(peso)
print(type(peso))

print('-------------------')
calificaciones = diccionario_inicial.get('calificaciones', [])
print(calificaciones)
for c in calificaciones:
    print(c)

print('------------------')
coordenadas = diccionario_inicial.get('coordinates')
print(coordenadas)
print(coordenadas['lat'])
print(coordenadas.get('lon'))

