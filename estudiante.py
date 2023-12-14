lista_estudiantes = [
    {
        'nombre': 'Antonio',
        'calificaciones': [7.8, 9.8, 9.0, 10, 9.2]
    },
    {
        'nombre': 'Mariana',
        'calificaciones': [7.8, 9.8, 4.0, 10, 9.2]
    },
    {
        'nombre': 'Gerardo',
        'calificaciones': [7.2, 9.8, 9.0, 10, 9.2]
    },
    {
        'nombre': 'David',
        'calificaciones': [7.8, 9.8, 6.0, 10, 9.2]
    },
    {
        'nombre': 'Daniel',
        'calificaciones': [7.8, 9.8, 9.0, 5, 9.2]
    },
    {
        'nombre': 'Henrry',
        'calificaciones': [7.8, 9.8, 9.0, 2, 9.2]
    },
    {
        'nombre': 'Alejandro',
        'calificaciones': [7.8, 9.8, 9.0, 10, 9.2]
    },
    {
        'nombre': 'Jose Carlo',
        'calificaciones': [7.8, 8, 9.0, 10, 9.2]
    },
    {
        'nombre': 'Daniel',
        'calificaciones': [7, 8, 9.0, 10, 9.2]
    }
]

def promedio_estudiante(estudiante):
    calificaciones = estudiante.get('calificaciones')
    suma = 0
    for c in calificaciones:
        suma = suma + c
    promedio = suma / len(calificaciones)
    nombre = estudiante.get('nombre')
    return f'{nombre} tiene de promedio {promedio:.2f}'

for e in lista_estudiantes:
    print(promedio_estudiante(e))