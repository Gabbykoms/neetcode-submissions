class Solution:
    def isValid(self, s: str) -> bool:
        
        #define a hashmap between opening/closing
        hashmap = {')':'(', '}':'{', ']':'['}
        open_ = ['(', '[', '{']
        stack = []

        for brac in s:
            if brac in open_:
                stack.append(brac)
            elif brac in hashmap:
                if not stack or stack[-1] != hashmap[brac]:
                        return False
                stack.pop()
            
        

        return len(stack) == 0

        