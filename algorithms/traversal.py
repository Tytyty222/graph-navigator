from collections import deque


def bfs(graph, start):

    visited = set()
    queue = deque([start])

    result = []

    while queue:

        node = queue.popleft()

        if node not in visited:

            visited.add(node)
            result.append(node)

            for neighbor in graph.get_neighbors(node):
                queue.append(neighbor)

    return result


def dfs(graph, start):

    visited = set()
    result = []

    def _dfs(node):

        visited.add(node)
        result.append(node)

        for neighbor in graph.get_neighbors(node):

            if neighbor not in visited:
                _dfs(neighbor)

    _dfs(start)

    return result
