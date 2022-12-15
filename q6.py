import numpy as np

whole_string = ""
with open('q6.txt', 'r') as myfile:
    lines = myfile.readlines()

for line in lines:
    if line.startswith(">"):
        whole_string = whole_string + line.strip() + ">"
    else:
        whole_string = whole_string + line.strip()

strings = whole_string.split(">")[1:]
# extract only the dna parts and not the id
dnas = strings[1::2]

if len(dnas[0]) <= len(dnas[1]):
    s = dnas[0]
    t = dnas[1]
else:
    s = dnas[1]
    t = dnas[0]

D = np.zeros((len(s) + 1, len(t) + 1))
for i in range(D.shape[0]):
    D[i, 0] = i
for i in range(D.shape[1]):
    D[0, i] = i

for i in range(1, D.shape[0]):
    for j in range(1, D.shape[1]):
        D_ver = D[i - 1, j] + 1
        D_hor = D[i, j - 1] + 1
        if s[i - 1] != t[j - 1]:
            D_diag = D[i - 1, j - 1] + 1
        else:
            D_diag = D[i - 1, j - 1]
        D[i, j] = min(D_ver, D_hor, D_diag)

s_modified, t_modified = "", ""
i, j = len(s), len(t)
while i > 0 and j > 0:
    D_ver, D_hor, D_diag = D[i - 1, j], D[i, j - 1], D[i - 1, j - 1]
    min_val = min(D_ver, D_hor, D_diag)
    if D[i, j] == min_val or (min_val != D_hor and min_val != D_ver) or (min_val == D_hor and min_val == D_ver):
        s_modified = s[i - 1] + s_modified
        t_modified = t[j - 1] + t_modified
        i -= 1
        j -= 1
    elif min_val == D_ver:
        t_modified = "-" + t_modified
        s_modified = s[i - 1] + s_modified
        i -= 1
    elif min_val == D_hor:
        s_modified = "-" + s_modified
        t_modified = t[j - 1] + t_modified
        j -= 1
print(int(D[-1][-1]))
print(s_modified)
print(t_modified)

