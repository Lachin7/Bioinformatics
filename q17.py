import numpy as np


class Node:
    def __init__(self, number):
        self.number = number
        self.neighbors = []

    def add_neighbor(self, neighbor, weight):
        self.neighbors.append((neighbor, weight))


with open('q17.txt', 'r') as myfile:
    lines = myfile.readlines()

n = int(lines[0])
nodes = []
nodes_num = []
for line in lines[1:]:
    command1 = line.split("->")
    node1 = int(command1[0])
    command2 = command1[1].split(":")
    node2 = int(command2[0])
    weight = int(command2[1])

    if node1 in nodes_num:
        for node in nodes:
            if node.number == node1:
                if node2 in nodes_num:
                    # we're going to find the node
                    for second_node in nodes:
                        if second_node.number == node2:
                            node.add_neighbor(second_node, weight)
                            break
                else:
                    # we're going to create the second node
                    second_node = Node(node2)
                    node.add_neighbor(second_node, weight)
                    nodes.append(second_node)
                    nodes_num.append(node2)
    else:
        # we're going to create the first node
        node = Node(node1)
        nodes.append(node)
        nodes_num.append(node1)
        if node2 in nodes_num:
            # we're going to find the node
            for second_node in nodes:
                if second_node.number == node2:
                    node.add_neighbor(second_node, weight)
                    break
        else:
            # we're going to create the second node
            second_node = Node(node2)
            node.add_neighbor(second_node, weight)
            nodes.append(second_node)
            nodes_num.append(node2)

# for node in nodes:
#     print(node.number)
#     for noden, weight in node.neighbors:
#         print(noden.number, weight)


def find_node(num):
    for n in nodes:
        if n.number == num:
            return n


def find_path_val(node, n2num,  i, j, total_weight=0, visited_neighbors=None):
        if visited_neighbors is None:
            visited_neighbors = []
        # print(total_weight)
        if n2num == node.number:
            if res[i, j] == 0:
                res[i, j] = total_weight
            return
        visited_neighbors.append(node.number)
        for neighbor, w in node.neighbors:
            if neighbor.number not in visited_neighbors:
                visited_neighbors.append(neighbor.number)
                find_path_val(neighbor, n2num, i, j,total_weight + w , visited_neighbors)


res = np.zeros((n, n)).astype('int')
for i in range(n):
    for j in range(n):
        node = find_node(i)
        find_path_val(node, j, i, j)


# for j in range(n):
#     for i in range(n):
#         print(str(res[:, j]).replace('[', '').replace(']', '') + "\n")

res = np.matrix(res).astype('int')
with open('matrix.txt', 'w') as testfile:
    for row in res:
        row = str(row).replace('[', '').replace(']', '')
        print(row)
        testfile.write(row + '\n')