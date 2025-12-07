#product of array = (product of left side) * ( product of right side)
#Time: O(N)
#Space: O(N)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        

        #product of left side
        result = [1] * len(nums)
        left_prod = 1

        for i in range(len(nums)):
            result[i] = left_prod
            left_prod*=nums[i]


        #product of right side
        right_prod = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] = right_prod * result[i]
            right_prod = right_prod * nums[i]
        
        return result 
        

