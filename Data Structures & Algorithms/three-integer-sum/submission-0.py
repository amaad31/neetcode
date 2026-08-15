class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        output = []
        n = len(nums)
        for i in range(n):
            for j in range(0, n - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        # [-4, -1, ,-1, 0, 1, 2] 
        for left_pointer in range(n - 2):
            right_pointer = n - 1
            middle_pointer = left_pointer + 1
            while middle_pointer < right_pointer:
                curr_sum = nums[right_pointer] + nums[left_pointer] + nums[middle_pointer]
                if curr_sum == 0:
                    sub_output = [nums[right_pointer], nums[middle_pointer], nums[left_pointer]]
                    if sub_output not in output:
                        output.append(sub_output)
                    right_pointer -= 1
                    middle_pointer += 1
                elif curr_sum < 0:
                    middle_pointer += 1
                    continue
                else:
                    right_pointer -= 1
                    continue
        return output
                 

