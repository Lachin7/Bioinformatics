import sys

with open('q18.txt', 'r') as myfile:
    n = int(myfile.readline())
    j = int(myfile.readline())
    D = [list(map(int, myfile.readline().split())) for i in range(n)]

res = 1000000
for i in range(n):
    for k in range(n):
        if (i != j) and (j != k) and (i != k):
            res = min(res, (D[i][j] + D[j][k] - D[i][k])/2)

print(int(res))