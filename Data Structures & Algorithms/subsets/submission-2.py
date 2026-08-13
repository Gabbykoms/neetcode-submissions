class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #if we reach the end, we should have found a solution
        #at each point, we decide we want to add the point or not add it

        result = []
        path = []

        def backtrack(i, path):
            if i == len(nums):
                result.append(path[:])
                return 
            
            #exclude
            backtrack(i+1, path)

            #include
            path.append(nums[i])
            backtrack(i+1, path)
            path.pop()
        backtrack(0, path)
        return result
            
           



        
                
                    

                             
        