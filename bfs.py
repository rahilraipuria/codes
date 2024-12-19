from collections import deque

def bfs(graph, start_vertex):
    n = len(graph)
    visited = [False] * n
    queue = deque([start_vertex])
    visited[start_vertex] = True

    print("BFS Traversal:")
    while queue:
        vertex = queue.popleft()
        print(f"Visiting vertex: {vertex}")

        for neighbor, is_connected in enumerate(graph[vertex]):
            if is_connected and not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True

def main():
    # Input graph as adjacency matrix
    n = int(input("Enter the number of vertices: "))
    print("Enter the adjacency matrix (rows of 1s and 0s):")
    graph = [list(map(int, input().split())) for _ in range(n)]

    # Perform BFS starting from a given vertex
    start_vertex = int(input("Enter the starting vertex (0-indexed): "))
    bfs(graph, start_vertex)

if __name__ == "__main__":
    main()
