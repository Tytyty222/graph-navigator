from graphs.directed_graph import DirectedGraph


class WeightedGraph(DirectedGraph):

    def add_edge(self, src, dest, weight=1):

        if weight < 0:
            raise ValueError("Weight cannot be negative")

        super().add_edge(src, dest, weight)
