# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]

def is_balanced(text):
    stack = []
    for char in list(enumerate(text)):
        if char[1] not in ['(','[','{',')',']','}']:
            continue
        if char[1] in ['(','[','{']:
            stack.append(char)
        else:
            if len(stack) == 0:
                return char[0]+1
            top = stack.pop(len(stack)-1)
            if (top[1] == '[' and char[1] != ']') or (top[1] == '(' and char[1] != ')') or (top[1] == '{' and char[1] != '}'):
               return char[0]+1
        #print(stack)
    if len(stack) == 0:
        return 'Success'
    else: return stack[0][0]+1

def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            pass

        if next in ")]}":
            # Process closing bracket, write your code here
            pass


def main():
    text = list(input())
    #mismatch = find_mismatch(text)
    print(is_balanced(text))
    # Printing answer, write your code here


if __name__ == "__main__":
    main()
