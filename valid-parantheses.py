# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for c in s:
            if c == ')':
                if len(stack) > 0 and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            
            elif c =='}':
                if len(stack) > 0 and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            
            elif c == ']':
                if len(stack) > 0 and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
            
        
        if len(stack) != 0:
            return False
        
        return True
                 
            
