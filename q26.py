with open('q26.txt', 'r') as myfile:
    lines = myfile.readlines()

reads_len = []
sum_len = 0
for read in lines:
    lenn = len(read.strip())
    reads_len.append(lenn)
    sum_len += lenn

temp = 0
N75 = 0
N50 = 0
reads_len.sort()
for i in reads_len:
    if sum_len - temp > sum_len // 2:
        N50 = i
    if sum_len - temp > (3 * sum_len) // 4:
        N75 = i
    temp += i

print(N50, N75)
