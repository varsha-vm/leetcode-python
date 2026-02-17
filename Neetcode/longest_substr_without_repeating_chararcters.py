#Intuition -> two pointerb
#Approach -> expand as i see new letters, shrink as i see dups
#Time-> O(N)
#Space -> O(min(N, M))
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        r = 0
        hashset = set()

        while r<len(s):
            
            while s[r] in hashset:
                hashset.remove(s[l])
                l+=1

            hashset.add(s[r])
            res = max(res, r-l+1)
            r+=1


        return res
