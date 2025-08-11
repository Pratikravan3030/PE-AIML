from collections import deque

MAX = 100
graph = [[0] * MAX for _ in range(MAX)]
visited = [False] * MAX

def BFS(start, V):
    q = deque()
    visited[start] = True
    q.append(start)

    while q:
        node = q.popleft()
        print(node + 1, end=" ")

        for i in range(V):
            if graph[node][i] == 1 and not visited[i]:
                visited[i] = True
                q.append(i)

def main():
    V = int(input("Enter number of vertices: "))
    E = int(input("Enter number of edges: "))

    # Initialize visited & graph
    for i in range(V):
        visited[i] = False
        for j in range(V):
            graph[i][j] = 0

    print("Enter edges in (u v) format:")
    for _ in range(E):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        graph[u][v] = 1
        graph[v][u] = 1

    start = int(input("Enter start node: ")) - 1
    print("BFS traversal:", end=" ")
    BFS(start, V)
    print()

if __name__ == "__main__":
    main()
