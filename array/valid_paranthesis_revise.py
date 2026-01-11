#Approach : last open much be close first, for which stack is perfect to push and pop
#Time: O(N)
#Space: O(N)
class Solution(object):
    def isValid(self, s):
        hashmap = {
                '}':'{',
                ']':'[',
                ')':'('
        
        }
        
        stack = []

        for i in s:
            if i not in hashmap:
                stack.append(i)

            else:
                if not stack:
                    return False
                
                else:
                    if hashmap[i]!=stack.pop():
                        return False

        return not stack