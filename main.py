def longest_path(graph: list) -> int:
    n = len(graph)
    topo_order = topological_sort(graph, n)
    return calculate_longest_path(graph, topo_order, n)

# Helper function to perform topological sort
def topological_sort(graph, n):
    v = [False] * n
    stack = []
    
    def dfs(node):
        v[node] = True
        for neighbor, _ in graph[node]:
            if not v[neighbor]:
                dfs(neighbor)
        stack.append(node)
    
    for i in range(n):
        if not v[i]:
            dfs(i)
    
    return stack[::-1]

# Function to calculate longest path using topological sort
def calculate_longest_path(graph, topo_order, n):
    dist = [-float('inf')] * n

    for node in topo_order:
        if dist[node] == -float('inf'):
            dist[node] = 0

        for neighbor, weight in graph[node]:
            if dist[neighbor] < dist[node] + weight:
                dist[neighbor] = dist[node] + weight

    return max(dist)

# Example usage
#if __name__ == "__main__":
#    graph = [
#        [(1, 3), (2, 2)],
#        [(3, 4)],
#        [(3, 1)],
#        []
#    ]
#    print(longest_path(graph))  # Output: 7

