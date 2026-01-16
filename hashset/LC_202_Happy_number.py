#Time : O(N)
#Space: O(N)
class Solution(object):
    def sum_of_digits(self, n):
        res = 0
        while n:
            digit = n%10
            digit = digit**2
            res += digit
            n//=10

        return res


    def isHappy(self, n):
        hashset = set()

        while n not in hashset:
            hashset.add(n)
            if n == 1:
                return True

            else:
                n = self.sum_of_digits(n)


        return False
