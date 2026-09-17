class Solution:
    def isValid(self, s: str) -> bool:
        #tried solving it agani after a while and got this 
        stack = []
        hashmap={')':'(', ']':'[', '}':'{'}

        for i in s:
            if i not in hashmap:
                stack.append(i)
            else:
                if not stack:
                    return False
                if stack[-1] == hashmap[i]:
                    stack.pop()
                else:
                    return False
            

        if len(stack) !=0:
            return False
        else:
            return True 
        """stack = []
        hashmap={')':'(', ']':'[', '}':'{'}

        for char in s:
            if char in hashmap:
                if stack and stack[-1] == hashmap[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False
        """  
            
        