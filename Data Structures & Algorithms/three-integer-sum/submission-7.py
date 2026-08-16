class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = list(sorted(nums))
        nums_len = len(nums)
        res = []
        i = 0
        while i < nums_len:
            if i > 0 and nums[i - 1] == nums[i]:
                i += 1
                continue
            l, r = i + 1, nums_len - 1
            while l < r:
                cur_sum = nums[i] + nums[l] + nums[r]
                if 0 == cur_sum:
                    res.append([nums[i], nums[l], nums[r]])
                    r -= 1
                    while nums[r] == nums[r + 1] and l < r:
                        r -= 1
                elif cur_sum < 0:
                    l += 1
                else:
                    r -= 1
            i += 1
        return res