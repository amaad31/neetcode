class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges:
            return True

        edges_map = defaultdict(list)
        visited = set()

        for edge in edges:
            edges_map[edge[0]].append(edge[1])
            edges_map[edge[1]].append(edge[0])

        def dfs(node, prev):
            if node in visited:
                return False
            
            visited.add(node)
            for ngbr in edges_map[node]:
                if ngbr == prev:
                    continue
                if not dfs(ngbr, node):
                    return False
            
            return True

        if not dfs(0, None):
            return False

        if len(visited) == n:
            return True
        
        return False