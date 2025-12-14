#Approach: Last open, close first
#Time: O(N)
#Space: O(N)
class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
                    ')': '(',
                    ']': '[',
                    '}': '{'
                }

        stack = []

        for i in s:
            #if opening brackets only, push to stack
            if i in mapping.values():
                stack.append(i)

            #if closing bracket, check for the match
            else:
                #if stack is empty
                if not stack:
                    return False

                top_ele = stack.pop()
                if top_ele != mapping[i]:
                    return False


        return not stack




