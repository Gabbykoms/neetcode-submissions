class Solution:
    def maxArea(self, heights: List[int]) -> int:

        ptr1, ptr2 = 0, len(heights)-1
        max_wtr = 0

        while ptr1 <= ptr2:
            curr_wtr = (ptr2 - ptr1)* min(heights[ptr1], heights[ptr2])
            max_wtr = max(max_wtr, curr_wtr)
            if heights[ptr1] <= heights[ptr2]:
                ptr1 += 1
            else:
                ptr2 -= 1

        
        return max_wtr
        