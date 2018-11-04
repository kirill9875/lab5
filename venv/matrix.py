from random import random


def maximum_1 (ad):
    mx = 0
    for i in range(1,N):
        s = 0
        s1 = 0
        j = 0
        while i + j < N :
            s += ad[j][(i + j) % N ]
            s1 += ad[(i + j) % N][j]
            j+=1
        print('s =',s)
        print('s1 =', s1)
        if s > mx :
            mx = s
        if s1 > mx :
            mx = s1
    print(mx)



N = 3
a = []
for i in range(N):
    b = []
    for j in range(N):
        n = int(random() * 10)
        b.append(n)
        print("%3d" % n, end='')
    a.append(b)
    print()
ch = input("Главная (1) или побочная (2): ")
if ch == '1' or ch == '2':
    summa = diagonal(a, ch)
    print(summa)

maximum_1(a)
