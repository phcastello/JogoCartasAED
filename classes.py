class Player:
    def __init__(self, name: str):
        self.name = name
        self.score = 0

    def add_point(self, cardNumber):
        self.score += cardNumber

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from empty stack")

    def is_empty(self):
        return len(self.items) == 0
    
    def show_top(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("show_top from empty stack")

