from decimal import Decimal
A = float(format(Decimal(input()), '.2f'))
B = float(format(Decimal(input()), '.2f'))
C = float(format(Decimal(input()), '.2f'))
media = (A*2 + B*3 + C*5)/10
print("MEDIA = {:.1f}".format(media))