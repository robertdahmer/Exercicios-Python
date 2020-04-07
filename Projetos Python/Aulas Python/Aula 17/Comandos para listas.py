# num = [2, 5, 9, 1]
# /num[2] = 3
# num.append(7)
# num.sort(reverse=True)
# num.insert(2, 0)
# num.pop()
# if 9 in num:
#     num.remove(2)
# else:
#     print(f'Não tem essa porra')
# print(num)
# print(f'Essa lista tem {len(num)} elementos.')

valores = list()
valores.append(2)
valores.append(4)
valores.append(9)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
