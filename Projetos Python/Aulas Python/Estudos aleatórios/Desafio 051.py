#Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.
print("""=========================
   10 TERMOS DE UMA PA
=========================""")
n1 = int(input('Primeiro termo:'))
n2 = int(input('Razão: '))
decimo = n1 + (10 - 1) * n2
for pa in range(n1, decimo, n2):
    print(pa, end=' > ')
print('ACABOU')
