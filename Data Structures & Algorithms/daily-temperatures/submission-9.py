class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if not temperatures:
            return []
        
        temps_stack = []
        temps_len = len(temperatures)
        res = [0] * temps_len
        for i in range(temps_len):
            cur_temp = temperatures[i]
            while temps_stack and temps_stack[-1][0] < cur_temp:
                popped_temp, popped_i = temps_stack.pop()
                res[popped_i] = i - popped_i

            if i < temps_len - 1 and cur_temp < temperatures[i + 1]:
                res[i] = 1
            else:
                temps_stack.append((cur_temp, i))
        
        return res