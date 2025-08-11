MAX = 100
graph = [[0] * MAX for _ in range(MAX)]
visited = [False] * MAX

def DFS(node, V):
    visited[node] = True
    print(node + 1, end=" ")

    for i in range(V):
        if graph[node][i] == 1 and not visited[i]:
            DFS(i, V)

# Main
V = int(input("Enter number of vertices: "))
E = int(input("Enter number of edges: "))

# Reset graph and visited arrays
for i in range(V):
    visited[i] = False
    for j in range(V):
        graph[i][j] = 0

print("Enter edges in (u, v) format:")
for _ in range(E):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u][v] = 1
    graph[v][u] = 1

start = int(input("Enter start node: "))
start -= 1

print("DFS traversal:", end=" ")
DFS(start, V)
print()
