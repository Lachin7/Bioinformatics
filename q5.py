import numpy as np

whole_string = ""
with open('q5.txt', 'r') as myfile:
    lines = myfile.readlines()

for line in lines:
    if line.startswith(">"):
        whole_string = whole_string + line.strip() + ">"
    else:
        whole_string = whole_string + line.strip()

strings = whole_string.split(">")[1:]
# extract only the dna parts and not the id
strings = strings[1::2]
n = len(strings)

D = np.zeros((n, n))
for i in range(n):
    for j in range(i, n):
        if i == j:
            D[i, j] = 0
        else:
            si = strings[i]
            sj = strings[j]
            arr_diff = [k for k in range(len(si)) if si[k] != sj[k]]
            D[i, j] = len(arr_diff)/len(si)
            D[j, i] = len(arr_diff)/len(si)

float_formatter = "{:.5f}".format
np.set_printoptions(formatter={'float_kind':float_formatter})
print(str(D).replace(' [', '').replace('[', '').replace(']', ''))