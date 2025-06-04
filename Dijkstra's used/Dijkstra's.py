# this is just a stand-alone python script to show how dijkstra algorithm was implemented 
# we did not use the heapq library in the micropython we just used math
import sys
import math
import matplotlib.pyplot as plt
from heapq import heappush, heappop

def dijkstra(graph, src, dest):
    inf = sys.maxsize
    node_data = {node: {'cost': inf, 'pred': []} for node in graph}
    node_data[src]['cost'] = 0
    visited = []
    min_heap = [(0, src)]

    while min_heap:
        current_cost, temp = heappop(min_heap)

        if temp in visited:
            continue
        visited.append(temp)

        for neighbor in graph[temp]:
            cost = node_data[temp]['cost'] + graph[temp][neighbor]
            if cost < node_data[neighbor]['cost']:
                node_data[neighbor]['cost'] = cost
                node_data[neighbor]['pred'] = node_data[temp]['pred'] + [temp]
                heappush(min_heap, (cost, neighbor))

    path = node_data[dest]['pred'] + [dest]
    print("Shortest Distance:", node_data[dest]['cost'])
    print("Shortest Path:", " -> ".join(path))
    return path

def draw_graph(graph, pos, shortest_path):
    fig, ax = plt.subplots()

    # Draw all edges and edge weights
    drawn_edges = set()
    for node in graph:
        for neighbor in graph[node]:
            if (neighbor, node) in drawn_edges:
                continue
            x1, y1 = pos[node]
            x2, y2 = pos[neighbor]
            ax.plot([x1, x2], [y1, y2], color='gray', linewidth=1, zorder=1)
            # Draw edge weight at midpoint
            mx, my = (x1 + x2) / 2, (y1 + y2) / 2
            ax.text(mx, my, str(graph[node][neighbor]), fontsize=12, color='blue')
            drawn_edges.add((node, neighbor))

    # Highlight shortest path nodes and edges first
    path_nodes = set(shortest_path)
    for i in range(len(shortest_path)-1):
        n1, n2 = shortest_path[i], shortest_path[i+1]
        x1, y1 = pos[n1]
        x2, y2 = pos[n2]
        ax.plot([x1, x2], [y1, y2], color='red', linewidth=3, zorder=3)

    # Draw all nodes (orange if in path, else lightblue)
    for node, (x, y) in pos.items():
        color = 'orange' if node in path_nodes else 'lightblue'
        ax.scatter(x, y, s=800, color=color, edgecolors='black', zorder=4)

    # Draw node labels last, always in black
    for node, (x, y) in pos.items():
        ax.text(x, y, node, ha='center', va='center', fontsize=8, weight='bold', color='black', zorder=5)

    ax.axis('off')
    plt.tight_layout()
    plt.show()

#Define grid
if __name__ == "__main__":
    graph = {
        'A1': {'A': 0.15},
        'A': {'A1':0.15, 'B': 0.10, 'K': 0.25},
        'B1': {'B': 0.15},
        'B': {'B1':0.15,'A': 0.10, 'C': 0.10},
        'C1': {'C': 0.15},
        'C': {'C1':0.15,'B': 0.10, 'D': 0.10},
        'D1':{'D':0.15},
        'D': {'D1':0.15,'C': 0.10, 'E': 0.20},
        'E': {'D': 0.20, 'F': 0.50, 'G': 0.15},
        'F': {'E': 0.50, 'H': 0.15},
        'G': {'J': 0.10, 'H': 0.50, 'E': 0.15},
        'H': {'I': 0.10, 'G': 0.50, 'F': 0.15},
        'I': {'J': 0.50, 'S': 0.50, 'H': 0.10},
        'J': {'G': 0.10, 'M': 0.10, 'K': 0.50, 'I': 0.50},
        'K': {'A': 0.25, 'L': 0.10, 'J': 0.50},
        'L': {'K': 0.10, 'N': 0.15, 'M': 0.50},
        'M': {'L': 0.25, 'J': 0.10, 'O': 0.15},
        'N': {'O': 0.50, 'L': 0.15},
        'O': {'M': 0.15, 'N': 0.50, 'P': 0.20},
        'P1':{'P': 0.15},
        'P': {'P1':0.15,'O': 0.20, 'Q': 0.10},
        'Q1': {'Q': 0.15},
        'Q': {'Q1':0.15,'P': 0.10, 'R': 0.10},
        'R1': {'R': 0.15},
        'R': {'R1':0.15,'Q': 0.10, 'S': 0.10},
        'S1': {'S': 0.15},
        'S': {'S1':0.15,'R': 0.10, 'I': 0.50}
    }

    pos = {
        'A1': (0,16),
        'A': (0, 12),
        'B1':(2, 16),
        'B': (2, 12),
        'C1':(4, 16), 
        'C': (4, 12),
        'D1': (6, 16),
        'D': (6, 12),
        'E': (9, 12),
        'F': (18, 12),
        'G': (9, 9),
        'H': (18, 9),
        'I': (18, 6),
        'J': (9, 6),
        'K': (0, 6),
        'L': (0, 3),
        'M': (9, 3),
        'N': (0, 0),
        'O': (9, 0),
        'P1':  (12, -4),
        'P': (12, 0),
        'Q1':  (14, -4),
        'Q': (14, 0),
        'R1':  (16, -4),
        'R': (16, 0),
        'S1':  (18, -4),
        'S': (18, 0)
    }

    source = 'A'
    destination = 'N'
    shortest_path = dijkstra(graph, source, destination)
    draw_graph(graph, pos, shortest_path)

