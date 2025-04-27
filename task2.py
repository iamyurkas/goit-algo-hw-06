import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

G = nx.Graph()

# nodes - people
G.add_nodes_from(["Jon", "Arya", "Brandon", "Sansa", "Rickon", "Robb", "Joffrey", "Tomen", "Myrcella"])

# adding arcs
G.add_edges_from([
    ("Jon", "Arya"),
    ("Jon", "Robb"),
    ("Jon", "Brandon"),
    ("Joffrey", "Myrcella"),
    ("Joffrey", "Tomen"),
    ("Myrcella", "Tomen"),
    ("Arya", "Brandon"),
    ("Arya", "Sansa"),
    ("Brandon", "Sansa"),
    ("Brandon", "Rickon"),
    ("Brandon", "Sansa"),
    ("Sansa", "Robb"),
    ("Joffrey", "Sansa"),
    ("Joffrey", "Arya"),
])

# visualisation
plt.figure(figsize=(10, 8))
nx.draw_networkx(G, with_labels=True, node_color='skyblue', node_size=3000, font_size=10, font_weight='bold')
plt.title("Social network")
plt.axis('off')
plt.show()

# graph characteristics
print("Main characteristics of the graph:")
print(f"- Nodes number: {G.number_of_nodes()}")
print(f"- Arcs number: {G.number_of_edges()}")

# node degree
print("\nThe degree of each node in the graph:")
for node, degree in G.degree():
    print(f"- {node}: {degree}")

# DFS path
def dfs_path(graph, start, goal, path=None, visited=None):
    if path is None:
        path = []
    if visited is None:
        visited = set()
    path = path + [start]
    visited.add(start)
    if start == goal:
        return path
    for neighbor in graph.neighbors(start):
        if neighbor not in visited:
            new_path = dfs_path(graph, neighbor, goal, path, visited)
            if new_path:
                return new_path
    return None

# BFS path
def bfs_path(graph, start, goal):
    queue = deque([(start, [start])])
    visited = set()
    while queue:
        (vertex, path) = queue.popleft()
        if vertex == goal:
            return path
        visited.add(vertex)
        for neighbor in graph.neighbors(vertex):
            if neighbor not in visited and neighbor not in (p[0] for p in queue):
                queue.append((neighbor, path + [neighbor]))
    return None

# path
start_node = "Jon"
goal_node = "Myrcella"

print(f"\nDFS path from {start_node} to {goal_node}: {dfs_path(G, start_node, goal_node)}")
print(f"BFS path from {start_node} to {goal_node}: {bfs_path(G, start_node, goal_node)}")
