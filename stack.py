class Stack:
    def __init__(self, ) -> None:
        self.stack = []

    def pop(self):
        if not self.is_empty():
            print(self.stack.pop())
        else:
            print("Stack is empty")

    def push(self, item):
        self.stack.append(item)
        print(item, "pushed to stack")

    def peek(self):
        if not self.is_empty():
            print(self.stack[-1])

    def is_empty(self):
        return len(self.stack)==0

    def check_stack(self):
        print(self.stack)

stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.check_stack()

stack.peek()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
