class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list) # stores key to an array of (timestamps, values)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap or timestamp < self.timemap[key][0][0]:
            return ""
        cur_arr = self.timemap[key]
        l, r = 0, len(cur_arr) - 1
        mid = 0
        res = -1
        while l <= r:
            mid = l + ((r - l) // 2)
            mid_num = cur_arr[mid][0]
            if mid_num <= timestamp:
                res = mid
                l = mid + 1
            else:
                r = mid - 1
        return cur_arr[res][1]
