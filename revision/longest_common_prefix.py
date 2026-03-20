class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        for i in range(len(strs[0])):
            arbitrary = strs[0]

            for s in strs:
                if i==len(s) or arbitrary[i]!=s[i]:
                    return res

            res+=arbitrary[i]

        return res
