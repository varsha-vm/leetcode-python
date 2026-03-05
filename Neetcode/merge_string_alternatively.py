#Time: O(N)
#Time: O(N)
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res=[]
        i=0
        j=0
        n = len(word1)
        m = len(word2)

        while i<n or j<m:
            if i<n:
                res.append(word1[i])

            if j<m:
                res.append(word2[j])


            i+=1
            j+=1

        return "".join(res)