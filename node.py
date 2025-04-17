import math
import numpy as np # type: ignore

def ceildiv(a, b):
    return -(a // -b)

class Node:
    def __init__(self,arr):
        self.initial_config = arr
        self.moves = 0
        self.parent = None
        self.priority = 0 + manhattan_distance(self,3)
    def __lt__(self, other):
        return self.priority < other.priority

def hamming_distance(node,n):
    distance = 0
    for i in range(n*n):
        if node.initial_config[i]!= i+1:
            distance += 1
    return distance
def manhattan_distance(node,n):
    distance = 0
    for i in range(n*n):
        if node.initial_config[i]!= i+1:
            x1 = i//n
            y1 = i%n
            x2 = (node.initial_config[i]-1)//n
            y2 = (node.initial_config[i]-1)%n
            distance += abs(x1-x2) + abs(y1-y2)
    return distance

def euclidean_distance(node,n):
    distance = 0
    for i in range(n*n):
        if node.initial_config[i]!= i+1:
            x1 = i//3
            y1 = i%3
            x2 = (node.initial_config[i]-1)//n
            y2 = (node.initial_config[i]-1)%n
            distance += math.sqrt((x1-x2)**2 + (y1-y2)**2)
    return distance

def linear_conflict(node,n):
    row_conflict = 0
    col_conflict = 0
    #row conflict
    rows = []
    for i in range(n):
        rows.append(node.initial_config[i*3:(i+1)*3])
    #print("rows: ")
    print(rows)
    
    for i,row in enumerate(rows):
        #print(f"row no.: {i} here: ")
        print(row)
        for j in range(len(row)):
            for k in range(j+1,len(row)):
                #print(f"row items:  { row[j] } and {row[k]}")
                print(f"{ceildiv(row[j],n)-1} {ceildiv(row[k],n)-1} {i}")
                if (i==ceildiv(row[j],n)-1 and i==ceildiv(row[k],n)-1 and row[j]>row[k] and row[j]!=0 and row[k]!=0):
                    #print(f"{row[j]},{ row[k] }  row conflict" )
                    row_conflict += 1

    #columns
    r = np.array(rows)
    cols = np.hsplit(r,n)
    for i,col in enumerate(cols):
        for j in range(len(cols)):
            for k in range(j+1,len(cols)):
                if ((col[j]-1)%n==i and (col[k]-1)%n==i and col[j]>col[k] and col[j]!=0 and col[k]!=0):
                    #print(f"{col[j]}  ,  {col[k]}  column conflict" )
                    col_conflict += 1
    return row_conflict + col_conflict + manhattan_distance(node,n)

# arr = [4,2,3,1,5,6,7,8,0]
# node = Node(arr)
# linear_conflict(node,3)