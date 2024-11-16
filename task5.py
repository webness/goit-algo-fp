import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
import time


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            pos[node.left.id] = (x - 1 / 2 ** layer, y - 1)
            add_edges(graph, node.left, pos, x=x - 1 / 2 ** layer, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            pos[node.right.id] = (x + 1 / 2 ** layer, y - 1)
            add_edges(graph, node.right, pos, x=x + 1 / 2 ** layer, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, visited_nodes=None):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = []
    for node in tree.nodes(data=True):
        node_id = node[0]
        if visited_nodes and node_id in visited_nodes:
            colors.append(visited_nodes[node_id])
        else:
            colors.append(node[1]['color'])

    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(12, 8))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def bfs_traversal(tree_root):
    queue = deque([tree_root])
    visited_nodes = {}
    step = 0

    while queue:
        node = queue.popleft()

        # Assign color based on traversal order
        color = f"#{hex(0x1296F0 + step * 50)[2:]}"  # Darker to lighter blue shades
        visited_nodes[node.id] = color
        step += 1

        draw_tree(tree_root, visited_nodes)  # Visualize current state
        time.sleep(1)  # Pause for better visualization

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


def dfs_traversal(tree_root):
    stack = [tree_root]
    visited_nodes = {}
    step = 0

    while stack:
        node = stack.pop()

        # Assign color based on traversal order
        color = f"#{hex(0x1296F0 + step * 50)[2:]}"  # Darker to lighter blue shades
        visited_nodes[node.id] = color
        step += 1

        draw_tree(tree_root, visited_nodes)  # Visualize current state
        time.sleep(1)  # Pause for better visualization

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)


def build_large_tree(depth):
    if depth == 0:
        return None

    root = Node(0)

    def build_tree(node, current_depth):
        if current_depth < depth:
            node.left = Node(node.val * 2 + 1)
            node.right = Node(node.val * 2 + 2)
            build_tree(node.left, current_depth + 1)
            build_tree(node.right, current_depth + 1)

    build_tree(root, 1)
    return root


if __name__ == "__main__":
    depth = 4
    root = build_large_tree(depth)

    print("Breadth-First Traversal:")
    bfs_traversal(root)

    print("\n3Depth-First Traversal:")
    dfs_traversal(root)
