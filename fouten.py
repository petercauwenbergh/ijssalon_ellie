import math
def discriminant(a,b,c):
    uitkomst = []
    try:
        D1 = (-b + math.sqrt(b**2 - 4*a*c))/(2 * a)
        D2 = (-b - math.sqrt(b**2 - 4*a*c))/(2 * a)
        uitkomst.append(D1)
        uitkomst.append(D2)
    except:
        uitkomst="geen oplossing"
    return uitkomst

print ('Voor de formule ax^2 + bx + c, geef a, b en c:')
a = int(input('Wat is getal a? '))
b = int(input('Wat is getal b? '))
c = int(input('Wat is getal c? '))

oplossing=discriminant(a,b,c)

print (f'Met de waarden {a}, {b} en {c} berekenden we 3-de discriminant met als oplossingswaarden {discriminant(a,b,c)}.')