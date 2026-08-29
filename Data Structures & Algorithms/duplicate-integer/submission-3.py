class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # seen = set()
        # for i in range(len(nums)):
        #     if nums[i] in seen:
        #         return True
        #     seen.add(nums[i])
        # return False

        #alternative approach comparing only the lengths of the set and original array
        return len(set(nums)) < len(nums)