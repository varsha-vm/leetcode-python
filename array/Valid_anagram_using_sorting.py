#Time: O(N LOG N)
#Space: O(1)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s)==sorted(t)