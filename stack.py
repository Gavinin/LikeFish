class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return self.stack == []

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[len(self.stack) - 1]

    def size(self):
        return len(self.stack)

    def push(self, obj):
        self.stack.append(obj)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()
