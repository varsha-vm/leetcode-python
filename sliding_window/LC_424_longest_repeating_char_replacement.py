#Appraoch: when invalid, reduce
#Time: O(N)
#Space: O(N)
class Solution(object):
    def characterReplacement(self, s, k):
        hashmap={}
        l=0
        max_freq=0
        result = 0

        for r in range(len(s)):
            hashmap[s[r]]=hashmap.get(s[r],0)+1
            max_freq=max(max_freq, hashmap[s[r]])

            #if invalid
            if (r-l+1) - max_freq > k:
                hashmap[s[l]]-=1
                l+=1

            result = max(max_freq, r-l+1)

        return result