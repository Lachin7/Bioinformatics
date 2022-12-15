import numpy as np
import blosum as bl

whole_string = ""
with open('q9.txt', 'r') as myfile:
    lines = myfile.readlines()

for line in lines:
    if line.startswith(">"):
        whole_string = whole_string + line.strip() + ">"
    else:
        whole_string = whole_string + line.strip()

strings = whole_string.split(">")[1:]
# extract only the dna parts and not the id
dnas = strings[1::2]
x = dnas[0]
y = dnas[1]
max_score = -1
a, b = 11, 1
scoring_matrix = bl.BLOSUM(62)
i_opt, j_opt = 0, 0
print(x)
print(y)
x_len = len(x)
y_len = len(y)
shape = (x_len + 1, y_len + 1)
M, X, Y, B = np.zeros(shape, dtype='int'), np.zeros(shape, dtype='int'), np.zeros(shape, dtype='int'), np.zeros(shape, dtype='int')


for i in range(1, shape[0]):
    for j in range(1, shape[1]):

        # X_scores = []
        # Y_scores = [M[i, j-1] - a, Y[i, j-1] - b]
        X[i, j] = max(M[i-1, j] - a, X[i-1, j] - b)
        Y[i, j] = max(M[i, j-1] - a, Y[i, j-1] - b)
        M_scores = [M[i - 1, j - 1] + scoring_matrix[x[i - 1] + y[j - 1]],
                    X[i, j], Y[i, j], 0]
        M[i, j] = max(M_scores)

        B[i, j] = M_scores.index(M[i,j])
        if M[i, j] > max_score:
            max_score = M[i, j]
            i_opt, j_opt = i, j

s_modified, t_modified = "", ""
i, j = i_opt, j_opt

while B[i, j] >= 0 and i * j !=0:
    if B[i, j] == 0:
        i -= 1
        j -= 1
    elif B[i, j] == 1:
        i -= 1
    elif B[i, j] == 2:
        j -= 1
# print(i_opt, j_opt, i, j)
print(int(max_score))
print(x[i: i_opt])
print(y[j:j_opt])


