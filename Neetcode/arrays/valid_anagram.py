class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
            hashmap_s = {}
            hashmap_t = {}

            for letter in s:
                hashmap_s[letter] = hashmap_s.get(letter, 0)+1
            for letter in t:
                hashmap_t[letter] = hashmap_t.get(letter, 0)+1


            return hashmap_s == hashmap_t