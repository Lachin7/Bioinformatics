with open('q24.txt', 'r') as myfile:
    lines = myfile.readlines()

reads = []
for read in lines:
    reads.append(read.strip())
    reads.append(
        read.strip().replace('A', 'X').replace('T', 'Y').replace('G', 'Z').replace('C', 'K').replace('X', 'T').replace(
            'Y', 'A').replace(
            'Z', 'C').replace('K', 'G')[::-1])


for k in range(2, len(reads[0]))[::-1]:

    G = {}
    for read in reads:
        G[read] = []
        for d in range(len(reads[0])-k):
            G[read].append((read[d:d+k], read[d+1:d+k+1]))


    all_tuples = []
    for val in G.values():
        for tup in val:
            all_tuples.append(tup)


    all_tuples = list(set(all_tuples))
    def find_in_tuples(res0, next):
        for tup in all_tuples:
            if tup[0] == next:
                res0 += tup[0][-1]
                next = tup[1]
                all_tuples.remove(tup)

                return next, res0
        return None, None


    tup0 = all_tuples[0]
    res0 = tup0[0][-1]
    next = tup0[1]
    all_tuples.remove(tup0)
    cycle1_found = False
    while True:
        next, res0 = find_in_tuples(res0, next)
        if next is None:
            break
        if next == tup0[0]:
            cycle1_found = True
            my_res = res0
            break


    cycle2_found = False
    if cycle1_found:
        tup0 = all_tuples[0]
        res0 = tup0[0][-1]
        next = tup0[1]
        all_tuples.remove(tup0)
        while not cycle2_found:
            next, res0 = find_in_tuples(res0, next)
            if next is None:
                break
            if next == tup0[0]:
                cycle2_found = True
                break



    if len(all_tuples)==0 and cycle1_found and cycle2_found:
        print(res0)
        break




    #search for the next cycle:


