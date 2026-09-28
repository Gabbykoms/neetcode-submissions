class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        if not nums:
            return []
        nums.sort()
        res = []

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            
            if i > 0 and (nums[i-1] == nums[i]):
                continue
            l = i + 1
            r = len(nums) - 1

            while l < r:
                if (nums[i] + nums[l] + nums[r]) > 0:
                    r -= 1
                elif (nums[i] + nums[l] + nums[r]) < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        
        return res


        