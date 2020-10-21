#programmable by Belhaj Ayman MPSI2
def trianglePascal(n):
    T = [[0] * (n+1) for p in range(n+1)]
    for p in range(n+1):
        if n == 0:
            T[p][0] = 1
        else:
            for k in range(n+1):
                if k == 0:
                    T[p][0] = 1
                else:
                    T[p][k] = T[p-1][k-1] + T[p-1][k]
    for i in range(len(T)):
        print(T[i])

trianglePascal(5)
