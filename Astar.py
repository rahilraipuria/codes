import heapq

class Graph:
    def __init__(self, adjacency_matrix):
        self.graph = adjacency_matrix
        self.n = len(adjacency_matrix)

    def a_star_search(self, start, goal, heuristic):
        pq = []  # Priority queue (min-heap)
        heapq.heappush(pq, (heuristic[start], 0, start, [start]))  # (f(n), g(n), node, path)
        g_costs = {start: 0}  # Dictionary to store the g(n) cost

        while pq:
            f_n, g_n, node, path = heapq.heappop(pq)

            # If goal is reached, return the path
            if node == goal:
                print(f"\nPath to {goal} using A* Search: {' -> '.join(map(str, path))}")
                print(f"Total cost: {g_n}")
                return path

            # Explore neighbors
            for neighbor in range(self.n):
                if self.graph[node][neighbor] > 0:  # There's an edge (positive weight)
                    edge_cost = self.graph[node][neighbor]
                    new_g_n = g_n + edge_cost  # g(n) for the neighbor
                    f_n = new_g_n + heuristic[neighbor]  # f(n) = g(n) + h(n)

                    if neighbor not in g_costs or new_g_n < g_costs[neighbor]:
                        g_costs[neighbor] = new_g_n
                        heapq.heappush(pq, (f_n, new_g_n, neighbor, path + [neighbor]))

        print(f"\nNode {goal} not found in the graph.")
        return None


def main():
    n = int(input("Enter the number of nodes: "))
    print("Enter the adjacency matrix (space-separated numbers, use 0 for no edge):")
    adjacency_matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        adjacency_matrix.append(row)

    g = Graph(adjacency_matrix)

    start_node = int(input("Enter the starting node for the search: "))
    goal_node = int(input("Enter the goal node to search for: "))

    # Input heuristic values for each node
    print("Enter the heuristic values for each node:")
    heuristic = {}
    for node in range(n):
        heuristic[node] = int(input(f"Heuristic for node {node}: "))

    print(f"\nA* Search starting from node {start_node} to find node {goal_node}:")
    g.a_star_search(start_node, goal_node, heuristic)


if __name__ == "__main__":
    main()
