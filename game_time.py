horaInicial, minutoInicial, horaFinal, minutoFinal = map(int, input().split())

tempoHoraTotal = horaFinal - horaInicial

if tempoHoraTotal < 0:
    tempoHoraTotal = 24 + tempoHoraTotal

tempoMinutoTotal = minutoFinal - minutoInicial

if tempoMinutoTotal < 0:
    tempoMinutoTotal = 60 + tempoMinutoTotal

    if tempoHoraTotal == 0:
        tempoHoraTotal = 24

    tempoHoraTotal = tempoHoraTotal - 1

if horaInicial == horaFinal and minutoInicial == minutoFinal:
    print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
else:
    print(
        f'O JOGO DUROU {tempoHoraTotal} HORA(S) E {tempoMinutoTotal} MINUTO(S)')
