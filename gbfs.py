import heapq

def greedy_best_first_search(graph, start, goal, heuristic):
    # Priority queue (min-heap)
    open_list = []
    heapq.heappush(open_list, (heuristic[start], start))

    # Visited set to track explored nodes
    visited = set()

    print("Path Traversal:")
    while open_list:
        # Select the node with the smallest heuristic value
        _, current = heapq.heappop(open_list)

        print(f"Visiting node: {current}")

        if current == goal:
            print("Goal reached!")
            return

        if current in visited:
            continue

        visited.add(current)

        # Explore neighbors
        for neighbor, cost in enumerate(graph[current]):
            if cost > 0 and neighbor not in visited:
                heapq.heappush(open_list, (heuristic[neighbor], neighbor))

    print("Goal not reachable from the start node.")

def main():
    # Input graph as adjacency matrix
    n = int(input("Enter the number of nodes: "))
    print("Enter the adjacency matrix (rows of 1s and 0s):")
    graph = [list(map(int, input().split())) for _ in range(n)]

    print("Enter the heuristic values for each node:")
    heuristic = list(map(int, input().split()))

    start = int(input("Enter the starting node (0-indexed): "))
    goal = int(input("Enter the goal node (0-indexed): "))

    greedy_best_first_search(graph, start, goal, heuristic)

if __name__ == "__main__":
    main()
