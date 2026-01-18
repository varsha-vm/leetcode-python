class Solution(object):
    def missingNumber(self, nums):
        xor = 0
        n = len(nums)

        #xor numbers fron 0 to n
        for i in range(n+1):
            xor = xor ^ i

        #xor numbers in nums
        for i in nums:
            xor = xor ^ i

        return xor