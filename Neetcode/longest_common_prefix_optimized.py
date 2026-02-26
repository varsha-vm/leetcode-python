class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        first_word_len = len(strs[0])

        for i in range(first_word_len):
            arbitrary = strs[0][i]

            for j in range(1, len(strs)):
                word = strs[j]
                if len(word)==i or word[i]!=arbitrary:
                    return ans

                
            ans+=strs[0][i]


        return ans