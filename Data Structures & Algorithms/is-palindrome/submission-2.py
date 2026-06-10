class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = [x.lower() for x in s if x.isalnum()]
        print(res)
        return res == res[::-1]

        #return False
        