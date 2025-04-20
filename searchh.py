from node import *
from utils import * 
import heapq
import time

def A_star_search(node, n, f):
    if unsolvableLogic(node, n) == False:
        return False

    intended = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    h = []
    explored = []
    expanded = []
    heapq.heapify(h)
    heapq.heappush(h, (node.priority, node))
    
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    log_filename = f"Asifdebug_log_{timestamp}.txt"
    
    def state_to_2d_str(state, n):
        return "\n".join([" ".join(map(str, state[i*n:(i+1)*n])) for i in range(n)])

    with open(log_filename, 'w', encoding='utf-8') as log_file:
        log_file.write("==== A* Search Debug Log ====\n")
        log_file.write(f"Heuristic: {f.__name__}\n")
        log_file.write(f"Start State:\n{state_to_2d_str(node.initial_config, n)}\n\n")
        
        while len(h):
            # Log current state of the heap
            log_file.write(f"\nHeap size: {len(h)}")
            log_file.write(f"\nCurrent heap priorities: {[item[0] for item in h]}\n")
            
            child_node = heapq.heappop(h)[1]
            current_state = child_node.initial_config
            
            log_file.write("\n" + "="*40 + "\n")
            log_file.write(f"EXPANDING NODE (g={child_node.moves}, h={child_node.priority - child_node.moves}):\n")
            log_file.write(state_to_2d_str(current_state, n) + "\n")
            
            if np.array_equal(intended, current_state):
                log_file.write("\n!!! GOAL FOUND !!!\n")
                print(f"Minimum number of moves: {child_node.moves}")
                print(f"Expanded: {len(expanded)}")
                print(f"Explored: {len(explored)}")
                return True

            # Add to expanded and log
            expanded.append(child_node)
            log_file.write(f"\n--- Expanded List (Total: {len(expanded)}) ---")
            for idx, ex_node in enumerate(expanded, 1):
                log_file.write(f"\nExpanded Node #{idx} (g={ex_node.moves}, h={ex_node.priority - ex_node.moves}):\n")
                log_file.write(state_to_2d_str(ex_node.initial_config, n) + "\n")

            possible_nodes = find_moves(child_node, n)
            log_file.write(f"\nGenerated {len(possible_nodes)} children:")
            
            for possible_node in possible_nodes:
                log_file.write("\n" + "-"*30)
                log_file.write("\nChild State:\n" + state_to_2d_str(possible_node, n))
                
                if isInClosedList(possible_node, expanded):
                    log_file.write("\n[Already in expanded, SKIPPING]")
                    continue
                if isInClosedList(possible_node, explored):
                    log_file.write("\n[Already in explored, SKIPPING]")
                    continue
                
                # Create new node
                new_node = Node(possible_node)
                new_node.moves = child_node.moves + 1
                new_node.parent = child_node
                new_node.priority = new_node.moves + f(new_node, n)
                
                log_file.write(f"\nNew priority: {new_node.priority} (g={new_node.moves}, h={f(new_node, n)})")
                
                # Check if in heap
                in_heap = any(np.array_equal(item[1].initial_config, possible_node) for item in h)
                if not in_heap:
                    heapq.heappush(h, (new_node.priority, new_node))
                    explored.append(new_node)
                    log_file.write("\n[Added to heap]")
                else:
                    log_file.write("\n[Already in heap]")

            log_file.write("\n" + "="*40 + "\n")
            
        log_file.write("\nHeap is empty. No solution found.\n")
    return False

# Rest of your test code remains the same...


#7,3,2,4,5,8,1,6,0
#0,1,3,4,2,5,7,8,6
#1,2,3,0,4,6,7,5,8
#1,5,0,7,6,4,2,3,8
node = Node([1,5,0,7,6,4,2,3,8])


value = A_star_search(node,3,hamming_distance)

if value==False:
    print("Unsolvable puzzle")