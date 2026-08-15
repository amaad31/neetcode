class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:        
        nums_map = defaultdict(int)

        for i in range(len(nums)):
            num = nums[i]
            diff = target - num
            if diff in nums_map.keys():
                return [nums_map[target - num], i]
            nums_map[num] = i
        
        return []
