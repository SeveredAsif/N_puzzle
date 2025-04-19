class Node:
    def __init__(self,arr):
        self.initial_config = arr
        self.moves = 0
        self.parent = None
        self.priority = 0 
    def __lt__(self, other):
        return self.priority < other.priority