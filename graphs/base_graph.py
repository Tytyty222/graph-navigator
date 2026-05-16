from collections import defaultdict


class GraphNode:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)


class Graph:
    def __init__(self):
        self._adjacency = defaultdict(dict)

    def add_node(self, node):

        if node in self._adjacency:
            raise ValueError("Node already exists")

        self._adjacency[node] = {}

    def remove_node(self, node):

        if node not in self._adjacency:
            raise ValueError("Node does not exist")

        self._adjacency.pop(node)

        for neighbor in self._adjacency:
            self._adjacency[neighbor].pop(node, None)

    def add_edge(self, src, dest, weight=1):
        raise NotImplementedError

    def remove_edge(self, src, dest):

        if src in self._adjacency:
            self._adjacency[src].pop(dest, None)

    def get_neighbors(self, node):
        return self._adjacency[node]

    def get_nodes(self):
        return list(self._adjacency.keys())

    def display(self):

        for node, neighbors in self._adjacency.items():
            print(f"{node} -> {neighbors}")
