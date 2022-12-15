class Node:
    def __init__(self, number):
        self.node_A = None
        self.node_C = None
        self.node_G = None
        self.node_T = None
        self.number = number


class Trie:
    def __init__(self):
        self.root = Node(0)

    def print_trie(self):
        print_node(self.root)

f = open("q4_output.txt", "w")



def print_node(node):
    if node.node_A is not None:
        print(str(node.number) + "->" + str(node.node_A.number) + ":A")
        print_node(node.node_A)
    if node.node_C is not None:
        print(str(node.number) + "->" + str(node.node_C.number) + ":C")
        print_node(node.node_C)
    if node.node_G is not None:
        print(str(node.number) + "->" + str(node.node_G.number) + ":G")
        print_node(node.node_G)
    if node.node_T is not None:
        print(str(node.number) + "->" + str(node.node_T.number) + ":T")
        print_node(node.node_T)


def trie_construction(patterns):
    trie = Trie()
    counter = 1
    for pattern in patterns:
        current_node = trie.root
        for i in range(len(pattern)):
            current_symbol = pattern[i]
            if current_symbol == 'A' and current_node.node_A is None:
                current_node.node_A = Node(counter)
                counter += 1
                current_node = current_node.node_A
            elif current_symbol == 'C' and current_node.node_C is None:
                current_node.node_C = Node(counter)
                counter += 1
                current_node = current_node.node_C
            elif current_symbol == 'G' and current_node.node_G is None:
                current_node.node_G = Node(counter)
                counter += 1
                current_node = current_node.node_G
            elif current_symbol == 'T' and current_node.node_T is None:
                current_node.node_T = Node(counter)
                counter += 1
                current_node = current_node.node_T
            elif current_symbol == 'A' and current_node.node_A is not None:
                current_node = current_node.node_A
            elif current_symbol == 'C' and current_node.node_C is not None:
                current_node = current_node.node_C
            elif current_symbol == 'G' and current_node.node_G is not None:
                current_node = current_node.node_G
            elif current_symbol == 'T' and current_node.node_T is not None:
                current_node = current_node.node_T
    return trie


input_data = []
with open('q4_input.txt', 'r') as myfile:
    lines = myfile.readlines()

for line in lines:
    input_data.append(line.strip())

trie = trie_construction(input_data)
trie.print_trie()


# f.write(result)
# f.close()