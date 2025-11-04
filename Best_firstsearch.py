from queue import PriorityQueue

def best_first_search(graph, heuristics, start, goal):
    visited = set()
    pq = PriorityQueue()
    pq.put((heuristics[start], start))  # (heuristic, node)
    
    while not pq.empty():
        (h, current) = pq.get()
        print(current, end=" ")

        if current == goal:
            print("\nGoal reached!")
            return

        visited.add(current)

        for neighbor in graph[current]:
            if neighbor not in visited:
                pq.put((heuristics[neighbor], neighbor))

# Example Graph (Adjacency List)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Example Heuristic Values (lower = closer to goal)
heuristics = {
    'A': 6,
    'B': 4,
    'C': 5,
    'D': 2,
    'E': 1,
    'F': 0
}

# Run Best First Search
print("Best First Search Path:")
best_first_search(graph, heuristics, 'A', 'F')
