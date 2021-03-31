e = 2.718281828182818
w = 0.0
n = 1000
x = 970
i = 0
i1 = 0
cont = 0
for i1 in range(n-x):
    j1 = 0
    fatX = 1

    for j1 in range(x-1, 0, -1):
        fatX += fatX*j1

#    print(fatX)

    j2 = 0
    fatN = 1
    for j2 in range(n-1, 0, -1):
        fatN += fatN*j2
#    print(fatN)

    j3 = 0
    fatNX = 1
    for j3 in range(n-x-1, 0, -1):
        fatNX += fatNX*j3

    nCr = fatN/(fatX*fatNX)
#    print(fatNX)
#    print(nCr)

    w += nCr * (pow(0.98, x)) * (pow(0.02, n-x))
    x += 1

ans = 1-w
print(w)
# chances de erros
print(ans)
# chances de acertos
