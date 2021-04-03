valor = int(input())
notas_disponiveis = [100, 50, 20, 10, 5, 2, 1]
print(valor)
for nota in notas_disponiveis:
  divisao = int(valor/nota)
  
  if(divisao > 0):
    valor = valor - divisao*nota
    
  print("{} nota(s) de R$ {},00".format(divisao,nota))
