class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        result, path = [], []

        def backtrack():
            if len(path) == len(nums):
                result.append(path[:])
                return 
            
            #exclude : there cannot be an exclude option because all are always included


            #include
            for num in nums:
                if num not in path:
                    path.append(num)
                    backtrack()
                    path.pop()
        backtrack()
        print(result)
        return result
        