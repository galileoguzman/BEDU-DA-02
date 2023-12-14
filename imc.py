print('Indice de Masa Corporal (IMC)')

masa = input('¿Cual es tu peso en Kilogramos?')
estatura = input('¿Cual es tu estatura en metros?')

masa = float(masa)
estatura = float(estatura)

imc = masa / (estatura * estatura)
print(f'Tu IMC es de {imc:.2f}')

# imc < 18.5 bajo de peso
# img < 25 Peso normal
# imc < 30 Sobre peso
# imc > Obesidad

if imc < 18.5:
    print('Bajo de peso')
elif imc < 25:
    print('Peso normal')
elif imc < 30:
    print('Sobre peso')
else:
    print('Obesidad')
