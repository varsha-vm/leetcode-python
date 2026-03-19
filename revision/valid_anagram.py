#Time: O(N)
#SpaceL O(N)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_t = dict()
        hash_s = dict()

        for i in s:
            hash_s[i] = hash_s.get(i, 0)+1
        
        for j in t:
            hash_t[j] = hash_t.get(j, 0)+1


        return hash_t == hash_s