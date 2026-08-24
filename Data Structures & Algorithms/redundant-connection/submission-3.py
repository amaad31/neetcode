class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        if not edges:
            return []

        edges_map = defaultdict(list)
        visited = set()
        res = [set()]

        for edge in edges:
            edges_map[edge[0]].append(edge[1])
            edges_map[edge[1]].append(edge[0])

        def dfs(node, prev, path):
            if node in visited:
                res[0] = path.copy()
                return False

            visited.add(node)
            path.add(node)

            for neighbor in edges_map[node]:
                if neighbor == prev:
                    continue

                if not dfs(neighbor, node, path):
                    return False

            path.remove(node)
            return True

        for node in edges_map.keys():
            if node not in visited:
                if not dfs(node, None, set()):
                    break

        for i in range(len(edges) - 1, -1, -1):
            x, y = edges[i]
            if x in res[0] and y in res[0]:
                return [x, y]

        return []