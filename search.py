from node import *

node = Node([1,2,3,4,0,5,6,7,8])

def find_moves(node,n):
    arr = node.initial_config
    row = 0
    col = 0
    zero_pos = 0
    for i,val in enumerate(node.initial_config):
        if val==0:
            row = i//n 
            col = i%n
            zero_pos = i
            break
    
    poss_moves = [[row-1,col],[row+1,col],[row,col-1],[row,col+1]]
    for poss_move in poss_moves:
        duplicate_arr = arr[:]
        if (poss_move[0]<n and poss_move[1]<n):
            temp = arr[poss_move[0]*n+poss_move[1]]
            duplicate_arr[zero_pos] = temp
            duplicate_arr[poss_move[0]*n+poss_move[1]] = 0
            print(duplicate_arr)

find_moves(node,3)


    