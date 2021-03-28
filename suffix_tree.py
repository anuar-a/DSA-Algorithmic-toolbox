# python3
import sys


def build_suffix_tree(text):

  """Build a suffix tree of the string text and return a list
  with all of the labels of its edges (the corresponding
  substrings of the text) in any order."""

  result = []
  tree = {0:{}}
  count = 1
  for i in range(len(text)):
      current_node = 0
      print(text[i:])
      for j in text[i:]:
          current_symbol = j
          if current_symbol in tree[current_node]:
              current_node = tree[current_node][current_symbol]
          else:
              tree[current_node][current_symbol] = count
              current_node = count
              tree[count] = {}
              count = count + 1
  print(count)
  for i in tree:
      print(i, tree[i])
  for i in range(count):
      if i in tree and len(tree[i]) == 1:
          temp = str()
          for j in tree[i].keys():
              temp = temp + j
          for j in tree[i+1].keys():
              temp = temp + j
          tree[i] = {str(temp):i+2}
          tree.pop(i+1)
          print(tree[i])
  return result

if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  result = build_suffix_tree(text)
  print("\n".join(result))
