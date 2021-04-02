p1 = input().split()
p2 = input().split()

x1, y1 = p1
x2, y2 = p2

distancia = (pow(float(x2) - float(x1),2) + pow(float(y2) - float(y1),2))**0.5

print("%.4f" %distancia)