class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        res = [-1, -1]
        mid_target = -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                mid_target = mid
                break
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        if nums[mid_target] != target:
            return [-1, -1]

        mid_target = mid
        l, r = 0, mid_target
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        res[0] = l

        l, r = mid_target, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] <= target:
                res[1] = mid
                l = mid + 1
            else:
                r = mid - 1
        
        return res
        