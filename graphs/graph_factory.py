from graphs.directed_graph import DirectedGraph
from graphs.undirected_graph import UndirectedGraph
from graphs.weighted_graph import WeightedGraph


class GraphFactory:

    @staticmethod
    def create_graph(graph_type):

        if graph_type == "directed":
            return DirectedGraph()

        if graph_type == "undirected":
            return UndirectedGraph()

        if graph_type == "weighted":
            return WeightedGraph()

        raise ValueError("Unknown graph type")
