class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers:
            return []
        #numbers = sorted(numbers)
        right_pointer = len(numbers) - 1
        left_pointer = 0
        while(left_pointer<right_pointer):
            curr_sum = numbers[right_pointer] + numbers[left_pointer]
            if curr_sum < target:
                left_pointer += 1
            elif curr_sum > target:
                right_pointer -= 1
            else:
                return [left_pointer + 1, right_pointer + 1]
        return []