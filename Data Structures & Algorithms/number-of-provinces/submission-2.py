class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if not isConnected:
            return 0
        prov = len(isConnected[0])
        parent = [1] * (prov + 1)
        for i in range(1, prov + 1):
            parent[i] = i
        rank = [1] * (prov + 1)
        res = prov
        def find(city):
            while parent[city] != city:
                city = parent[city]
            return city
        def union(city1, city2):
            par1, par2 = find(city1), find(city2)
            if par1 == par2:
                return 0
            if rank[par1] < rank[par2]:
                parent[par2] = par1
                rank[par1] += rank[par2]
                rank[par2] = 1
            else:
                parent[par1] = par2
                rank[par2] += rank[par1]
                rank[par1] = 1
            return 1

        for city1 in range(1, len(isConnected) + 1):
            for city2 in range(1, prov + 1):
                if isConnected[city1 - 1][city2 - 1] == 1:
                    res -= union(city1, city2)
        return res