import networkx as nx
import matplotlib.pyplot as plt

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