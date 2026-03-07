class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()
        l=0
        r=0
        longest_len = 0

        while r<len(s):
            while s[r] in hashset:
                hashset.remove(s[l])
                l+=1

            hashset.add(s[r])
            longest_len = max(longest_len, r-l+1)
            r+=1

        return longest_len
