class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #return sorted(s) == sorted(t)
        #this solution is easier using sorting, but it has O(nlogn) time complexity and O(n) space


        #this second solution, although is longer, has O(n) time complexity and O(1) space complexity
        s_low = s.lower()
        t_low = t.lower()
        if len(t) != len(s):
            return False
        final_arr = [0]*26
        for i in range(len(s)):
            final_arr[ord(s_low[i]) - ord('a')] += 1
        
        for i in range(len(t)):
            final_arr[ord(t_low[i]) - ord('a')] -= 1
        
        for i in range(len(final_arr)):
            if final_arr[i] > 0:
                return False
        return True
        
        