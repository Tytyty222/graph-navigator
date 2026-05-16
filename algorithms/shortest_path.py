from collections import deque
import heapq


def shortest_path_bfs(graph, start, goal):

    queue = deque([(start, [start])])
    visited = set()

    while queue:

        node, path = queue.popleft()

        if node == goal:
            return path

        visited.add(node)

        for neighbor in graph.get_neighbors(node):

            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    return None


def dijkstra(graph, start):

    distances = {node: float("inf") for node in graph.get_nodes()}
    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:

        current_distance, current_node = heapq.heappop(priority_queue)

        for neighbor, weight in graph.get_neighbors(current_node).items():

            distance = current_distance + weight

            if distance < distances[neighbor]:

                distances[neighbor] = distance

                heapq.heappush(
                    priority_queue,
                    (distance, neighbor)
                )

    return distances
