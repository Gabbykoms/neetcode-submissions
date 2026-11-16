class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        path = []

        def backtrack(ind, path):
            s = sum(path)
            if s == target:
                result.append(path[:])
                return 
            if s > target or ind == len(nums):
                return
            
            #exclude
            backtrack(ind+1, path)

            #include
            path.append(nums[ind])
            backtrack(ind, path)
            path.pop()

        backtrack(0, [])
        return result
        