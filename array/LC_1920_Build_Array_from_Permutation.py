#Approach => Encode and decode to keep it in place
#Time => O(N)
# Space => O(1)
class Solution(object):
    def buildArray(self, nums):
        n = len(nums)
        #Encode w/ secret formula => (old + n * new)
        for i in range(n):
            new_value = nums[nums[i]] % n
            old_value = nums[i]
            nums[i] = old_value + n * new_value
        
        #Decode
        for i in range(n):
            nums[i] = nums[i] // n

        return nums

        