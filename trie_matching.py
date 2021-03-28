# python3
import sys

NA = -1

class Node:
	def __init__ (self):
		self.next = [NA] * 4

def prefix_trie_matching(text,tree):
	count = 0
	symbol = text[count]
	v = 0

	while True:
		if len(tree[v]) == 0:
			return v
		elif symbol in tree[v]:
			v = tree[v][symbol]
			count = count + 1
			if count < len(text):
				symbol = text[count]
			else:
				symbol = ""
		else:
			return

def trie_matching(text,tree):
	result = []
	cursor = 0

	while len(text) > 0:
		if prefix_trie_matching(text,tree) != None:
			result.append(cursor)
		text = text[1:]
		cursor = cursor + 1

	return result

def solve (text, n, patterns):
	result = []
	tree = build_trie(patterns)

	return trie_matching(text,tree)

def build_trie(patterns):
    tree = {0:{}}
    count = 1

    for pattern in patterns:
        current_node = 0
        for i in pattern:
            current_symbol = i
            if current_symbol in tree[current_node]:
                current_node = tree[current_node][current_symbol]
            else:
                tree[current_node][current_symbol] = count
                current_node = count
                tree[count] = {}
                count = count + 1

    return tree

text = sys.stdin.readline ().strip ()
n = int (sys.stdin.readline ().strip ())
patterns = []
for i in range (n):
	patterns += [sys.stdin.readline ().strip ()]

ans = solve (text, n, patterns)

sys.stdout.write (' '.join (map (str, ans)) + '\n')
