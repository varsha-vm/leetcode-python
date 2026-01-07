#Time: O(N)
#Space: O(1)
class Solution:
    def romanToInt(self, s: str) -> int:
        hashmap = {
                        'I':1,
                        'V':5,
                        'X':10,
                        'L':50,
                        'C':100,
                        'D':500,
                        'M':1000        
                    }

        result = 0

        #left to righ => Addition scenario
        for i in range(len(s)):
            cur_val = hashmap[s[i]]
            #If next value exists
            if i+1<len(s) and cur_val < hashmap[s[i+1]]:
                result-=cur_val
            else:
                result+=cur_val

        return result

