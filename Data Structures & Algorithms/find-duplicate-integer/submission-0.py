class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        counter = Counter(nums)
        for num in nums:
            if counter[num] > 1 :
                return num
        