#Approach: hashmap + sorted keys + list comprahension
#Time: N (K log K)
#Space: O(N*K)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_anagrams = {}

        for i in strs:
            key_word = "".join(sorted(i))
            if key_word not in group_anagrams:
                group_anagrams[key_word] = []
            
            group_anagrams[key_word].append(i)

        return list(group_anagrams.values())
