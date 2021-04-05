N = input().split(" ")
NP6 = 0
N1, N2, N3, N4 = N
N1 = float(N1)
N2 = float(N2)
N3 = float(N3)
N4 = float(N4)

N5 = (N1*2 + N2*3 + N3*4 + N4*1)/10
print('Media: {:.1f}'.format(N5))

if (5 <= N5 < 7.0):
    print('Aluno em exame.')
    NP6 = float(input())
    print('Nota do exame: {:.1f}'.format(NP6))
    NP6 = (N5 + NP6)/2

if(N5 >= 7.0 or NP6 > 5.0):
    print('Aluno aprovado.')
    if(NP6 > 5.0):
        print('Media final: {:.1f}'.format(NP6))
else:
    print('Aluno reprovado.')
