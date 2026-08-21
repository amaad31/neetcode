class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for point in points:
            distance = math.sqrt(point[0] * point[0] + point[1] * point[1])
            if len(distances) == k:
                heapq.heappushpop(distances, (-distance, point))
            else:
                heapq.heappush(distances, (-distance, point))
            
        res = []
        while distances:
            res.append(distances.pop()[1])
        
        return res