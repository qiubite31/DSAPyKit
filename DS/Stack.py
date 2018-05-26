class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        self.stack.pop()

    def __str__(self):
        return str(self.stack) + ' <-Enter'

stack = Stack()
print(stack)
stack.push(2)
print(stack)
stack.push(3)
print(stack)
stack.pop()
print(stack)
stack.push(4)
print(stack)
stack.push(5)
print(stack)