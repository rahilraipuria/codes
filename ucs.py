import heapq

class Graph:
    def __init__(self, adjacency_matrix):
        self.graph = adjacency_matrix
        self.n = len(adjacency_matrix)

    def uniform_cost_search(self, start, goal):
        pq = []  # Priority queue to store (cost, node, path)
        heapq.heappush(pq, (0, start, [start]))
        visited = {}  # Dictionary to store the minimum cost to each node

        while pq:
            current_cost, node, path = heapq.heappop(pq)

            # Skip if we've already found a cheaper way to this node
            if node in visited and visited[node] <= current_cost:
                continue

            visited[node] = current_cost

            # Check if we've reached the goal
            if node == goal:
                print(f"\nPath to {goal} with total cost {current_cost}: {' -> '.join(map(str, path))}")
                return path

            # Explore neighbors
            for neighbor in range(self.n):
                if self.graph[node][neighbor] > 0:  # There's an edge with a positive weight
                    new_cost = current_cost + self.graph[node][neighbor]  # Use the actual edge cost
                    heapq.heappush(pq, (new_cost, neighbor, path + [neighbor]))

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
    print(f"\nUniform Cost Search starting from node {start_node} to find node {goal_node}:")
    g.uniform_cost_search(start_node, goal_node)

if __name__ == "__main__":
    main()
