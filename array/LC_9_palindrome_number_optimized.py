class Solution:
    def isPalindrome(self, x: int) -> bool:
        #negative scenario
        if x<0 or x%10==0 and x!=0:
            return False

        reversed_last_digits = 0
        
        while x>reversed_last_digits:
            get_last_digit = x%10
            reversed_last_digits = reversed_last_digits * 10 + get_last_digit
            x//=10

        return x==reversed_last_digits or x==reversed_last_digits//10
