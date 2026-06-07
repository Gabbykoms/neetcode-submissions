class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0
        longest = 1
        for i in range(len(nums)):
            curr = nums[i]
            
            count = 1
            while curr + 1 in nums:
                count += 1
                curr += 1
            longest = max(longest, count)
        
        return longest



        