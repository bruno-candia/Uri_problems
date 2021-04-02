nome_do_vendedor = str(input())
salario_fixo= float(input())
total_de_vendas_em_dinheiro = float(input())

salario_final_do_mes = (salario_fixo + total_de_vendas_em_dinheiro*0.15)
print("TOTAL = R$ {:.2f}".format(salario_final_do_mes))