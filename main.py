import random
def flouck ():
    art = []
    print('Введите размер матрицы n*n : ')
    global x
    x = int(input())
    global a
    a = []
    for i in range(x):
        mult = 1
        ab = False
        a.append([])
        for j in range(x):
            a[i].append(random.randint(-1,5))
            print(a[i][j], end=' ')
            if a[i][j] < 0 :
                ab = True
        print()
        if ab == False :
            for j in range(x) :
                mult = mult * a[i][j]
            art.append(mult)
    return print('Произведение элементов в тех строках, которые не содержат отрицательных элементов: ',art)
def maximum_1 ():
    mx = 0
    for i in range(1,x):
        s = 0
        s1 = 0
        j = 0
        while i + j < x :
            s += a[j][(i + j) % x ]
            s1 += a[(i + j) % x][j]
            j+=1
        # print('s =',s)
        # print('s1 =', s1)
        if s > mx :
            mx = s
        if s1 > mx :
            mx = s1
    print('Максимум среди сумм элементов диагоналей, параллельных главной диагонали матрицы: ',mx)
flouck()
maximum_1()

