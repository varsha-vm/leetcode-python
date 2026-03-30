#Approach : When array is sorted in ascending ordern and values change sign, compare ends and place max value at back
#Time: O(N)
#Space: O(N)
class Solution(object):
    def sortedSquares(self, nums):
        l=0
        r=len(nums)-1
        position = len(nums)-1
        result = [0]*len(nums)

        while position>=0:
            squared_l=nums[l]*nums[l]
            squared_r=nums[r]*nums[r]
            
            if squared_l>squared_r:
                    result[position]=squared_l
                    l+=1
                    position-=1
            else:
                result[position]=squared_r
                r-=1
                position-=1

        return result
