class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = ["+", "-", "*", "/"]

        for el in tokens:
            if el not in operands:
                stack.append(int(el))

            if el in operands and len(stack) >= 2:
                a  = stack.pop()
                b  = stack.pop()

                if el == "+":
                    stack.append(int(a+b))
                elif el == "*":
                    stack.append(int(a*b))
                elif el == "-":
                    stack.append(int(b- a))
                
                else:
                    if b != 0:
                        stack.append(int(b/a))
                    else:
                        stack.append(0)
        return stack[0]
                
                
                
            

            
        
        print(stack)
        # print(first)

        return 0
        