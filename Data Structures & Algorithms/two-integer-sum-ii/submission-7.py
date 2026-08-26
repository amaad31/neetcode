class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers:
            return []
        
        l, r = 0, len(numbers) - 1
        while l < r:
            left_val, right_val = numbers[l], numbers[r]
            if left_val + right_val == target:
                return [l + 1, r + 1]
            elif left_val + right_val > target:
                r -= 1
            else:
                l += 1
        return []