class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        output = [0] * length
        stack = []
        stack_idx = []
        for i in range(1, length):
            if temperatures[i - 1] < temperatures[i]:
                output[i - 1] = 1
                if stack:
                    while stack and temperatures[i] > stack[-1]:
                        popped = stack.pop()
                        popped_idx = stack_idx.pop()
                        output[popped_idx] = i - popped_idx
            else:
                stack.append(temperatures[i - 1])
                stack_idx.append(i - 1)

        return output
            

