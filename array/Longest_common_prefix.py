#Time: O(n*m)
#Space: O(m)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        first_word_len = len(strs[0])

        for i in range(first_word_len):
            arbitrary_first_word = strs[0][i]
            for s in strs:
                if i==len(s) or s[i] != arbitrary_first_word:
                    return ans 

            
            ans+=strs[0][i]

        return ans
