import numpy as np


def global_alignment_dp_affine_gap_penalty(x, y, a, b, scoring_matrix):
    x_len = len(x)
    y_len = len(y)
    shape = (x_len + 1, y_len + 1)
    M, X, Y = np.zeros(shape, dtype='int'), np.zeros(shape, dtype='int'), np.zeros(shape, dtype='int')
    # we also need some backtrace matrices for each of them
    Mt, Xt, Yt = np.zeros(shape, dtype='int'), np.zeros(shape, dtype='int'), np.zeros(shape, dtype='int')

    # initialization
    max_neg = -10000
    for i in range(1, shape[0]):
        M[i, 0] = max_neg
        X[i, 0] = max_neg
        Y[i, 0] = -a - (i - 1) * b
    for j in range(1, shape[1]):
        M[0, j] = max_neg
        X[0, j] = -a - (j - 1) * b
        Y[0, j] = max_neg

    # filing the matrices
    for i in range(1, shape[0]):
        for j in range(1, shape[1]):
            M_scores = [M[i - 1, j - 1] + scoring_matrix[x[i - 1] + y[j - 1]],
                        X[i - 1, j - 1] + scoring_matrix[x[i - 1] + y[j - 1]],
                        Y[i - 1, j - 1] + scoring_matrix[x[i - 1] + y[j - 1]]]
            X_scores = [M[i, j - 1] - a, X[i, j - 1]-b, Y[i, j - 1] - a]
            Y_scores = [M[i - 1, j] -a, X[i - 1, j] -a, Y[i - 1, j] -b]
            M[i, j] = max(M_scores)
            X[i, j] = max(X_scores)
            Y[i, j] = max(Y_scores)

            Mt[i, j] = M_scores.index(M[i, j])
            Xt[i, j] = X_scores.index(X[i, j])
            Yt[i, j] = Y_scores.index(Y[i, j])

    # trace back to print the augmented strings
    x_modified, y_modified = "", ""
    i, j = len(x), len(y)
    backtrace_matrices = [Mt, Xt, Yt]
    vals = [M[i, j], X[i, j], Y[i, j]]
    current_mat = vals.index(max(vals))

    prev_mat = backtrace_matrices[current_mat][i, j]
    while i > 0 and j > 0:
        if current_mat == 0:
            x_modified = x[i - 1] + x_modified
            y_modified = y[j - 1] + y_modified
            i -= 1
            j -= 1
        elif current_mat == 1:
            x_modified = "-" + x_modified
            y_modified = y[j - 1] + y_modified
            j -= 1
        elif current_mat == 2:
            y_modified = "-" + y_modified
            x_modified = x[i - 1] + x_modified
            i -= 1
        current_mat = prev_mat
        prev_mat = backtrace_matrices[current_mat][i, j]

    if i == 0 and j != 0:
        x_modified = '-' * j + x_modified
        y_modified = y[:j] + y_modified
    elif i != 0 and j == 0:
        x_modified = x[:i] + x_modified
        y_modified = '-' * i + y_modified

    print(max(M[-1, -1], X[-1, -1], Y[-1, -1]))  # maximum_alignment_score
    print(x_modified)
    print(y_modified)


whole_string = ""
with open('q7.txt', 'r') as myfile:
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
    x = dnas[0]
    y = dnas[1]
else:
    x = dnas[1]
    y = dnas[0]

import blosum as bl

global_alignment_dp_affine_gap_penalty(x, y, 11, 1, bl.BLOSUM(62))
