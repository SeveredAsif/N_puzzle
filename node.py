from utils import * 

class Node:
    def __init__(self,arr):
        self.initial_config = arr
        self.moves = 0
        self.parent = None
        self.priority = 0 + manhattan_distance(self,3)
    def __lt__(self, other):
        return self.priority < other.priority