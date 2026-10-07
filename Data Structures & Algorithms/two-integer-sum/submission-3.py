class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #the space complexity is O(n)
        #the time complexity is O(n)
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[nums[i]]  = i
        
        #doesn't even matter since we're guaranteed there are duplicates
        return
        
        