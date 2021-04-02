numeros = input().split()
n1, n2, n3 = numeros
n1 = int(n1)
n2 = int(n2)
n3 = int(n3)

maior = int((n1 + n2 + abs(n1-n2) + 2*n3 + 2*abs((n1+n2+abs(n1-n2)-2*n3)/2))/4)

print(f"{maior} eh o maior")