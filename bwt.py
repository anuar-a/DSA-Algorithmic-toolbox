# python3
import sys

def BWT(text):
    result = []
    ans = str()
    for i in range(len(text)):
        result.append(text[i:] + text[0:i])
    result.sort()
    for i in range(len(text)):
        ans = ans + str(result[i][-1])
    return ans

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(BWT(text))
