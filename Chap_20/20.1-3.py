# Number of vertices
n = 4

# Initialize the graph with empty lists for each vertex
graph = [[] for _ in range(n)]

# Function to add an edge from u to v
def add_edge(graph, u, v):
    graph[u].append(v)

# Add edges to the graph
add_edge(graph, 0, 1)  # Edge from vertex 0 to vertex 1
add_edge(graph, 0, 2)  # Edge from vertex 0 to vertex 2
add_edge(graph, 1, 2)  # Edge from vertex 1 to vertex 2
add_edge(graph, 2, 0)  # Edge from vertex 2 to vertex 0
add_edge(graph, 2, 3)  # Edge from vertex 2 to vertex 3
add_edge(graph, 3, 3)  # Edge from vertex 3 to vertex 3 (loop)

# Function to print the graph
def print_graph(graph):
    for i, neighbors in enumerate(graph):
        print(f"Vertex {i}: {neighbors}")

def reverse_graph(graph):
    reverse_graph = [[] for _ in range(len(graph))]
    for i, neighbors in enumerate(graph):
        for neighbor in neighbors:
            reverse_graph[neighbor].append(i)
    return reverse_graph
print_graph(graph)
reverse_graph = reverse_graph(graph)
print_graph(reverse_graph)

