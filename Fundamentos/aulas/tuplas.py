# Tuplas:
tupla1 = (0, 1, 2, 3, 4)  # homogênia
tupla2 = (2, 'a', 5.44, True, None)  # heterogênia

print(tupla2[1:4])
print(tupla1[-2:])
print(tupla2[:])

t1 = (30, 10, 20)
t2 = (2, 'a', 5.44, True)

print(t1 + t2)  # Concatenação
print(t1 * 3)  # Repetição
print(10 not in t1)  # filiação

# funções úteis
print(len(t2))
print(min(t1))
print(max(t1))
print(sum(t1))

tup1 = (1, 2, 3)
# t1[0] = 'a' -> ERRO
