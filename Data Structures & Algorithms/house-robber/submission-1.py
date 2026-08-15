class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        leng = len(nums)
        if leng == 1:
            return nums[0]
        elif leng == 2:
            return max(nums[0], nums[1])
        last_to_last = nums[0]
        last = nums[1]
        res = max(last_to_last, last)
        for i in range(2, leng):
            num = nums[i]
            if num + last_to_last > last:
                res = num + last_to_last
            temp_last = last
            last = num + last_to_last
            last_to_last = max(last_to_last, temp_last)
        return res