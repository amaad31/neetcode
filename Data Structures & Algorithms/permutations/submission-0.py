class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return
        result = []
        path = []
        used = set()

        def backtrack():
            if len(path) == len(nums):
                result.append(path[:])
                return

            for num in nums:
                if num in used:
                    continue
                path.append(num)
                used.add(num)
                backtrack()
                path.pop()
                used.remove(num)

        backtrack()
        return result