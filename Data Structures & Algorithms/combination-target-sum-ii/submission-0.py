class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()  # Fix 4: must sort first
        res = []

        def backtracking(start, curr, total):  # Fix 1: renamed i to start
            if total == target:
                res.append(list(curr))
                return

            if total > target:
                return

            prev = -1
            for i in range(start, len(candidates)):  # Fix 1: start from 'start', not 0
                if candidates[i] == prev:
                    continue
                curr.append(candidates[i])
                backtracking(i + 1, curr, total + candidates[i])  # Fix 2: total + not +=
                curr.pop()
                prev = candidates[i]  # Fix 3: prev not pev, candidates not candidate

        backtracking(0, [], 0)
        return res