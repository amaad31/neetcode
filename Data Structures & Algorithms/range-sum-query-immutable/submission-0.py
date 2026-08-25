class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.leng = len(nums)
        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        if left < 0 or right >= self.leng or left > right:
            return 0
        
        res = 0
        for i in range(left, right + 1):
            res += self.nums[i]
        return res