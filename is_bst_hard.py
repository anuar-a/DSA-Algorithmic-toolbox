#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

result = []
minval = -sys.maxsize
maxval = sys.maxsize

def IsBinarySearchTree(i,tree):
  # Implement correct algorithm here
  if tree == []:
      return True
  inOrder(i,tree)
  #rootindex = result.index(tree[0][0])
  result1 = [i[0] for i in result]
  #print(result1,rootindex)
  if result1 != sorted(result1):
      return False
  if result1[:rootindex] != [] and max(result1[:rootindex]) >= result1[rootindex]:
      return False
  if result1[rootindex + 1:] != [] and min(result1[rootindex+1:]) < result1[rootindex]:
      return False
  '''next = result.copy()
  result.clear()
  newroot = r
  for i in range(len(next)-1):
      if next[i] == next[i + 1]:
          for j in tree:
              if next[i] == j[0]:
                 if IsBinarySearchTree(tree.index(j),tree):
                     continue
                 else:
                     return False
  for i in range(len(result)-1):
      if result[i] > result[i + 1]:
          return False
  for i in range(len(result[:rootindex])):
      if result[i] >= result[rootindex]:
          return False
  for i in range(len(result[rootindex+1:])):
      if result[rootindex] > result[rootindex + 1 + i]:
          return False'''
  return True

def inOrder(i,tree):
  global rootindex
  if i == -1:
      return
  inOrder(tree[i][1],tree)
  result.append(tree[i])
  if len(result) >=2 and result[len(result)-1][0] == result[len(result)-2][0]:
      if tree.index(result[len(result)-1]) < tree.index(result[len(result)-2]) :
          result[len(result)-2][0] = result[len(result)-2][0] + 1

  if i == 0:
      rootindex = len(result)-1
  inOrder(tree[i][2],tree)

  return result

def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(0,tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
