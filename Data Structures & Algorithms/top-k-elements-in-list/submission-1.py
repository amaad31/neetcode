class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numbers_count = defaultdict(int)
        for num in nums:
            numbers_count[num] = numbers_count.get(num, 0) + 1
        numbers_count = dict(sorted(numbers_count.items(), key=lambda item: item[1]))
        return list(numbers_count.keys())[-k:]
        #sorted_numbers_list = [0] * (max(numbers_count.values()) + 1)
        #for number, count in numbers_count.items():
         #   sorted_numbers_list[count] = number
        #return sorted_numbers_list[-k:]