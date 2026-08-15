class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, (len(nums) - 1)
        while l <= r:
            m = (l + r) // 2
            if (nums[l] <= nums[m]) and (nums[m] <= nums[r]):
                return nums[l]
            elif (nums[l] >= nums[m]) and (nums[m] >= nums[r]):
                return nums[r]
            elif (nums[l] >= nums[m]) and (nums[m] <= nums[r]):
                r = m
            else:
                l = m
        return None