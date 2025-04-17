from node import *
from utils import * 
import heapq


def A_star_search(node,n,f):
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
    while (len(h)):
        child_node = heapq.heappop(h)[1]
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
        possible_nodes  = find_moves(child_node,n)
        for possible_node in possible_nodes:
            moves = child_node.moves + 1
            new_node = Node(possible_node)
            new_node.moves = moves
            new_node.parent = child_node
            new_node.priority = moves + f(new_node,n)
            explored.append(new_node)
            heapq.heappush(h,(new_node.priority,new_node))


node = Node([1,2,3,0,4,6,7,5,8])


value = A_star_search(node,3,linear_conflict)
if value==False:
    print("Unsolvable puzzle")
    