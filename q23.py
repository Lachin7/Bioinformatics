with open('q23.txt', 'r') as myfile:
    lines = myfile.readlines()

reads = []
for read in lines:
    reads.append(read.strip())
    reads.append(
        read.strip().replace('A', 'X').replace('T', 'Y').replace('G', 'Z').replace('C', 'K').replace('X', 'T').replace(
            'Y', 'A').replace(
            'Z', 'C').replace('K', 'G')[::-1])

G = {}
for read in reads:
    node1 = read[:len(read) - 1]
    node2 = read[1:]
    if node1 not in G:
        G[node1] = [node2]
    elif node2 not in G[node1]:
        G[node1].append(node2)

for a, nodes in sorted(G.items()):
    for n in nodes:
        print(f'({a}, {n})')

