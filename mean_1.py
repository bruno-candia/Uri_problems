from decimal import Decimal
A = float(format(Decimal(input()), '.2f'))
B = float(format(Decimal(input()), '.2f'))
media = (A*3.5 + B*7.5)/11
print("MEDIA = {:.5f}".format(media))