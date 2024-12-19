def is_safe(graph, color, vertex, c):
    for i in range(len(graph)):
        if graph[vertex][i] == 1 and color[i] == c:
            return False
    return True


def graph_coloring_util(graph, m, color, vertex):
    if vertex == len(graph):
        return True

    for c in range(m):
        if is_safe(graph, color, vertex, c):
            color[vertex] = c
            if graph_coloring_util(graph, m, color, vertex + 1):
                return True
            color[vertex] = -1  # Backtrack if no solution is found for this color

    return False


def graph_coloring(graph, m):
    n = len(graph)
    color = [-1] * n  # Initialize color array with -1 (no color)

    if not graph_coloring_util(graph, m, color, 0):
        print("Solution does not exist")
        return None

    return color


def input_graph():
    n = int(input("Enter the number of vertices: "))
    graph = [[0] * n for _ in range(n)]
    e = int(input("Enter the number of edges: "))
    print("Enter the edges (u, v) where u and v are 0-indexed:")
    for _ in range(e):
        u, v = map(int, input().split())
        graph[u][v] = 1
        graph[v][u] = 1  # Since it's an undirected graph
    return graph, n


def main():
    graph, n = input_graph()
    m = int(input(f"Enter the number of colors to use (maximum {n}): "))
    color = graph_coloring(graph, m)

    if color:
        print("\nVertex coloring result:")
        for i in range(n):
            print(f"Vertex {i} -> Color {color[i]}")


if __name__ == "__main__":
    main()
