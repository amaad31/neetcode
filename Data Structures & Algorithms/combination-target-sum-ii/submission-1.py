class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        candidates.sort()
        res_set = defaultdict(list)
        res = []
        def traverse(idx, cur_sum, cur_sol):
            if cur_sum < target and idx < len(candidates):
                traverse(idx + 1, (cur_sum + candidates[idx]), (cur_sol + [candidates[idx]]))
                traverse(idx + 1, cur_sum, cur_sol)
            else:
                if cur_sum == target:
                    if cur_sol not in res_set.values():
                        res_set[len(res_set)] = cur_sol
                        res.append(cur_sol[:])
                return
        traverse(0, 0, [])
        return res