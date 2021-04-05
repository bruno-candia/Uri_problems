# Minha solução

x, y, z = map(int, input().split())
segundoMaior = 0

maior = x + y + abs(x-y)
maior = int((maior + 2*z + 2*abs((maior - 2*z)/2))/4)

if x == maior:
    segundoMaior = (y + z + abs(y-z))/2

elif y == maior:
    segundoMaior = (x + z + abs(x-z))/2

elif z == maior:
    segundoMaior = (y + x + abs(y-x))/2

menor = x + y - abs(x-y)
menor = int((menor + 2*z - 2*abs((menor-2*z)/2))/4)

print(f"{menor}\n{int(segundoMaior)}\n{maior}\n")
print(f"{x}\n{y}\n{z}")


# Melhor solução
# X,Y,Z = map(int,input().split())
# list = [X,Y,Z]
# list.sort()
# print(f"{list[0]}\n{list[1]}\n{list[2]}")
# print(f"\n{X}\n{Y}\n{Z}")
