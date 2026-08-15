class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        counter_map = Counter(nums)
        freq_arr = [[] for _ in range(len(nums) + 1)]

        for num in list(set(nums)):
            freq_arr[counter_map[num]].append(num)
        
        res = []
        for i in range(len(nums), 0, -1):
            cur_arr = freq_arr[i]
            if not freq_arr[i]:
                continue
            while(k > 0 and cur_arr):
                res.append(cur_arr.pop())
                if len(res) == k:
                    return res
        
        return res
                