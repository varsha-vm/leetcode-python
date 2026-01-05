#Time: O(N * M)
#Space: O(N * M)
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        
        for word in strs:
            count = [0]* 26 #a-z => 26 letters

            for char in word:
                pos = ord(char)-ord("a")
                count[pos]+=1

            key = tuple(count) #Coz dict keys need to be immutable and tuples are immutable

            hashmap[key].append(word) 

        return list(hashmap.values())  


