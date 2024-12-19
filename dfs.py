def dfs(graph, visited, vertex):
    print(f"Visiting vertex: {vertex}")
    visited[vertex] = True

    for neighbor, is_connected in enumerate(graph[vertex]):
        if is_connected and not visited[neighbor]:
            dfs(graph, visited, neighbor)

def main():
    # Input graph as adjacency matrix
    n = int(input("Enter the number of vertices: "))
    print("Enter the adjacency matrix (rows of 1s and 0s):")
    graph = [list(map(int, input().split())) for _ in range(n)]

    # Initialize visited list
    visited = [False] * n

    # Perform DFS starting from vertex 0
    start_vertex = int(input("Enter the starting vertex (0-indexed): "))
    print("\nDFS Traversal:")
    dfs(graph, visited, start_vertex)

if __name__ == "__main__":
    main()
