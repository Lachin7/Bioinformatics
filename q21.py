import numpy as np


class Tree:
    def __init__(self, nodes=None):
        if nodes is None:
            nodes = []
        self.nodes = nodes

    def insert_node(self, src, dest, dist, new_node_num):
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
                dist -= w
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
                print(str(n.number) + "->" + str(neighbor) + ":" + f'{weight:.3f}')


class Node:
    def __init__(self, number, neighbors=None, age=0.0):
        if neighbors is None:
            neighbors = []
        self.number = number
        self.neighbors = neighbors
        self.age = age

    def add_neighbor(self, neighbor, weight):
        self.neighbors.append((neighbor, weight))


def create_neighbor_joining_mat(D, n):
    res = np.zeros((n, n)).astype(float)
    for i in range(n):
        for j in range(i+1, n):
            res[i, j] = (n - 2) * D[i][j] - [sum(row) for row in D][i] - [sum(row) for row in D][j]
            res[j, i] = res[i, j]
    return res


def create_delta_mat(D, n):
    res = np.zeros((n, n)).astype(float)
    for i in range(n):
        for j in range(i+1, n):
            res[i, j] = ([sum(row) for row in D][i] - [sum(row) for row in D][j]) / (n - 2)
            res[j, i] = res[i, j]
    return res


def neighbor_joining(D, n, nodes):
    if n == 2:
        return Tree([Node(nodes[0], [(nodes[1], D[0][1])]), Node(nodes[1], [(nodes[0], D[0][1])])])

    m = nodes[-1] + 1
    nodes.append(m)
    D_p = create_neighbor_joining_mat(D, n)
    min_i, min_j, min_val = 0, 0, 1000000.0
    for i in range(n):
        for j in range(n):
            if i != j:
                if D_p[i, j] < min_val:
                    min_i = i
                    min_j = j
                    min_val = D_p[i, j]
    Delta = create_delta_mat(D, n)
    limb_len_i = (D[min_i][min_j] + Delta[min_i, min_j]) / 2
    limb_len_j = (D[min_i][min_j] - Delta[min_i, min_j]) / 2

    new_row = []
    for i in range(n):
        val = 0.5 * (D[i][min_i] + D[i][min_j] - D[min_i][min_j])
        new_row.append(val)
        D[i].append(val)

    new_row += [0.0]
    D.append(new_row)

    D_new = []
    for j in range(len(D)):
        if j != max(min_i, min_j):
            D_new.append([D[j][k] for k in range(len(D[j])) if k != max(min_i, min_j)])
    D = []
    for j in range(len(D_new)):
        if j != min(min_i, min_j):
            D.append([D_new[j][k] for k in range(len(D_new[j])) if k != min(min_i, min_j)])
    # D_new = []
    # for i in range(len(D)):
    #     for j in range(len(D)):
    #         if i != min_i and j!=min_i and i != min_j and j!=min_j:
    #             D_new[i][j] = D[i][j]
    # print(len(D))
    # print(min_i, min_j)
    # D_new = np.zeros((len(D),len(D)))
    # for i in range(len(D)):
    #     for j in range(len(D[i])):
    #         D_new[i, j] = D[i][j]
    # print(D_new)
    # np.delete(D_new, min_i, 0)
    # np.delete(D_new, [min_i, min_j], 0)
    # print(D_new)
    # np.delete(D_new, [min_i, min_j], 1)
    # D_new = []
    # for i in range(len(D_new)):
    #     for j in range(len(D_new[i])):
    #         if i != min_j and j != min_j:
    #             D_new.append(D_new[i][j])

    # D = D_new.tolist()
    # print(D)
    node_i = nodes[min_i]
    node_j = nodes[min_j]
    nodes.remove(node_i)
    nodes.remove(node_j)
    T = neighbor_joining(D, n - 1, nodes)

    if T.find_node(node_i) is None:
        T.nodes.append(Node(node_i, [(m, limb_len_i)]))
    else:
        T.find_node(node_i).neighbors.append((m, limb_len_i))

    if T.find_node(node_j) is None:
        T.nodes.append(Node(node_j, [(m, limb_len_j)]))
    else:
        T.find_node(node_j).neighbors.append((m, limb_len_j))

    if T.find_node(m) is None:
        T.nodes.append(Node(m, [(node_i, limb_len_i), (node_j, limb_len_j)]))
    else:
        T.find_node(m).neighbors.append((node_i, limb_len_i))
        T.find_node(m).neighbors.append((node_j, limb_len_j))
    return T
    # T.find_node(min_i).neighbors().append((m, limb_len_i))
    # T.find_node(min_j).neighbors().append((m, limb_len_j))
    # del D[min_i]
    # del D[min_j]


with open('q21.txt', 'r') as myfile:
    n = int(myfile.readline())
    D = [list(map(int, myfile.readline().split())) for i in range(n)]

neighbor_joining(D, n, list(range(n))).print()
