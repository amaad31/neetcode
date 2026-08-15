class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # a      ,b      ,c      ,d
        # 1      ,a      ,a*b    ,a*b*c
        # b*c*d  ,c*d    ,d      ,1
        # 1, 1, 2, 8
        # 48, 24, 6, 1
        if not nums:
            return []
        nums_len = len(nums)
        left_mul = [1] * nums_len
        right_mul = [1] * nums_len

        for i in range(1, nums_len):
            num = nums[i - 1]
            right_mul[i] = right_mul[i - 1] * num
        
        for i in range(nums_len - 2, -1, -1):
            num = nums[i + 1]
            left_mul[i] = left_mul[i + 1] * num
        
        res = []
        for i in range(nums_len):
            res_i = (left_mul[i] * right_mul[i])
            res.append(res_i)

        return res