#Approach : hashmap & compare
#Time: o(N)
#Space: O(N+M) => o(N)
class Solution(object):
    def isAnagram(self, s, t):
        bucket_s = {}
        bucket_t = {}

        for char in s:
            bucket_s[char] = bucket_s.get(char, 0)+1

        for char in t:
            bucket_t[char] = bucket_t.get(char, 0)+1 


        return bucket_s == bucket_t