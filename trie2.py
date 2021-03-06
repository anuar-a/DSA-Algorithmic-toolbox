#Uses python3
import sys

# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.
def build_trie(patterns):
    #tree = {1:[3,'A'],2:[4]}
    #tree[2].append('B')
    #print(tree[2])
    # write your code here
    tree = {0:{}}
    count = 1
    for pattern in patterns:
        current_node = 0
        for i in pattern:
            current_symbol = i
            if current_symbol in tree[current_node]:
                current_node = tree[current_node][current_symbol]
            else:
                #new_node = max(tree.values()) + 1
                tree[current_node][current_symbol] = count
                current_node = count
                tree[count] = {}
                count = count + 1
            #print(count)
    #print(tree)
    return tree


if __name__ == '__main__':
    patterns = sys.stdin.read().split()[1:]
    tree = build_trie(patterns)
    #print(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))
