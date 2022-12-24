def ham_dist(s1, s2):
    res = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            res += 1
    return res


def get_ripe(T, Tag):
    for v in T.keys():
        if Tag[v] == 0 and Tag[T[v][0]] == 1 and Tag[T[v][1]] == 1:
            return v
    return None


def min_ham_dist(s, v):
    min_score = min([s[k][v] for k in 'ATGC'])
    min_scores, min_ks = [], []
    for k in 'ACTG':
        if s[k][v] == min_score:
            min_ks.append(k)
    return min_score, min_ks


def calc_s(s, k, v):
    res = float('inf')
    for c in 'ACTG':
        if c == k:
            alpha = 0
        else:
            alpha = 1
        if s[c][v] + alpha < res:
            res = s[c][v] + alpha
    return res


def SmallParsimony(T, Character, A, parents):
    tags = {}
    s = {c: {} for c in 'ATCG'}
    for v in T.keys():
        tags[v] = 0
        if len(T[v]) == 0:
            tags[v] = 1
            for c in 'ATCG':
                if v[Character] == c:
                    s[c][v] = 0
                else:
                    s[c][v] = float('inf')

    v = get_ripe(T, tags)
    while not v == None:
        tags[v] = 1
        for c in 'ATCG':
            s[c][v] = calc_s(s, c, T[v][0]) + calc_s(s, c, T[v][1])
        w = v
        v = get_ripe(T, tags)
    v = w
    min_score, _ = min_ham_dist(s, v)
    back_track = [v]
    while back_track:
        v = back_track.pop()
        _, ks = min_ham_dist(s, v)
        if v in parents:
            if A[parents[v]][-1] not in ks:
                A[v] += ks[0]
            else:
                A[v] += A[parents[v]][-1]
        else:
            A[v] += ks[0]
        if T[v]:
            back_track.extend([T[v][0], T[v][1]])
    return min_score


with open('tree.txt', 'r') as myfile:
    lines = myfile.readlines()

T = {}
parents = {}
for line in lines[1:]:
    p = line.strip().split('->')[0]
    c = line.strip().split('->')[1]
    parents[c] = p
    if c not in T:
        T[c] = []
    if p in T:
        T[p].append(c)
    else:
        T[p] = [c]

n = int(lines[0].strip())
A = {k: '' for k in T.keys()}
score = 0
for Character in range(len(lines[1].strip().split('->')[1])):
    score += SmallParsimony(T, Character, A, parents)

with open('res.txt', 'w') as resfile:
    resfile.write(str(score) + '\n')
    for p in T.keys():
        if T[p]:
            resfile.write(str(A[p]) + '->' + str(A[T[p][0]]) + ':' + str(ham_dist(A[p], A[T[p][0]])) + '\n')
            resfile.write(str(A[p]) + '->' + str(A[T[p][1]]) + ':' + str(ham_dist(A[p], A[T[p][1]])) + '\n')
            resfile.write(str(A[T[p][0]]) + '->' + str(A[p]) + ':' + str(ham_dist(A[p], A[T[p][0]])) + '\n')
            resfile.write(str(A[T[p][1]]) + '->' + str(A[p]) + ':' + str(ham_dist(A[p], A[T[p][1]])) + '\n')
