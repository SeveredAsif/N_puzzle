import search
import node
import utils


print("Choose one of the following heuristics for A* search:")
print("1. Hamming distance")
print("2. Manhattan distance")
print("3. Euclidean distance")
print("4. Linear conflict (Manhattan + linear conflicts)")
choice = input("Enter 1, 2, 3 or 4: ")


def select_heuristic(option):
    if option == '1':
        return utils.hamming_distance
    elif option == '2':
        return utils.manhattan_distance
    elif option == '3':
        return utils.euclidean_distance
    elif option == '4':
        return utils.linear_conflict
    else:
        print("Invalid choice; defaulting to Manhattan distance.")
        return utils.manhattan_distance

heuristic_fn = select_heuristic(choice)


n = int(input())
grid = []

for _ in range(n):
    row = list(map(int, input().split()))
    grid.extend(row)

start_node = node.Node(grid)
result = search.A_star_search(start_node, n, heuristic_fn)
if not result:
    print("Unsolvable puzzle")
