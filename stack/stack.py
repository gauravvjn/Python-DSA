# Unlimited capacity/length/size of the stack
class Stack:

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return "Stack Is Empty"
        return self.stack.pop()

    def peek(self):
        return self.stack[len(self.stack) - 1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


# Limited capacity, without maintaining a pointer to last(top) element
class Stack:

    def __init__(self, capacity):
        self.stack = []
        self.capacity = capacity   # This will maintain the size/length of the Stack

    def push(self, item):
        if self.size() >= self.capacity:
            return "Stack Is Full"
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return "Stack Is Empty"
        return self.stack.pop()

    def peek(self):
        return self.stack[len(self.stack) - 1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


# Limited capacity, with maintaining a pointer to last(top) element
class Stack:

    def __init__(self, capacity):
        self.stack = []
        self.capacity = capacity
        self.top = -1  # This will have a pointer to the last/most_recent element.

    def push(self, data):
        if self.size() >= self.capacity:
            return "Stack Is Full"
        self.stack.append(data)
        self.top += 1

    def pop(self):
        if self.is_empty():
            return "Stack Is Empty"
        self.top -= 1
        return self.stack.pop()

    def peek(self):
        return self.stack[self.top]

    def is_empty(self):
        return self.top < 0

    def size(self):
        return self.top + 1

    def top_element(self):
        return self.stack[self.top]  # self.stack[-1]

"""
s = Stack() # Or s = Stack(capacity=10)

print(s.is_empty())
print(s.size())
s.push('cat')
s.push('dog')
s.push('cow')
print(s.is_empty())
print(s.size())
print(s.peek())
print(s.pop())
print(s.pop())
print(s.size())
print(s.peek())
"""
