class Graph:
    def __init__(self, adjacency_matrix):
        self.graph = adjacency_matrix
        self.n = len(adjacency_matrix)  # Number of nodes

    def iterative_deepening_search(self, start, goal):
        depth = 0
        while True:
            print(f"\nSearching with depth limit {depth}:")
            found_path = self.depth_limited_search(start, goal, depth)
            if found_path:
                print(f"\nPath to {goal}: {' -> '.join(map(str, found_path))}")
                return found_path
            depth += 1

    def depth_limited_search(self, start, goal, max_depth):
        visited = set()
        path = []
        return self._dfs_helper(start, goal, visited, path, 0, max_depth)

    def _dfs_helper(self, node, goal, visited, path, current_depth, max_depth):
        if current_depth > max_depth:
            return None
        visited.add(node)
        path.append(node)
        if node == goal:
            return path.copy()
        for neighbor in range(self.n):
            if self.graph[node][neighbor] == 1 and neighbor not in visited:
                found_path = self._dfs_helper(
                    neighbor, goal, visited, path, current_depth + 1, max_depth
                )
                if found_path:
                    return found_path
        path.pop()
        return None


def main():
    n = int(input("Enter the number of nodes: "))
    print("Enter the adjacency matrix (0/1 format, space-separated):")
    adjacency_matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        adjacency_matrix.append(row)

    g = Graph(adjacency_matrix)

    start_node = int(input("Enter the starting node for the search: "))
    goal_node = int(input("Enter the goal node to search for: "))

    print(f"Iterative Deepening Search starting from node {start_node} to find node {goal_node}:")
    g.iterative_deepening_search(start_node, goal_node)


if __name__ == "__main__":
    main()
