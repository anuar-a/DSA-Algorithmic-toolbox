#python3
import sys

class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.stack = []

    def Push(self, a):
        self.__stack.append(a)
        if len(self.stack) == 0:
            self.stack.append(a)
        if a >= self.stack[-1]:
            if a == 0:
                True
            else:
                self.stack.append(a)

    def Pop(self):
        assert(len(self.__stack))
        x = self.__stack.pop()
        if x == self.stack[-1]:
            if x == 0:
                True
            else:
                self.stack.pop()

    def Max(self):
        assert(len(self.__stack))
        #print(self.__stack)
        #print(self.stack)
        return self.stack[-1]


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
