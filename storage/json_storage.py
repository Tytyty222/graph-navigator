import json


def save_graph(graph, filename):

    data = {
        "nodes": graph.get_nodes(),
        "edges": []
    }

    for node in graph.get_nodes():

        for neighbor, weight in graph.get_neighbors(node).items():

            data["edges"].append({
                "src": node,
                "dest": neighbor,
                "weight": weight
            })

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def load_graph(graph, filename):

    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)

    for node in data["nodes"]:
        graph.add_node(node)

    for edge in data["edges"]:

        graph.add_edge(
            edge["src"],
            edge["dest"],
            edge["weight"]
        )

    return graph
