from graphs.base_graph import Graph


class UndirectedGraph(Graph):

    def add_edge(self, src, dest, weight=1):

        if src not in self._adjacency:
            raise ValueError("Source node does not exist")

        if dest not in self._adjacency:
            raise ValueError("Destination node does not exist")

        self._adjacency[src][dest] = weight
        self._adjacency[dest][src] = weight
