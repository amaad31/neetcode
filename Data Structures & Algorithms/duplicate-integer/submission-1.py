class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter_map = Counter(nums)

        for num, count in counter_map.items():
            if count > 1:
                return True
        
        return False