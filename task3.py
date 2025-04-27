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

# Dijkstra path
shortest_paths = dict(nx.all_pairs_dijkstra_path(G))
shortest_distances = dict(nx.all_pairs_dijkstra_path_length(G))

# shortest paths
print("\nShortest paths:")
for source in G.nodes():
    for target in G.nodes():
        if source != target:
            print(f"{source} -> {target}: path = {shortest_paths[source][target]}, weight = {shortest_distances[source][target]}")
