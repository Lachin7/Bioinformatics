alphabet = input().split(" ")
num = int(input())
result = []

def get_k_mers(prev, k):
    if k == 0:
        result.append(prev)
        return
    for i in range(len(alphabet)):
        get_k_mers(prev+alphabet[i], k - 1)


get_k_mers("", num)
result.sort()

for i in range(len(result)):
    print(result[i])