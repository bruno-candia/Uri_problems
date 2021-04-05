A, B, C = map(float, input().split())
list = [A, B, C]
list.sort()

if (list[0] + list[1]) > list[2]:
    perimetroDoTriangulo = list[0] + list[1] + list[2]
    print('Perimetro = %.1f' % perimetroDoTriangulo)
else:
    areaDoTrapezio = ((B+A)*C)/2
    print('Area = %.1f' % areaDoTrapezio)
