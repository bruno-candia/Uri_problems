numero_de_funcionarios = int(input())
hora_de_trabalho= int(input())
valor_por_hora = float(input())

salario = (hora_de_trabalho*valor_por_hora)
print("NUMBER = {}\nSALARY = U$ {:.2f}".format(numero_de_funcionarios,salario))