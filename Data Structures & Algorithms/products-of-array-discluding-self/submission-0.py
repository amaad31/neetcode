class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        left_product_list = [1] * nums_len
        right_product_list = [1] * nums_len
        output = [1] * nums_len
        for i in range(1, nums_len):
            left_product_list[i] = left_product_list[i - 1] * nums[i - 1]
        for i in range(nums_len - 2, -1, -1):
            right_product_list[i] = right_product_list[i + 1] * nums[i + 1]
        for i in range(nums_len):
            output[i] = left_product_list[i] * right_product_list[i]
        return output