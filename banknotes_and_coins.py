valor = float(input())
notas_disponiveis = [100, 50, 20, 10, 5, 2]
moedas_disponiveis = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print("NOTAS:")
for nota in notas_disponiveis:
  divisao = int(valor/nota)
  print("{} nota(s) de R$ {:.2f}".format(divisao,nota))
  valor = valor - divisao*nota

print("MOEDAS:")
for moeda in moedas_disponiveis:
  divisao = int(round(valor,2)/moeda)
  print("{} moeda(s) de R$ {:.2f}".format(divisao,moeda))
  valor = valor - divisao*moeda
    
  