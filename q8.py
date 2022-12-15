import numpy as np
class pam250:
    matrix = {
        'A': {  'A': 2, 'R': -2, 'N':  0, 'D':  0, 'C': -2, 'Q':  0, 'E':  0, 'G':  1, 'H': -1, 'I': -1, 'L':  -2, 'K': -1, 'M': -1, 'F': -3, 'P':  1, 'S':  1, 'T':  1, 'W': -6, 'Y': -3, 'V':  0, 'B':  0, 'Z':  0, 'X':  0, '-': -8 },
        'R': { 'A': -2, 'R':  6, 'N':  0, 'D': -1, 'C': -4, 'Q':  1, 'E': -1, 'G': -3, 'H':  2, 'I': -2, 'L': -3, 'K':  3, 'M':  0, 'F': -4, 'P':  0, 'S':  0, 'T': -1, 'W':  2, 'Y': -4, 'V': -2, 'B': -1, 'Z':  0, 'X': -1, '-': -8 },
        'N': { 'A': 0, 'R':  0, 'N':  2, 'D':  2, 'C': -4, 'Q':  1, 'E':  1, 'G':  0, 'H':  2, 'I': -2, 'L': -3, 'K':  1, 'M': -2, 'F': -3, 'P':  0, 'S':  1, 'T':  0, 'W': -4, 'Y': -2, 'V': -2, 'B':  2, 'Z':  1, 'X':  0, '-': -8 },
        'D': { 'A': 0, 'R': -1, 'N':  2, 'D':  4, 'C': -5, 'Q':  2, 'E':  3, 'G':  1, 'H':  1, 'I': -2, 'L': -4, 'K':  0, 'M': -3, 'F': -6, 'P': -1, 'S':  0, 'T':  0, 'W': -7, 'Y': -4, 'V': -2, 'B':  3, 'Z':  3, 'X': -1, '-': -8 },
        'C': { 'A': -2, 'R': -4, 'N': -4 , 'D': -5, 'C': 12, 'Q': -5, 'E': -5, 'G': -3, 'H': -3, 'I': -2, 'L': -6, 'K': -5, 'M': -5, 'F': -4, 'P': -3, 'S':  0, 'T': -2, 'W': -8, 'Y':  0, 'V': -2, 'B': -4, 'Z': -5, 'X': -3, '-': -8 },
        'Q': {  'A': 0, 'R':  1, 'N':  1, 'D':  2, 'C': -5, 'Q':  4, 'E':  2, 'G': -1, 'H':  3, 'I': -2, 'L': -2, 'K':  1, 'M': -1, 'F': -5, 'P':  0, 'S': -1, 'T': -1, 'W': -5, 'Y': -4, 'V': -2, 'B':  1, 'Z':  3, 'X': -1, '-': -8 },
        'E': {  'A': 0, 'R': -1, 'N':  1, 'D':  3, 'C': -5, 'Q':  2, 'E':  4, 'G':  0, 'H':  1, 'I': -2, 'L': -3, 'K':  0, 'M': -2, 'F': -5, 'P': -1, 'S':  0, 'T':  0, 'W': -7, 'Y': -4, 'V': -2, 'B':  3, 'Z':  3, 'X': -1, '-': -8 },
        'G': {  'A': 1, 'R': -3, 'N':  0, 'D':  1, 'C': -3, 'Q': -1, 'E':  0, 'G':  5, 'H': -2, 'I': -3, 'L': -4, 'K': -2, 'M': -3, 'F': -5, 'P':  0, 'S':  1, 'T':  0, 'W': -7, 'Y': -5, 'V': -1, 'B':  0, 'Z':  0, 'X': -1, '-': -8 },
        'H': { 'A': -1, 'R':  2, 'N':  2, 'D':  1, 'C': -3, 'Q':  3, 'E':  1, 'G': -2, 'H':  6, 'I': -2, 'L': -2, 'K':  0, 'M': -2, 'F': -2, 'P':  0, 'S': -1, 'T': -1, 'W': -3, 'Y':  0, 'V': -2, 'B': 1, 'Z':  2, 'X': -1, '-': -8 },
        'I': { 'A': -1, 'R': -2, 'N': -2, 'D': -2, 'C': -2, 'Q': -2, 'E': -2, 'G': -3, 'H': -2, 'I':  5, 'L':  2, 'K': -2, 'M':  2, 'F':  1, 'P': -2, 'S': -1, 'T':  0, 'W': -5, 'Y': -1, 'V':  4, 'B': -2, 'Z': -2, 'X': -1, '-': -8 },
        'L': { 'A': -2, 'R': -3, 'N': -3, 'D': -4, 'C': -6, 'Q': -2, 'E': -3, 'G': -4, 'H': -2, 'I':  2, 'L':  6, 'K': -3, 'M':  4, 'F':  2, 'P': -3, 'S': -3, 'T': -2, 'W': -2, 'Y': -1, 'V':  2, 'B': -3, 'Z': -3, 'X': -1, '-': -8 },
        'K': { 'A': -1, 'R':  3, 'N':  1, 'D':  0, 'C': -5, 'Q':  1, 'E':  0, 'G': -2, 'H':  0, 'I': -2, 'L': -3, 'K':  5, 'M':  0, 'F': -5, 'P': -1, 'S':  0, 'T':  0, 'W': -3, 'Y': -4, 'V': -2, 'B':  1, 'Z':  0, 'X': -1, '-': -8 },
        'M': { 'A': -1, 'R':  0, 'N': -2, 'D': -3, 'C': -5, 'Q': -1, 'E': -2, 'G': -3, 'H': -2, 'I':  2, 'L':  4, 'K':  0, 'M':  6, 'F':  0, 'P': -2, 'S': -2, 'T': -1, 'W': -4, 'Y': -2, 'V':  2, 'B': -2, 'Z': -2, 'X': -1, '-': -8 },
        'F': { 'A': -3, 'R': -4, 'N': -3, 'D': -6, 'C': -4, 'Q': -5, 'E': -5, 'G': -5, 'H': -2, 'I':  1, 'L':  2, 'K': -5, 'M':  0, 'F':  9, 'P': -5, 'S': -3, 'T': -3, 'W':  0, 'Y':  7, 'V': -1, 'B': -4, 'Z': -5, 'X': -2, '-': -8 },
        'P': {  'A': 1, 'R':  0, 'N':  0, 'D': -1, 'C': -3, 'Q':  0, 'E': -1, 'G':  0, 'H':  0, 'I': -2, 'L': -3, 'K': -1, 'M': -2, 'F': -5, 'P':  6, 'S':  1, 'T':  0, 'W': -6, 'Y': -5, 'V': -1, 'B': -1, 'Z':  0, 'X': -1, '-': -8 },
        'S': {  'A': 1, 'R': 0, 'N':  1, 'D':  0, 'C':  0, 'Q': -1, 'E':  0, 'G':  1, 'H': -1, 'I': -1, 'L': -3, 'K':  0, 'M': -2, 'F': -3, 'P':  1, 'S':  2, 'T':  1, 'W': -2, 'Y': -3, 'V': -1, 'B':  0, 'Z':  0, 'X':  0, '-': -8 },
        'T': {  'A': 1, 'R': -1, 'N':  0, 'D':  0, 'C': -2, 'Q': -1, 'E':  0, 'G':  0, 'H': -1, 'I':  0, 'L': -2, 'K':  0, 'M': -1, 'F': -3, 'P':  0, 'S':  1, 'T':  3, 'W': -5, 'Y': -3, 'V':  0, 'B':  0, 'Z': -1, 'X':  0, '-': -8 },
        'W': { 'A': -6, 'R':  2, 'N': -4, 'D': -7, 'C': -8, 'Q': -5, 'E': -7, 'G': -7, 'H': -3, 'I': -5, 'L': -2, 'K': -3, 'M': -4, 'F':  0, 'P': -6, 'S': -2, 'T': -5, 'W': 17, 'Y':  0, 'V': -6, 'B': -5, 'Z': -6, 'X': -4, '-': -8 },
        'Y': { 'A': -3, 'R': -4, 'N': -2, 'D': -4, 'C':  0, 'Q': -4, 'E': -4, 'G': -5, 'H':  0, 'I': -1, 'L': -1, 'K': -4, 'M': -2, 'F':  7, 'P': -5, 'S': -3, 'T': -3, 'W':  0, 'Y': 10, 'V': -2, 'B': -3, 'Z': -4, 'X': -2, '-': -8 },
        'V': {  'A': 0, 'R': -2, 'N': -2, 'D': -2, 'C': -2, 'Q': -2, 'E': -2, 'G': -1, 'H': -2, 'I':  4, 'L':  2, 'K': -2, 'M':  2, 'F': -1, 'P': -1, 'S': -1, 'T':  0, 'W':  -6, 'Y': -2, 'V':  4, 'B': -2, 'Z': -2, 'X': -1, '-': -8 },
        'B': { 'A': 0, 'R': -1, 'N':  2, 'D':  3, 'C': -4, 'Q':  1, 'E':  3, 'G':  0, 'H':  1, 'I': -2, 'L': -3, 'K':  1, 'M': -2, 'F': -4, 'P': -1, 'S':  0, 'T':  0, 'W': -5, 'Y': -3, 'V': -2, 'B':  3, 'Z':  2, 'X': -1, '-': -8 },
        'Z': {  'A': 0, 'R':  0, 'N':  1, 'D':  3, 'C': -5, 'Q':  3, 'E':  3, 'G':  0, 'H':  2, 'I': -2, 'L': -3, 'K':  0, 'M': -2, 'F': -5, 'P':  0, 'S':  0, 'T': -1, 'W': -6, 'Y': -4, 'V': -2, 'B':  2, 'Z':  3, 'X': -1, '-': -8 },
        'X': {  'A': 0, 'R': -1, 'N':  0, 'D': -1, 'C': -3, 'Q': -1, 'E': -1, 'G': -1, 'H': -1, 'I': -1, 'L': -1, 'K': -1, 'M': -1, 'F': -2, 'P': -1, 'S':  0, 'T':  0, 'W': -4, 'Y': -2, 'V': -1, 'B': -1, 'Z': -1, 'X': -1, '-': -8 },
        '-': { 'A': -8, 'R': -8, 'N': -8, 'D': -8, 'C': -8, 'Q': -8, 'E': -8, 'G': -8, 'H': -8, 'I': -8, 'L': -8, 'K': -8, 'M': -8, 'F': -8, 'P': -8, 'S': -8, 'T': -8, 'W': -8, 'Y': -8, 'V': -8, 'B': -8, 'Z': -8, 'X': -8, '-':  1 }
    }

PAM250 = pam250.matrix
whole_string = ""
with open('q8.txt', 'r') as myfile:
    lines = myfile.readlines()

for line in lines:
    if line.startswith(">"):
        whole_string = whole_string + line.strip() + ">"
    else:
        whole_string = whole_string + line.strip()

strings = whole_string.split(">")[1:]
# extract only the dna parts and not the id
dnas = strings[1::2]
s = dnas[0]
t = dnas[1]
max_score = -1

i_opt, j_opt = 0, 0

D = np.zeros((len(s) + 1, len(t) + 1))
for i in range(1,D.shape[0]):
    D[i, 0] = D[i-1,0] - 5
for i in range(1,D.shape[1]):
    D[0, i] = D[0,i-1] - 5


for i in range(1, D.shape[0]):
    for j in range(1, D.shape[1]):
        max_val = max(0, D[i - 1, j] - 5, D[i, j - 1] - 5, D[i - 1, j - 1] + PAM250[s[i - 1]][ t[j - 1]])
        D[i, j] = max_val
        if max_val > max_score:
            max_score = max_val
            i_opt, j_opt = i, j

s_modified, t_modified = "", ""
i, j = i_opt, j_opt
while D[i, j] > 0:
    if D[i, j] == D[i - 1, j - 1] + PAM250[s[i - 1]][t[j - 1]]:
        s_modified = s[i - 1] + s_modified
        t_modified = t[j - 1] + t_modified
        i -= 1
        j -= 1
    elif D[i, j] == D[i - 1, j] - 5:
        t_modified = "-" + t_modified
        s_modified = s[i - 1] + s_modified
        i -= 1
    elif D[i, j] == D[i, j - 1] - 5:
        s_modified = "-" + s_modified
        t_modified = t[j - 1] + t_modified
        j -= 1
print(int(max_score))
print(s_modified.replace('-',''))
print(t_modified.replace('-',''))