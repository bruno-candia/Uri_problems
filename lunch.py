cardapio = {1: 4.00, 2: 4.50, 3: 5.00, 4: 2.00, 5: 1.50}

linha1 = input().split(" ")

pedido, quantidade = linha1

pedido = int(pedido)
quantidade = int(quantidade)

total = cardapio.get(pedido)*quantidade

print('Total: R$ {:.2f}'.format(total))
