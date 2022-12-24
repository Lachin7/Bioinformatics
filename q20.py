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


class Cluster:
    def __init__(self, label, nodes=None, age=0.0):
        self.label = label
        if nodes is None:
            nodes = []
        self.nodes = nodes
        self.age = age


def UPGMA(D, n):
    all_clusters = []
    T = Tree()
    for i in range(1, n + 1):
        all_clusters.append(Cluster(i - 1, nodes=[i - 1]))
        T.nodes.append(Node(i - 1))
    clusters = all_clusters.copy()
    new_label = n
    while len(clusters) > 1:
        # find the two closest clusters Ci and Cj
        min_dist = 1000000
        c_i = None
        c_j = None
        for i in clusters:
            for j in clusters:
                if i != j:
                    distance = 0
                    for n1 in i.nodes:
                        for n2 in j.nodes:
                            distance += D[n1][n2]
                    distance /= float(len(i.nodes) * len(j.nodes))
                    if distance < min_dist:
                        min_dist = distance
                        c_i = i
                        c_j = j
        c_new = Cluster(new_label, age=min_dist/2, nodes=c_i.nodes + c_j.nodes)
        node_new = Node(c_new.label, age=c_new.age)
        T.nodes.append(node_new)
        node_i = T.find_node(c_i.label)
        node_j = T.find_node(c_j.label)
        node_i.neighbors.append((new_label, node_new.age - node_i.age))
        node_j.neighbors.append((new_label, node_new.age - node_j.age))
        node_new.neighbors.append((node_i.number, node_new.age - node_i.age))
        node_new.neighbors.append((node_j.number, node_new.age - node_j.age))
        new_label += 1

        distances = []
        for c in all_clusters:
            distance = 0
            for n1 in c_new.nodes:
                for n2 in c.nodes:
                    distance += D[n1][n2]
                distance /= float(len(c_new.nodes) * len(c.nodes))
                D[c.label].append(distance)
                distances.append(distance)
        D.append(distances + [0])
        clusters.remove(c_i)
        clusters.remove(c_j)
        clusters.append(c_new)
        all_clusters.append(c_new)
    T.print()


with open('q20.txt', 'r') as myfile:
    n = int(myfile.readline())
    D = [list(map(int, myfile.readline().split())) for i in range(n)]

UPGMA(D, n)
