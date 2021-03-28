#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

result = []

def check_array(result,rootindex):
  if result != sorted(result):
      return False
  if result[:rootindex] != [] and max(result[:rootindex]) >= result[rootindex]:
      return False
  if result[rootindex+1:] != [] and min(result[rootindex+1:]) < result[rootindex]:
      return False
  result = []
  return True

def IsBinarySearchTree(tree):
  # Implement correct algorithm here
  answer = []
  if tree == []:
      return True
  inOrder(0,tree,0)
  #if [i[0] for i in result] != sorted([i[0] for i in result]):
  if check_array([i[0] for i in result],rootindex) == False:
      return False
  else:
      result1 = result[:rootindex]
      for i in range(len(result1)-1):
          if result1[i][0] == result1[i + 1][0]:
              answer.append(result1[i])
              answer.append(result1[i+1])
  # print('Yes')
  #print(answer)
  result.clear()
  for i in range(len(answer)-1):
      inOrder(tree.index(answer[i]),tree,tree.index(answer[i]))
      #print(result)
      if not check_array([i[0] for i in result],rootindex):
          return False
      result.clear()
  '''if len(tree) < 100:
      for i in range(len(tree)-1):
          inOrder(i,tree,i)
         # print(result,rootindex)
          if not check_array(result,rootindex):
              return False
          result.clear()
  else:
      for i in range(100):
          inOrder(i,tree,i)
         # print(result,rootindex)
          if not check_array(result,rootindex):
              return False
          result.clear()'''


  return True
  '''for i in range(len(result)-1):
      if result[i] > result[i + 1]:
          return False
  for i in range(len(result[:rootindex])):
      if result[i] >= result[rootindex]:
          return False
  for i in range(len(result[rootindex+1:])):
      if result[rootindex] > result[rootindex + 1 + i]:
          return False'''


def inOrder(i,tree,j):
  global rootindex
  if i == -1:
      return
  inOrder(tree[i][1],tree,0)
  result.append(tree[i])
  if tree[i] == tree[j]:
      rootindex = len(result)-1
  inOrder(tree[i][2],tree,0)
  return result

def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
