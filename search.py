from node import *

node = Node([1,2,3,4,0,5,6,7,8])

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
    # for i,val in enumerate(node.initial_config):
    #     if val==0:
    #         row = i//n 
    #         col = i%n
    #         zero_pos = i
    #         #print(zero_pos)
    #         break
    row,col,zero_pos = find_zero(node,n)
    
    poss_moves = [[row-1,col],[row+1,col],[row,col-1],[row,col+1]]
    #print(poss_moves)
    for poss_move in poss_moves:
        duplicate_arr = arr[:]
        if (poss_move[0]<n and poss_move[1]<n and poss_move[0]>-1 and poss_move[1]>-1):
            temp = arr[poss_move[0]*n+poss_move[1]]
            duplicate_arr[zero_pos] = temp
            duplicate_arr[poss_move[0]*n+poss_move[1]] = 0
            ans.append(duplicate_arr)
    return ans


import heapq


def A_star_search(node,n):
    inversions= find_inversions(node)
    if (n%2!=0 and inversions%2 != 0):
        return False
    row,col,zero_pos = find_zero(node,n)
    col_from_bottom = n - col
    if(n%2 == 0 and inversions%2 == 0): 
        if(col_from_bottom%2==0):
            return False
    if(n%2== 0 and inversions%2!=0):
        if(col_from_bottom%2!=0):
            return False

    intended = [1,2,3,4,5,6,7,8,0]
    h=[]
    explored = []
    expanded= []
    heapq.heapify(h)
    heapq.heappush(h,(node.priority,(node)))
    explored.append(node)
    # expanded closed_list = []
    while (len(h)):
        child_node = heapq.heappop(h)[1]
        #print(nodee)
        #print_node(child_node,n)
        if(np.array_equal(intended,child_node.initial_config)):
            print(f"Minimum number of moves: {child_node.moves}")
            print(f"Expanded: {len(expanded)}")
            print(f"Explored: {len(explored)}")
            printing_node = []
            while(child_node!=None):
                printing_node.append(child_node)
                child_node = child_node.parent
            printing_node.reverse()
            for nodes in printing_node:
                print_node(nodes,n)
            return True
        expanded.append(child_node)
        # print(nodee[1].initial_config)
        possible_nodes  = find_moves(child_node,n)
        #print(possible_nodes)
        for possible_node in possible_nodes:
            moves = child_node.moves + 1
            new_node = Node(possible_node)
            new_node.moves = moves
            new_node.parent = child_node
            new_node.priority = moves + linear_conflict(new_node,n)
            explored.append(new_node)
            # print_node(new_node,n)
            heapq.heappush(h,(new_node.priority,new_node))


node = Node([1,2,3,4,5,6,8,7,0])

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


value = A_star_search(node,3)
if value==False:
    print("Unsolvable puzzle")
    