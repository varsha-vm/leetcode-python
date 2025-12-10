#Approach: optimized -> dictionary + tuple of characters + list of values
#Time: O(N*K)
#Space: O(N*K)
class Solution(object):
    def groupAnagrams(self, strs):
        hashmap = {}

        for word in strs:
            count = [0]*26

            for ch in word:
                count[ord(ch) - ord("a")]+=1
            
            key = tuple(count)

            if key not in hashmap:
                hashmap[key]=[]
            
            hashmap[key].append(word)

        return list(hashmap.values())

