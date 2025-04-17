from node import *

node = Node([1,2,3,4,0,5,6,7,8])

def find_moves(node,n):
    ans = []
    arr = node.initial_config
    #print(arr)
    row = 0
    col = 0
    zero_pos = 0
    for i,val in enumerate(node.initial_config):
        if val==0:
            row = i//n 
            col = i%n
            zero_pos = i
            #print(zero_pos)
            break
    
    poss_moves = [[row-1,col],[row+1,col],[row,col-1],[row,col+1]]
    #print(poss_moves)
    for poss_move in poss_moves:
        duplicate_arr = arr[:]
        if (poss_move[0]<n and poss_move[1]<n and poss_move[0]>-1 and poss_move[1]>-1):
            temp = arr[poss_move[0]*n+poss_move[1]]
            duplicate_arr[zero_pos] = temp
            duplicate_arr[poss_move[0]*n+poss_move[1]] = 0
            ans.append(duplicate_arr)
            #print(duplicate_arr)
    return ans

#find_moves(node,3)

# from queue import PriorityQueue

import heapq
# h=[]
# heapq.heapify(h)
# heapq.heappush(h,(3,("Asif")))
# heapq.heappush(h,(1,("Ahnaf")))
# heapq.heappush(h,(2,("Anindita")))


#print(heapq.heappop(h))

def A_star_search(node,n):
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
        print_node(child_node,n)
        if(np.array_equal(intended,child_node.initial_config)):
            print(f"Minimum number of moves: {child_node.moves}")
            print(f"Expanded: {len(expanded)}")
            print(f"Explored: {len(explored)}")
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
            new_node.priority = moves + manhattan_distance(new_node,n)
            explored.append(new_node)
            # print_node(new_node,n)
            heapq.heappush(h,(new_node.priority,new_node))


node = Node([0,1,3,4,2,5,7,8,6])

def print_node(node,n):
    # arr = np.array(node.initial_config)
    # arr = np.split(arr,n,axis=0)
    arr = np.array(node.initial_config).reshape(n, n)
    print(arr)
    print()
    print()


A_star_search(node,3)
    