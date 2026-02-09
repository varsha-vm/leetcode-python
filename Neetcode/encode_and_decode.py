class Solution:
    def encode(self, strs: List[str]) -> str:
        res_str = ""
        for s in strs:
            length = len(s)
            deli = '#'
            res_str+=(str(length) + deli + s)

        return res_str

    def decode(self, s: str) -> List[str]:
        r=len(s)-1
        i = 0
        res = []

        while i<=r:
            j = i

            while s[j]!='#':
                j+=1

            len_of_s = int(s[i:j])
            res.append(s[j+1:j+1+len_of_s])
            i = j+1+len_of_s

        return res