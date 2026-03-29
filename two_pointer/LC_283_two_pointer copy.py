#Approach: Two-pointer, look out for non-zero integers mainly
#Time: O(N)
#Space: O(1)
class Solution(object):
    def moveZeroes(self, nums):
        l=0
        r=0

        while r<len(nums):
            #if non-zero found, swap
            if nums[r]!=0:
                temp = nums[l]
                nums[l]=nums[r]
                nums[r]=temp
                l+=1
            r+=1
        return nums