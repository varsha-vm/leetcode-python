#Time :O(N*M)
#Space: O(N)
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for word in strs:
            count = [0]*26

            for letter in word:
                position = ord('a')-ord(letter)
                count[position]+=1

            count = tuple(count)
            hashmap[count].append(word)


        return list(hashmap.values())