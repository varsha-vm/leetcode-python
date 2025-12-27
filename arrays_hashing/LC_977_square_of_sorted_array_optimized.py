#Approach : When array is sorted in ascending ordern and values change sign, compare ends and place max value at back
#Time: O(N)
#Space: O(N)
class Solution(object):
    def sortedSquares(self, nums):
        l=0
        r=len(nums)-1
        pos=len(nums)-1
        result=[0]*len(nums)

        while pos>=0:
            squared_r = nums[r]*nums[r]
            squared_l = nums[l]*nums[l]

            if squared_l>squared_r:
                result[pos]=squared_l
                l+=1
            else:
                result[pos]=squared_r
                r-=1

            pos-=1

        return result
             
        
        