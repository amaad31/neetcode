class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            return [course for course in range(numCourses)]
        
        edges_map = defaultdict(list)
        full_record = set()
        output = []

        def dfs(node, record):
            if node in record:
                return False

            if node in full_record:
                return True

            record.add(node)
            full_record.add(node)
            for pre in edges_map[node]:
                if not dfs(pre, record):
                    return False
            record.remove(node)
            output.append(node)
            return True

        for edge in prerequisites:
            edges_map[edge[0]].append(edge[1])

        for node in range(numCourses):
            if node not in full_record:
                res = dfs(node, set())
                if not res:
                    return []
        
        return output