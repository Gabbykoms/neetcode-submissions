class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = [x.lower() for x in s if x.isalnum()]
        return res == res[::-1]

        #return False
        