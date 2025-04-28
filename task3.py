import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

# nodes - people
G.add_nodes_from(["Jon", "Arya", "Brandon", "Sansa", "Rickon", "Robb", "Joffrey", "Tomen", "Myrcella"])

# adding arcs width weights
G.add_weighted_edges_from([
    ("Jon", "Arya", 2),
    ("Jon", "Robb", 1),
    ("Jon", "Brandon", 3),
    ("Joffrey", "Myrcella", 2),
    ("Joffrey", "Tomen", 1),
    ("Myrcella", "Tomen", 1),
    ("Arya", "Brandon", 2),
    ("Arya", "Sansa", 2),
    ("Brandon", "Sansa", 1),
    ("Brandon", "Rickon", 3),
    ("Sansa", "Robb", 2),
    ("Joffrey", "Sansa", 3),
    ("Joffrey", "Arya", 5),
])

# visualisation
pos = nx.spring_layout(G, seed=42)
plt.figure(figsize=(10, 8))
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=3000, font_size=10, font_weight='bold')
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title("Social network")
plt.axis('off')
plt.show()

def dijkstra_custom(graph, start):
    visited = set()
    distances = {node: float('inf') for node in graph.nodes}
    previous_nodes = {node: None for node in graph.nodes}
    distances[start] = 0

    while len(visited) < len(graph.nodes):
        # looking for unused node
        current_node = min((node for node in graph.nodes if node not in visited), key=lambda node: distances[node])

        visited.add(current_node)

        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor]['weight']
            if distances[current_node] + weight < distances[neighbor]:
                distances[neighbor] = distances[current_node] + weight
                previous_nodes[neighbor] = current_node

    return distances, previous_nodes

def reconstruct_path(prev, start, end):
    path = []
    node = end
    while node and node != start:
        path.append(node)
        node = prev[node]
    if node:
        path.append(start)
    path.reverse()
    return path

# shortest paths
print("\nShortest paths:")
for source in G.nodes():
    distances, previous_nodes = dijkstra_custom(G, source)
    for target in G.nodes():
        if source != target:
            path = reconstruct_path(previous_nodes, source, target)
            print(f"{source} -> {target}: path = {path}, weight = {distances[target]}")
