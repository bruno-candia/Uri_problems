A, B, C = map(float, input().split())
list = [A, B, C]
list.sort()

if (list[0] + list[1]) > list[2]:
    if (list[2]**2 == (list[1]**2 + list[0]**2)):
        print('TRIANGULO RETANGULO')
    if (list[2]**2 > (list[1]**2 + list[0]**2)):
        print('TRIANGULO OBTUSANGULO')
    if (list[2]**2 < (list[1]**2 + list[0]**2)):
        print('TRIANGULO ACUTANGULO')
    if (list[2] == list[1] == list[0]):
        print('TRIANGULO EQUILATERO')
    if (list[2] == list[1] != list[0] or list[0] == list[1] != list[2] or list[0] == list[2] != list[1]):
        print('TRIANGULO ISOSCELES')
else:
    print('NAO FORMA TRIANGULO')
