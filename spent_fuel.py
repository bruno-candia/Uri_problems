tempo_gasto_na_viagem = int(input())
velocidade_media = int(input())

distancia = velocidade_media*tempo_gasto_na_viagem

combustivel_necessario = distancia/12

print("%.3f" %combustivel_necessario)