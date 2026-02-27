#Time:O(n*m)
#Space:O(n*m)
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        res = []

        for word in strs:
            count = [0]*26

            for l in word:
                pos = ord(l) - ord('a')
                count[pos]+=1

            count = tuple(count)
            hashmap[count].append(word)


        return list(hashmap.values())
