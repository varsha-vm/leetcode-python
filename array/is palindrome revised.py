
class Solution(object):
    def isPalindrome(self, x):
        if x < 0 or x%10==0 and x!=0:
            return False

        last_reversed = 0
        
        while x>last_reversed:
            last_digit = x%10
            last_reversed = last_reversed * 10 + last_digit
            x//=10
         

        return x == last_reversed or x==last_reversed//10
