import math
import numpy as np # type: ignore

def ceildiv(a, b):
    return -(a // -b)

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
    #print(rows)
    
    for i,row in enumerate(rows):
        #print(row)
        for j in range(len(row)):
            for k in range(j+1,len(row)):
                if (i==ceildiv(row[j],n)-1 and i==ceildiv(row[k],n)-1 and row[j]>row[k] and row[j]!=0 and row[k]!=0):
                    row_conflict += 1

    #columns
    r = np.array(rows)
    cols = np.hsplit(r,n)
    for i,col in enumerate(cols):
        for j in range(len(cols)):
            for k in range(j+1,len(cols)):
                if ((col[j]-1)%n==i and (col[k]-1)%n==i and col[j]>col[k] and col[j]!=0 and col[k]!=0):
                    col_conflict += 1
    return row_conflict + col_conflict + manhattan_distance(node,n)


def find_zero(node,n):
    for i,val in enumerate(node.initial_config):
        if val==0:
            row = i//n 
            col = i%n
            zero_pos = i
            #print(zero_pos)
            return row,col,zero_pos
        

def find_moves(node,n):
    ans = []
    arr = node.initial_config
    #print(arr)
    row = 0
    col = 0
    zero_pos = 0
    row,col,zero_pos = find_zero(node,n)
    
    poss_moves = [[row-1,col],[row+1,col],[row,col-1],[row,col+1]]
    for poss_move in poss_moves:
        duplicate_arr = arr[:]
        if (poss_move[0]<n and poss_move[1]<n and poss_move[0]>-1 and poss_move[1]>-1):
            temp = arr[poss_move[0]*n+poss_move[1]]
            duplicate_arr[zero_pos] = temp
            duplicate_arr[poss_move[0]*n+poss_move[1]] = 0
            ans.append(duplicate_arr)
    return ans


def find_inversions(node):
    count = 0
    arr = node.initial_config
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if(arr[i]>arr[j] and arr[j]!=0):
                count += 1
    return count


def print_node(node,n):
    # arr = np.array(node.initial_config)
    # arr = np.split(arr,n,axis=0)
    arr = np.array(node.initial_config).reshape(n, n)
    print(arr)
    print()
    print()