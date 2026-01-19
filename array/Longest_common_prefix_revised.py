#Time: O(N*M)
#Space: O(M)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        for i in range(len(strs[0])):
            arbitrary = strs[0]

            for s in strs:
                if len(s)==i or s[i]!=arbitrary[i]:
                    return res

            res+=strs[0][i]

        return res

                