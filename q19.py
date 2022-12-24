class Tree:
    def __init__(self, nodes=None):
        if nodes is None:
            nodes = []
        self.nodes = nodes

    def insert_node(self, src, dest, dist,new_node_num):
        path = self.traverse(src, dest)
        # print(path)
        for i in range(len(path) - 1):
            node = path[i]
            next = path[i + 1]
            w = 0
            for neighbor, weight in self.find_node(node).neighbors:
                if neighbor == next:
                    w = weight
                    break
            if dist >= w:
             dist -=w
            else:
                break
        new_node = Node(new_node_num)
        self.find_node(node).neighbors.append((new_node.number, dist))
        self.find_node(next).neighbors.append((new_node.number, w - dist))
        new_node.neighbors.append((node, dist))
        new_node.neighbors.append((next, w - dist))
        self.nodes.append(new_node)
        self.remove_edge(node, next)

    def remove_edge(self, src, target):
        src_node = self.find_node(src)
        for neighbor, weight in src_node.neighbors:
            if neighbor == target:
                src_node.neighbors.remove((neighbor, weight))

        tar_node = self.find_node(target)
        for neighbor, weight in tar_node.neighbors:
            if neighbor == src:
                tar_node.neighbors.remove((neighbor, weight))

    def find_node(self, num):
        for n in self.nodes:
            if n.number == num:
                return n

    def traverse(self, src, dest, visited_nodes=None):
        if visited_nodes is None:
            visited_nodes = []
        visited_nodes.append(src)
        src_node = self.find_node(src)
        for neighbor, weight in src_node.neighbors:
            if neighbor in visited_nodes:
                continue
            if neighbor == dest:
                return [src, dest]
            path = self.traverse(neighbor, dest, visited_nodes)
            if path is not None:
                return [src] + path
        return None

    def print(self):
        for n in self.nodes:
            for neighbor, weight in n.neighbors:
                print(str(n.number) + "->" + str(neighbor) + ":" + str(int(weight)))


class Node:
    def __init__(self, number, neighbors=None):
        if neighbors is None:
            neighbors = []
        self.number = number
        self.neighbors = neighbors

    def add_neighbor(self, neighbor, weight):
        self.neighbors.append((neighbor, weight))


with open('q19.txt', 'r') as myfile:
    n = int(myfile.readline())
    # j = int(myfile.readline())
    D = [list(map(int, myfile.readline().split())) for i in range(n)]


def calc_limb_len(D, n, j):
    res = 10000000
    for i in range(n):
        for k in range(n):
            if (i != j) and (j != k) and (i != k):
                res = min(res, (D[i][j] + D[j][k] - D[i][k]) / 2)
    return res


def additive_phylogeny(D, n, new_node_num):
    # if n = 2
    #         return the tree consisting of a single edge of length D1,2
    if n == 2:
        return Tree([Node(0, [(1, D[0][1])]), Node(1, [(0, D[0][1])])])

    # limbLength ← Limb(D, n)
    #     for j ← 1 to n - 1
    #         Dj,n ← Dj,n - limbLength
    #         Dn,j ← Dj,n
    lim_len = calc_limb_len(D, n, n - 1)
    for j in range(n - 1):
        D[j][n - 1] = D[j][n - 1] - lim_len
        D[n - 1][j] = D[j][n - 1]

    # (i,n,k) ← three leaves such that Di,k = Di,n + Dn,k
    #  x ← Di,n
    for i in range(n-1):
        for k in range(i+1, n-1):
            if D[i][k] == D[i][n - 1] + D[k][n-1] and i != k:
                src, des, node, x = i, k, n - 1, D[i][n - 1]
                break

    # remove row n and column n from D
    #     T ← AdditivePhylogeny(D, n - 1)
    T = additive_phylogeny(D, n - 1, new_node_num - 1)
    # [D[ind][:-1] for ind in range(n - 1)]
    #     v ← the (potentially new) node in T at distance x from i on the path between i and k
    T.insert_node(src, des, x, new_node_num)
    #     add leaf n back to T by creating a limb (v, n) of length limbLength
    #     return T
    if T.find_node(n-1) is None:
        T.nodes.append(Node(n-1, [(new_node_num, lim_len)]))
    else:
        T.find_node(n - 1).neighbors.append((new_node_num, lim_len))

    if T.find_node(new_node_num) is None:
        T.nodes.append(Node(new_node_num, [(n-1, lim_len)]))
    else:
        T.find_node(new_node_num).neighbors.append((n-1, lim_len))
    return T


T = additive_phylogeny(D, n, 2 * n - 3)
T.print()
