#Time:O(N * M)
#Space: O(N * M)
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for word in strs:
            key = [0]*26

            for letter in word:
                pos = ord(letter) - ord('a') 
                key[pos]+=1

            key = tuple(key)
            hashmap[key].append(word)

        return list(hashmap.values())