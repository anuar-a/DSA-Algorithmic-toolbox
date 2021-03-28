#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

result = []

def IsBinarySearchTree(tree):
  # Implement correct algorithm here
  if tree == []:
      return True
  inOrder(0,tree)
  for i in range(len(result)-1):
      if result[i] > result[i + 1]:
          return False
  return True

def inOrder(i,tree):
  if i == -1:
      return
  inOrder(tree[i][1],tree)
  result.append(tree[i][0])
  inOrder(tree[i][2],tree)
  return result

def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  #print(nodes)
  #print(tree)
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
