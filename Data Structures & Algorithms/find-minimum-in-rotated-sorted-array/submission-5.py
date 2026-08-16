class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return 0

        len_nums = len(nums)
        l, r = 0, len_nums - 1

        if nums[l] <= nums[r]:
            return nums[l]

        while nums[l] > nums[r]:
            mid = (l + r) // 2
            if nums[l] < nums[mid]:
                l = mid
            else:
                r = mid

        return nums[r + 1]


        