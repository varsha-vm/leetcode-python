#Time: O(n*m)
#Space:O(1)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_word_len = len(strs[0])
        res = ""

        for i in range(first_word_len):
            arbitrary_letter = strs[0][i]

            for word in strs:
                if i==len(word) or arbitrary_letter!=word[i]:
                    return res

            res+=arbitrary_letter


        return res
