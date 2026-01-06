#Time: O(n)
#Space: O(d)
class Solution(object):
    def isPalindrome(self, x):
        l = 0
        strs_x = str(x)
        r = len(strs_x)-1

        while l<r:
            if strs_x[l]!=strs_x[r]:
                return False

            l+=1
            r-=1

        return True