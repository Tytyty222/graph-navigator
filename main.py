from graphs.graph_factory import GraphFactory

from algorithms.traversal import bfs, dfs

from algorithms.shortest_path import (
    dijkstra,
    shortest_path_bfs
)

from storage.json_storage import (
    save_graph,
    load_graph
)


def main():

    print("GRAPH NAVIGATOR")

    graph = GraphFactory.create_graph("weighted")

    graph.add_node("A")
    graph.add_node("B")
    graph.add_node("C")
    graph.add_node("D")

    graph.add_edge("A", "B", 5)
    graph.add_edge("A", "C", 2)
    graph.add_edge("C", "D", 1)
    graph.add_edge("B", "D", 3)

    print("\nGraph:")
    graph.display()

    print("\nBFS traversal:")
    print(bfs(graph, "A"))

    print("\nDFS traversal:")
    print(dfs(graph, "A"))

    print("\nShortest path BFS:")
    print(shortest_path_bfs(graph, "A", "D"))

    print("\nDijkstra shortest paths:")
    print(dijkstra(graph, "A"))

    save_graph(graph, "graph.json")

    print("\nGraph saved to JSON")

    print("\nValidation tests:")

    try:
        graph.add_node("A")

    except ValueError as error:
        print(error)

    try:
        graph.add_edge("A", "B", -5)

    except ValueError as error:
        print(error)


if name == "__main__":
    main()
