#Approach =>Sliding window=> expand if same and shrink if diff
#Time: O(N)
#Space : O(N)
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}
        left = 0
        right = 0
        max_freq = 0
        result = 0

        while right<len(s):
            hashmap[s[right]]=hashmap.get(s[right],0)+1
            max_freq=max(max_freq, hashmap[s[right]])

            #check for negative scenario => Invalid window=>shrink from left
            if right-left+1 - max_freq > k:
                hashmap[s[left]]-=1
                left+=1

            result = max(result, right-left+1)
            right+=1

        return result