from node import *
from utils import * 
import heapq


def A_star_search(node,n,f):
    if (unsolvableLogic(node,n))==False:
        return False

    intended = list(range(1, n*n)) + [0]
    #print(intended)
    h=[]
    explored = []
    expanded= []
    heapq.heapify(h)
    heapq.heappush(h,(node.priority,(node)))
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
        #print(f"length: {len(expanded)}")
        possible_nodes  = find_moves(child_node,n)
        for possible_node in possible_nodes:
            if(isInClosedList(possible_node,expanded)!=True):
                insertNewMove(child_node,f,explored,h,possible_node,n)

#7,3,2,4,5,8,1,6,0
#0,1,3,4,2,5,7,8,6 --spec1st
#1,2,3,0,4,6,7,5,8 -- spec2nd
#1,5,0,7,6,4,2,3,8 --22 moves
#1,2,3,4,5,6,8,7,0 --spec 3rd - unsolvable
# node = Node([1,2,3,4,5,6,8,7,0])


# value = A_star_search(node,3,hamming_distance)

# if value==False:
#     print("Unsolvable puzzle")
    