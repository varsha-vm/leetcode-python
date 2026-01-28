#Time: O(N*M)
#Space : O(N*M)
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]: 
        hashmap = defaultdict(list)

        for word in strs:
            count = [0] * 26

            for letter in word:
                idx_letter = ord(letter) - ord('a')
                count[idx_letter]+=1

            tuple_count = tuple(count)
            hashmap[tuple_count].append(word)

        return list(hashmap.values())