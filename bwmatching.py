# python3
import sys


def PreprocessBWT(bwt):
  """
  Preprocess the Burrows-Wheeler Transform bwt of some text
  and compute as a result:
    * starts - for each character C in bwt, starts[C] is the first position
        of this character in the sorted array of
        all characters of the text.
    * occ_count_before - for each character C in bwt and each position P in bwt,
        occ_count_before[C][P] is the number of occurrences of character C in bwt
        from position 0 to position P inclusive.
  """
  # Implement this function yourself
  str_ref = '$ACGT'
  a_count = 0
  c_count = 0
  g_count = 0
  t_count = 0
  counts = [1,a_count,c_count,g_count,t_count]
  S_list = [0]
  a_list = [0]
  c_list = [0]
  g_list = [0]
  t_list = [0]

  for i in range(len(bwt)):
      if bwt[i] == 'A':
          a_count = a_count + 1
      if bwt[i] == 'C':
          c_count = c_count + 1
      if bwt[i] == 'G':
          g_count = g_count + 1
      if bwt[i] == 'T':
          t_count = t_count + 1
  starts = {'$':0, 'A':1, 'C':1 + a_count, 'G':1 + a_count + c_count, 'T': 1 + a_count + c_count + g_count}
  occ_counts_before = dict()
  '''for i in range(len(bwt)):
      a_list.append(bwt[0:i+1].count('A'))
      c_list.append(bwt[0:i+1].count('C'))
      g_list.append(bwt[0:i+1].count('G'))
      t_list.append(bwt[0:i+1].count('T'))
      S_list.append(bwt[0:i+1].count('$'))'''
  for i in range(len(bwt)):
      if bwt[i] == '$':
          a_list.append(a_list[-1])
          c_list.append(c_list[-1])
          g_list.append(g_list[-1])
          t_list.append(t_list[-1])
          S_list.append(S_list[-1]+1)
      if bwt[i] == 'A':
          a_list.append(a_list[-1]+1)
          c_list.append(c_list[-1])
          g_list.append(g_list[-1])
          t_list.append(t_list[-1])
          S_list.append(S_list[-1])
      if bwt[i] == 'C':
          a_list.append(a_list[-1])
          c_list.append(c_list[-1]+1)
          g_list.append(g_list[-1])
          t_list.append(t_list[-1])
          S_list.append(S_list[-1])
      if bwt[i] == 'G':
          a_list.append(a_list[-1])
          c_list.append(c_list[-1])
          g_list.append(g_list[-1]+1)
          t_list.append(t_list[-1])
          S_list.append(S_list[-1])
      if bwt[i] == 'T':
          a_list.append(a_list[-1])
          c_list.append(c_list[-1])
          g_list.append(g_list[-1])
          t_list.append(t_list[-1]+1)
          S_list.append(S_list[-1])

  occ_counts_before['$'] = S_list
  occ_counts_before['A'] = a_list
  occ_counts_before['C'] = c_list
  occ_counts_before['G'] = g_list
  occ_counts_before['T'] = t_list
  #print(starts)
  #print(occ_counts_before)

  return starts, occ_counts_before


def CountOccurrences(pattern, bwt, starts, occ_counts_before):
  """
  Compute the number of occurrences of string pattern in the text
  given only Burrows-Wheeler Transform bwt of the text and additional
  information we get from the preprocessing stage - starts and occ_counts_before.
  """
  # Implement this function yourself
  top = 0
  bottom = len(bwt) - 1
  cursor = 0
  while top <= bottom:
      if (cursor + 1) <= len(pattern):
          symbol = pattern[-1-cursor]
          #print(symbol)
          if occ_counts_before[symbol][top] != occ_counts_before[symbol][bottom+1]:
              #print('Yes')
              top = starts[symbol] + occ_counts_before[symbol][top]
              #print(top)
              bottom = starts[symbol] + occ_counts_before[symbol][bottom + 1]-1
              #print(bottom)
          else:
              return 0
      else:
          return bottom - top + 1
      #print('Cursor')
      cursor = cursor + 1


if __name__ == '__main__':
  bwt = sys.stdin.readline().strip()
  pattern_count = int(sys.stdin.readline().strip())
  patterns = sys.stdin.readline().strip().split()
  # Preprocess the BWT once to get starts and occ_count_before.
  # For each pattern, we will then use these precomputed values and
  # spend only O(|pattern|) to find all occurrences of the pattern
  # in the text instead of O(|pattern| + |text|).
  starts, occ_counts_before = PreprocessBWT(bwt)
  occurrence_counts = []
  for pattern in patterns:
    occurrence_counts.append(CountOccurrences(pattern, bwt, starts, occ_counts_before))
  print(' '.join(map(str, occurrence_counts)))
